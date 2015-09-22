class Layer():
    name = "Python"

    required_packages = [
        "Djaneiro",
        "Anaconda",
        "Python 3",
        "SublimeLinter-flake8",
        "AutoPEP8",
        "SublimeREPL",
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Python": ['py'],
        "Python3": [".sublimious"]
    }

    def init(self, config):
        pass
