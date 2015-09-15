class Layer():
    required_packages = [
        "JavaScriptNext - ES6 Syntax",
        "JsFormat",
        "tern_for_sublime",
        "SublimeLinter-flow",
        "SublimeLinter-jshint",
        "SublimeLinter-contrib-eslint",
        "SublimeLinter-json",
    ]

    keymap = [
    ]

    syntax_definitions = {
        "Javascript": ['.js', 'js'],
        "JSON": ['.jshintrc', '.eslintrc', '.jsbeautifyrc']
    }

    def init(self, config):
        pass
