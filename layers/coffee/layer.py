class Layer():
    name = "CoffeeScript"

    required_packages = [
        "SublimeREPL",
        "Better CoffeeScript",
        "CoffeeCompile",
        "SublimeLinter-coffeelint"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "CoffeeScript": ['coffee']
    }

    def init(self, config):
        pass
