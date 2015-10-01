import sys
import os
path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

import sublime  # noqa
import json  # noqa

from .lib.collector import Collector  # noqa
from .lib.io import write_sublimious_file  # noqa
from .lib.package_controller import PackageController  # noqa


class Sublimious():

    def __init__(self):
        self.sublime_dir = os.path.dirname(sublime.packages_path())
        self.packages_dir = os.path.join(self.sublime_dir, 'Packages')
        self.sublimious_packages_dir = os.path.join(self.packages_dir, 'sublimious/')
        self.user_dir = os.path.join(self.packages_dir, 'User')
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.collector = Collector(self.current_path)
        self.status_panel = sublime.active_window().create_output_panel("sublimious_status_panel")

        sublime.active_window().run_command("show_panel", {"panel": "output.sublimious_status_panel", "toggle": False})

        package_controller = PackageController()

        if not self.collector.get_user_config().nuke_everything:
            self.status_panel.run_command("status", {"text": "Sublimious is currently off."})
            self.status_panel.run_command("status", {"text": "Since this might be your first start, I created a ~/.sublimious file"})
            self.status_panel.run_command("status", {"text": "Open that file and change 'nuke_everything' to True to proceed\n"})
            sys.exit()

        self.status_panel.run_command("status", {"text": "Welcome to Sublimious. Just a moment, I'm initializing some things..."})

        # Nuke everything
        if not os.path.isdir(self.sublimious_packages_dir):
            os.mkdir(self.sublimious_packages_dir)

        settings_current = [os.path.join(self.sublimious_packages_dir, f) for f in os.listdir(self.sublimious_packages_dir) if f.endswith(".sublime-settings")]
        settings_user = [os.path.join(self.user_dir, f) for f in os.listdir(self.user_dir) if f.endswith(".sublime-settings")]
        filelist = settings_current + settings_user

        # Delete all settings except Package Control
        for f in filelist:
            if "Package Control" in f:
                continue

            os.remove(f)

        # Second iteration to initialise all layers with config
        collected_config = self.collector.get_collected_config()
        for layer in self.collector.get_layers():
            layer.init(collected_config)

        # Collect all packages
        all_packages = self.collector.collect_key("required_packages") + self.collector.get_user_config().additional_packages
        package_controller.install_packages(all_packages, callback=self.after_install)

    def after_install(self):
        settings_file = os.path.join(self.user_dir, 'Preferences.sublime-settings')

        # Get all keybinding definitions and save to keymapfile
        write_sublimious_file("%s/Default.sublime-keymap" % self.user_dir, json.dumps(self.collector.collect_key("sublime_keymap")))

        # Generate a bunch of syntax files depending on layer config
        syntax_definitions = self.collector.collect_syntax_specific_settings()
        for syntax, value in syntax_definitions.items():
            write_sublimious_file("%s/%s.sublime-settings" % (self.sublimious_packages_dir, syntax), json.dumps(value))

        # Generate package specific settings
        for package, setting in self.collector.get_collected_config()["package_settings"].items():
            write_sublimious_file("%s/%s.sublime-settings" % (self.user_dir, package), json.dumps(setting))

        # Take control over sublime settings file
        write_sublimious_file(settings_file, json.dumps(self.collector.get_collected_config()))

        self.status_panel.run_command("status", {"text": "All done! Enjoy sublimious."})


def plugin_loaded():
    Sublimious()
