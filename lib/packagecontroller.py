import sys
import os

import sublime


class PackageController:
    user_dir = None

    def __init__(self):
        sublime_dir = os.path.dirname(sublime.packages_path())
        installed_packages_dir = os.path.join(sublime_dir, 'Installed Packages')
        packages_dir = os.path.join(sublime_dir, 'Packages')

        self.user_dir = os.path.join(packages_dir, 'User')

        package_control = os.path.join(installed_packages_dir, "Package Control.sublime-package")
        sys.path.append(package_control)

    def reload(self):
        # We have to delete `Package Control.last-run` to not run into the cache
        last_run_file = os.path.join(self.user_dir, "Package Control.last-run")
        if os.path.isfile(last_run_file):
            os.remove(last_run_file)

        from package_control.package_cleanup import PackageCleanup
        sublime.set_timeout(lambda: PackageCleanup().start(), 2000)
