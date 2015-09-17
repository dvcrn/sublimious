import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import sublime_plugin
import sublime
import threading

from .lib.collector import Collector
from .lib import helpers

keys = {
    "SPACE": "<space>",
    "ESCAPE": "<esc>"
}


class SpaceListener(sublime_plugin.EventListener):
    settings = {
        'keyboard_overlay_timeout': 1
    }

    command_chain = []
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
            args = command.get("args", {})

            leaf = {}
            first = True
            for key in reversed(keys):
                if first:
                    first = False
                    if action:
                        leaf[key] = {"action": action, "args": args}

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
                out[key] = "%s" % action["category"]

            if "action" in action:
                out[key] = "%s" % action["action"]

        return out

    def get_actions_for_keyset(self, keyset=None):
        action_tree = self.generate_action_tree()
        if keyset is None or len(keyset) == 0:
            return self.flatten_action_set(action_tree)

        tree = action_tree
        for key in keyset:
            if "category" in tree[key]:
                tree = tree[key]

        return self.flatten_action_set(tree)

    def show_help(self):
        actions = self.get_actions_for_keyset(self.command_chain)
        self.shortcut_panel.run_command("show_sublimious_shortcuts", {"arr": actions })
        sublime.active_window().run_command("show_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def hide_help(self):
        sublime.active_window().run_command("hide_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def delegate_help_panel(self):
        if self.help_timeout:
            self.help_timeout.cancel()
        self.help_timeout = threading.Timer(self.settings["keyboard_overlay_timeout"], self.show_help)
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
            if self.command_chain[-2:] == ['f', 'd'] or self.command_chain[-1] == keys["ESCAPE"]:
                self.end_command_chain()
                return True

            tree = self.generate_action_tree()
            for key in self.command_chain:
                tree = tree[key]

            # check if we are on the final node
            if "action" in tree:
                sublime.active_window().run_command(tree["action"], tree["args"])
                self.end_command_chain()
                return True

        return False

    def on_window_command(self, window, command_name, args):
        if command_name == "press_key" and args["key"]:
            if args["key"] == keys["SPACE"]:
                self.start_command_chain()
                return ("press_key", {"key": ""})

            if self.inChain:
                self.add_command(args["key"])
                if not self.try_resolve_chain():
                    self.delegate_help_panel()

                return ("press_key", {"key": ""})

        self.hide_help()


def plugin_loaded():
    collector = Collector(os.path.dirname(os.path.realpath(__file__)))
    SpaceListener.shortcut_panel = sublime.active_window().create_output_panel("sublimious_shortcut_panel")
    SpaceListener.collector = collector
    SpaceListener.settings = helpers.mergedicts(SpaceListener.settings, collector.get_collected_config())




