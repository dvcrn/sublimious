import sublime


def show_console():
    sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": False})


def hide_console():
    sublime.active_window().run_command("hide_panel", {"panel": "console", "toggle": False})
