import sys
import sublime
import os
import itertools
import json


def plugin_loaded():
    sublime_dir = os.path.dirname(sublime.packages_path())
    packages_dir = os.path.join(sublime_dir, 'Packages')
    user_dir = os.path.join(packages_dir, 'User')

    pcontrol_settings = os.path.join(user_dir, 'Package Control.sublime-settings')
    settings_file = os.path.join(user_dir, 'Preferences.sublime-settings')

    current_path = os.path.dirname(os.path.realpath(__file__))
    config_path = "~/.sublimious"

    # Append the dir to path, so that loading stuff works
    sys.path.append(current_path)
    from lib.io import load_python_file, write_sublimious_file

    # Load sublimious config file or template
    if not os.path.exists(config_path):
        config_path = "%s/%s" % (current_path, "templates/.sublimious")
    config_file = load_python_file(config_path)

    # Collect all layers and layer configurations
    layers = []
    default_configuration = {}
    for layer in config_file.layers:
        layer_init_file = "%s/%s/layer.py" % (current_path, "layers/%s" % layer)
        layer_settings_file = "%s/%s/settings.py" % (current_path, "layers/%s" % layer)

        layer_init = load_python_file(layer_init_file)
        layers.append(layer_init.Layer())

        settings = eval(open(layer_settings_file, 'r').read())
        default_configuration.update(settings)

    # Load user configuration on top
    if (len(config_file.user_config) > 1):
        default_configuration.update(config_file["user_config"])

    # Second iteration to initialise all layers with config
    for layer in layers:
        layer.init(default_configuration)
        print("%s layer loaded!" % layer)

    # Collect all packages
    required_packages = list(map(lambda i: i.required_packages, layers))
    required_packages.append(config_file.additional_packages)
    all_packages = list(itertools.chain(*required_packages))

    # add all packages to sublime settings file
    write_sublimious_file(pcontrol_settings, json.dumps({'installed_packages': all_packages}))

    # Get all keybinding definitions and save to keymapfile
    keybindings = list(map(lambda i: i.keymap, layers))
    write_sublimious_file("Default.sublime-keymap", json.dumps(list(itertools.chain(*keybindings))))

    # Generate a bunch of syntax files depending on layer config
    syntax_definitions = {}
    for layer in layers:
        for syntax, files in layer.syntax_definitions.items():
            if syntax not in syntax_definitions:
                syntax_definitions[syntax] = []

            syntax_definitions[syntax] = syntax_definitions[syntax] + files

    for syntax, value in syntax_definitions.items():
        write_sublimious_file("%s.sublime-settings" % (syntax), json.dumps({"extensions": value}))

    # Take control over sublime settings file
    write_sublimious_file(settings_file, json.dumps(default_configuration))
