import sys
import os
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

import sublime_plugin
import sublime
import threading

from .lib import helpers
from .lib import collector

keys = {
    "SPACE": "<space>",
    "ESCAPE": "<esc>"
}


class SpaceListener(sublime_plugin.EventListener):
    settings = {
        'shortcut_overlay_timeout': 0.2,
        'show_shortcut_overlay': True
    }

    command_chain = []
    last_key = None
    inChain = False
    shortcut_panel = None
    help_timeout = None
    collector = None
    cached_action_tree = None

    def generate_action_tree(self):
        if self.cached_action_tree:
            return self.cached_action_tree

        keymap = self.collector.collect_key("sublimious_keymap")

        action_tree = {}
        for command in keymap:
            keys = command.get("keys")
            action = command.get("command", None)
            category = command.get("category", None)
            description = command.get("description", None)
            args = command.get("args", {})

            leaf = {}
            first = True
            for key in reversed(keys):
                if first:
                    first = False
                    if action:
                        leaf[key] = {"action": action, "args": args, "description": description}

                    if category:
                        leaf[key] = {"category": category}

                    continue

                leaf = {
                    key: leaf
                }

            action_tree = helpers.mergedicts(action_tree, leaf)

        self.cached_action_tree = action_tree
        return action_tree

    def flatten_action_set(self, actionset):
        out = {}
        for key, action in actionset.items():
            if "category" in action:
                out[key] = "+%s" % action["category"]

            if "action" in action:
                text = action["action"]
                if "description" in action:
                    text = action["description"]

                out[key] = "%s" % text

        return out

    def get_actions_for_keyset(self, keyset=None):
        action_tree = self.generate_action_tree()
        if keyset is None or len(keyset) == 0:
            return self.flatten_action_set(action_tree)

        try:
            tree = action_tree
            for key in keyset:
                if "category" in tree[key]:
                    tree = tree[key]
        except KeyError:
            return None

        return self.flatten_action_set(tree)

    def show_help(self):
        actions = self.get_actions_for_keyset(self.command_chain)
        if actions is None:
            self.end_command_chain()
            return

        self.shortcut_panel.run_command("show_sublimious_shortcuts", {"arr": actions})
        sublime.active_window().run_command("show_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def hide_help(self):
        sublime.active_window().run_command("hide_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def delegate_help_panel(self):
        if not self.settings["show_shortcut_overlay"]:
            return

        if self.help_timeout:
            self.help_timeout.cancel()

        if self.settings["shortcut_overlay_timeout"] == 0:
            self.show_help()
            return

        self.help_timeout = threading.Timer(self.settings["shortcut_overlay_timeout"], self.show_help)
        self.help_timeout.start()

    def start_command_chain(self):
        self.command_chain = []
        self.inChain = True
        self.delegate_help_panel()

    def end_command_chain(self):
        if self.help_timeout:
            self.help_timeout.cancel()

        self.inChain = False

    def add_command(self, key):
        if self.inChain:
            self.hide_help()
            self.command_chain.append(key)

    def try_resolve_chain(self):
        if self.inChain:
            if self.command_chain[-2:] == ['f', 'd'] \
                or self.command_chain[-1] == keys["ESCAPE"] \
                or self.command_chain[-1] == 'q':
                    self.end_command_chain()
                    return True

            tree = self.generate_action_tree()
            for key in self.command_chain:
                if key not in tree:
                    return False

                tree = tree[key]

            # check if we are on the final node
            if "action" in tree:
                sublime.active_window().run_command(tree["action"], tree["args"])
                self.end_command_chain()
                return True

        return False

    def on_window_command(self, window, command_name, args):
        if command_name == "press_key" and args["key"]:
            print(args["key"])
            if args["key"] == keys["SPACE"] and not self.inChain:
                self.start_command_chain()
                return ("noop")

            if self.inChain:
                self.add_command(args["key"])
                if not self.try_resolve_chain():
                    self.delegate_help_panel()

                return ("noop")

            self.last_key = args["key"]
            self.hide_help()

    def on_query_context(self, view, key, *args, **kwargs):
        # If we are in a command chain, we deny certain keybindings
        if key == 'sublimious_chain':
            return (not self.inChain)


def plugin_loaded():
    coll = collector.Collector(os.path.dirname(os.path.realpath(__file__)))
    SpaceListener.shortcut_panel = sublime.active_window().create_output_panel("sublimious_shortcut_panel")
    SpaceListener.collector = coll
    SpaceListener.settings = helpers.mergedicts(SpaceListener.settings, coll.get_collected_config())
