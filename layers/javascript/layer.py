class Layer():
    name = "Javascript"

    required_packages = [
        "Babel",
        "JsFormat",
        "tern_for_sublime",
        "SublimeLinter-flow",
        "SublimeLinter-jshint",
        "SublimeLinter-contrib-eslint",
        "SublimeLinter-json"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Javascript": ['js'],
        "JSON": ['.jshintrc', '.eslintrc', '.jsbeautifyrc']
    }

    def init(self, config):
        if "use_es6" in config:
            if config["use_es6"] == True:
                self.syntax_definitions["JavaScript (Babel)"] = ["js", "jsx"]
                del self.syntax_definitions["Javascript"]
