class Layer():
    name = "Elixir"

    required_packages = [
        "Elixir",
        "ElixirSublime"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Elixir": ['exs', 'ex']
    }

    def init(self, config):
        pass
