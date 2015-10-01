import os
import sublime
import sublime_plugin


class OpenSublimiousConfigCommand(sublime_plugin.WindowCommand):
    def run(self, *args, **kw):
        print("Opening .sublimious")
        config_path = os.path.expanduser("~/.sublimious")
        if os.path.exists(config_path):
            sublime.active_window().open_file(config_path)
