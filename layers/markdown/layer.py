class Layer():
    required_packages = [
        "MarkdownEditing",
    ]

    keymap = [
    ]

    syntax_definitions = {
        "Markdown": ['md', 'mdown']
    }

    color_scheme_definitions = {
        "Markdown": 'Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme',
    }

    def init(self, config):
        pass
