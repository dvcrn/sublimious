class Layer():
    name = "CoffeeScript"

    required_packages = [
        "SublimeREPL",
        "Leiningen",
        "Enhanced Clojure",
        "ClojureDocSearch",
        "Parinfer"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Clojure": ['clj'],
        "ClojureScript": ['cljs']
    }

    def init(self, config):
        pass
