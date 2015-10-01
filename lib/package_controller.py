import sys
import os

from .package_resolver import PackageResolver

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

        from package_control.package_manager import PackageManager
        self.package_control = PackageManager()

    def install_packages(self, packages, callback=lambda: True, wipe_others=True):
        if wipe_others:
            installed_packages = self.package_control.list_packages()

            to_remove = []
            for pkg in installed_packages:
                if pkg not in packages:
                    to_remove.append(pkg)

        to_install = []
        for pkg in packages:
            if pkg in installed_packages:
                continue
            to_install.append(pkg)

        PackageResolver(self.package_control, to_install, to_remove, callback).start()

    def reload(self):
        # We have to delete `Package Control.last-run` to not run into the cache
        last_run_file = os.path.join(self.user_dir, "Package Control.last-run")
        if os.path.isfile(last_run_file):
            os.remove(last_run_file)

        from package_control.package_cleanup import PackageCleanup
        sublime.set_timeout(lambda: PackageCleanup().start(), 2000)
