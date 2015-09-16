class Layer():
    name = "Python"

    required_packages = [
        "Djaneiro",
        "Jedi - Python autocompletion",
        "Python 3",
        "SublimeLinter-flake8",
        "AutoPEP8",
        "SublimeREPL",
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Python3": ['.py', 'py']
    }

    def init(self, config):
        pass
