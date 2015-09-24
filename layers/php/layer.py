class Layer():
    name = "PHP"

    required_packages = [
        "SublimeLinter-php",
        "Phpcs",
        "Laravel Blade Highlighter"
    ]

    sublimious_keymap = []
    sublime_keymap = []

    syntax_definitions = {
        "PHP": ['php'],
        "laravel-blade": ['blade.php', 'blade']
    }

    def init(self, config):
        pass
