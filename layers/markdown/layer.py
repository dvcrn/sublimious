class Layer():
    name = "Markdown"

    required_packages = [
        "MarkdownEditing",
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "Markdown": ['md', 'mdown']
    }

    color_scheme_definitions = {
        "Markdown": 'Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme',
    }

    def init(self, config):
        pass
