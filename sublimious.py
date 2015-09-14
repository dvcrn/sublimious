from importlib.machinery import SourceFileLoader
import json
import sublime
import os
import itertools

sublime_dir = os.path.dirname(sublime.packages_path())
packages_dir = os.path.join(sublime_dir, 'Packages')
user_dir = os.path.join(packages_dir, 'User')

sublime_settings_file = os.path.join(user_dir, 'Package Control.sublime-settings')

current_path = os.path.dirname(os.path.realpath(__file__))
config_path = "~/.sublimious"

# Load sublimious config file or template
if not os.path.exists(config_path):
    config_path = "%s/%s" % (current_path, "templates/.sublimious")

config_file = SourceFileLoader("", config_path).load_module()

# Collect all layers
layers = []
for layer in config_file.layers:
    layer_path = "%s/%s" % (current_path, "layers/%s" % layer)
    layer_init_file = "%s/%s.py" % (layer_path, layer)

    layer_class = SourceFileLoader("", layer_init_file).load_module()
    layer_instance = layer_class.Layer()
    layer_instance.init()

    print("%s layer loaded!" % layer)

    layers.append(layer_instance)

# Collect all packages
required_packages = list(map(lambda i: i.required_packages, layers))
required_packages.append(config_file.additional_packages)
all_packages = list(itertools.chain(*required_packages))

# add all packages to sublime settings file
with open(sublime_settings_file, "w") as settings:
    settings.write(json.dumps({'installed_packages': all_packages}))

# Get all keybinding definitions and save to keymapfile
keybindings = list(map(lambda i: i.keymap, layers))
with open("Default.sublime-keymap", "w") as settings:
    settings.write(json.dumps(list(itertools.chain(*keybindings))))

syntax_definitions = {}
for layer in layers:
    syntax_definitions.update(layer.syntax_definitions)

for syntax, value in syntax_definitions.items():
    with open("%s.sublime-settings" % syntax, "w") as syntax_file:
        syntax_file.write(json.dumps({"extensions": value}))
