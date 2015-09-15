import sys
import sublime
import sublime_plugin
import os
import itertools
import json


class StatusCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.set_read_only(False)
        self.view.insert(edit, self.view.size(), "%s\n" % text)
        self.view.set_read_only(True)
        self.view.show(self.view.size())


def plugin_loaded():
    sublime_dir = os.path.dirname(sublime.packages_path())
    packages_dir = os.path.join(sublime_dir, 'Packages')
    user_dir = os.path.join(packages_dir, 'User')
    status_panel = sublime.active_window().create_output_panel("sublimious_status_panel")
    sublime.active_window().run_command("show_panel", {"panel": "output.sublimious_status_panel", "toggle": False})

    status_panel.run_command("status", {"text": "Welcome to Sublimious."})

    pcontrol_settings = os.path.join(user_dir, 'Package Control.sublime-settings')
    settings_file = os.path.join(user_dir, 'Preferences.sublime-settings')

    current_path = os.path.dirname(os.path.realpath(__file__))
    config_path = "~/.sublimious"


    # Append the dir to path, so that loading stuff works
    sys.path.append(current_path)
    from lib.io import load_python_file, write_sublimious_file
    from lib import collector

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
        status_panel.run_command("status", {"text": "'%s' layer loaded..." % layer.name})

    # Collect all packages
    status_panel.run_command("status", {"text": "Collecting all packages..."})
    all_packages = collector.collect_key(layers, "required_packages") + config_file.additional_packages
    write_sublimious_file(pcontrol_settings, json.dumps({'installed_packages': all_packages}))

    # Get all keybinding definitions and save to keymapfile
    status_panel.run_command("status", {"text": "Building keymap..."})
    write_sublimious_file("%s/Default.sublime-keymap" % current_path, json.dumps(collector.collect_key(layers, "keymap")))

    # Generate a bunch of syntax files depending on layer config
    syntax_definitions = collector.collect_syntax_specific_settings(layers)
    for syntax, value in syntax_definitions.items():
        write_sublimious_file("%s/%s.sublime-settings" % (current_path, syntax), json.dumps(value))
        status_panel.run_command("status", {"text": "Collected %s syntax definition..." % syntax})

    # Take control over sublime settings file
    status_panel.run_command("status", {"text": "Taking control over Preferences.sublime-settings..."})
    write_sublimious_file(settings_file, json.dumps(default_configuration))

    status_panel.run_command("status", {"text": "ALL DONE!"})
    status_panel.run_command("status", {"text": "(this window will self close in 5s)"})

    sublime.set_timeout(lambda: sublime.active_window().run_command("hide_panel", {"panel": "output.sublimious_status_panel", "toggle": False}), 5000)
