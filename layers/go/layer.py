class Layer():
    name = "Go"

    required_packages = [
        "GoSublime",
        "SublimeLinter-contrib-golint",
        "SublimeLinter-contrib-govet",
        "SublimeLinter-contrib-gotype"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "GoSublime-Go": ['go']
    }

    def init(self, config):
        pass
