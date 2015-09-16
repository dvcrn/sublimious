import sublime_plugin
import sublime
import threading

keys = {
    "SPACE": "<space>",
    "ESCAPE": "<esc>"
}


class SpaceListener(sublime_plugin.EventListener):
    command_chain = []
    inChain = False
    shortcut_panel = None
    help_timeout = None

    def show_help(self):
        self.shortcut_panel.run_command("show_sublimious_shortcuts", {"arr":
            {
            "p": "project",
            "b": "buffer",
            "f": "file",
            "w": "window",
            "a": "actions",
            "g": "git",
            "a": "git",
            "c": "create",
            "s": "select",
            "i": "insert",
            "m": "moo",
            "n": "new",
            "v": "visual",
            }})

        sublime.active_window().run_command("show_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def hide_help(self):
        sublime.active_window().run_command("hide_panel", {"panel": "output.sublimious_shortcut_panel", "toggle": False})

    def delegate_help_panel(self):
        if self.help_timeout:
            self.help_timeout.cancel()
        self.help_timeout = threading.Timer(1.0, self.show_help)
        self.help_timeout.start()

    def start_command_chain(self):
        self.command_chain = []
        self.inChain = True
        self.delegate_help_panel()

    def end_command_chain(self):
        if self.help_timeout:
            self.help_timeout.cancel()

        self.hide_help()
        self.inChain = False

    def add_command(self, key):
        if self.inChain:
            self.hide_help()
            self.command_chain.append(key)
            self.delegate_help_panel()

    def try_resolve_chain(self):
        if self.inChain:
            if self.command_chain[-2:] == ['f', 'd'] or self.command_chain[-1] == keys["ESCAPE"]:
              self.end_command_chain()

    def on_window_command(self, window, command_name, args):
        if command_name == "press_key" and args["key"]:
            if args["key"] == keys["SPACE"]:
                self.start_command_chain()
                return ("press_key", {"key": ""})

            if self.inChain:
                self.add_command(args["key"])
                self.try_resolve_chain()
                return ("press_key", {"key": ""})

def plugin_loaded():
    SpaceListener.shortcut_panel = sublime.active_window().create_output_panel("sublimious_shortcut_panel")
