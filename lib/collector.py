import itertools
import os
import shutil

from .io import load_python_file
from .helpers import mergedicts

import zipfile


class Collector():
    layers = []
    collected_config = {}
    user_config = {}
    is_zip = False
    zip_file = None

    def __init__(self, sublimious_dir, user_dir=None):
        self.layers = []
        self.commands = []
        self.collected_config = {}
        self.user_config = {}
        self.is_zip = False
        self.zip_file = None

        if "sublime-package" in sublimious_dir:
            self.is_zip = True
            self.zip_file = zipfile.ZipFile(sublimious_dir)

        config_path = os.path.expanduser("~/.sublimious")
        if not os.path.exists(config_path):
            if self.is_zip:
                templ = self.zip_file.open("templates/.sublimious")
                target = open(config_path, "wb")
                shutil.copyfileobj(templ, target)
                target.close()
            else:
                template_path = "%s/%s" % (sublimious_dir, "templates/.sublimious")
                shutil.copyfile(template_path, config_path)

            print("[sublimious] no config found. Copied template.")

        config_file = load_python_file(config_path)

        # Collect all layers and layer configurations
        for layer in config_file.layers:

            try:
                if self.is_zip:
                    layer_init = __import__("layers.%s.layer" % layer, globals(), locals(), ['Layer'])
                else:
                    layer_init_file = "%s/%s/layer.py" % (sublimious_dir, "layers/%s" % layer)
                    layer_init = load_python_file(layer_init_file)
            except ImportError:
                print("[sublimious] tried to load layer '%s' but couldn't import it. Does it exist?" % layer)
                continue

            self.layers.append(layer_init.Layer())
            self.commands.append("layers.%s.commands" % layer)

            if self.is_zip:
                settings = eval(self.zip_file.read("layers/%s/settings.py" % layer))
            else:
                layer_settings_file = "%s/%s/settings.py" % (sublimious_dir, "layers/%s" % layer)
                settings = eval(open(layer_settings_file, 'r').read())

            self.collected_config = mergedicts(self.collected_config, settings)

        # Load user configuration on top
        if (len(config_file.user_config) > 0):
            self.collected_config = mergedicts(self.collected_config, config_file.user_config)

        self.user_config = config_file

    def get_layers(self):
        return self.layers

    def get_commands(self):
        return self.commands

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

                syntax_definitions[syntax]["extensions"] = list(set(syntax_definitions[syntax]["extensions"] + files))

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
