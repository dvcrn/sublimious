import itertools
import os
from .io import load_python_file

class Collector():
    layers = []
    collected_config = {}
    user_config = {}

    def __init__(self, sublimious_dir):
        print(sublimious_dir)

        config_path = "~/.sublimious"
        if not os.path.exists(config_path):
            config_path = "%s/%s" % (sublimious_dir, "templates/.sublimious")

        config_file = load_python_file(config_path)

        # Collect all layers and layer configurations
        for layer in config_file.layers:
            layer_init_file = "%s/%s/layer.py" % (sublimious_dir, "layers/%s" % layer)
            layer_settings_file = "%s/%s/settings.py" % (sublimious_dir, "layers/%s" % layer)

            layer_init = load_python_file(layer_init_file)
            self.layers.append(layer_init.Layer())

            settings = eval(open(layer_settings_file, 'r').read())
            self.collected_config.update(settings)

        # Load user configuration on top
        if (len(config_file.user_config) > 1):
            self.collected_config.update(config_file["user_config"])

        self.user_config = config_file

    def get_layers(self):
        return self.layers

    def get_collected_config(self):
        return self.collected_config

    def get_user_config(self):
        return self.user_config

    def collect_syntax_specific_settings(self):
        syntax_definitions = {}

        for layer in self.layers:
            if not hasattr(layer, "syntax_definitions"):
                continue

            for syntax, files in layer.syntax_definitions.items():
                if syntax not in syntax_definitions:
                    syntax_definitions[syntax] = {"extensions": []}

                syntax_definitions[syntax]["extensions"] = syntax_definitions[syntax]["extensions"] + files



            if not hasattr(layer, "color_scheme_definitions"):
                continue

            for syntax, color_schemes in layer.color_scheme_definitions.items():
                if syntax not in syntax_definitions:
                    syntax_definitions[syntax] = {"color_scheme": []}

                if "color_scheme" not in syntax_definitions[syntax]:
                    syntax_definitions[syntax]["color_scheme"] = color_schemes

        return syntax_definitions

    def collect_key(self, key):
        collected_list = list(map(lambda i: getattr(i, key), self.layers))
        return list(itertools.chain(*collected_list))
