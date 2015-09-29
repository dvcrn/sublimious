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

        from package_control.package_manager import PackageManager
        self.package_control = PackageManager()

    def install_package(self, package_name):
        self.package_control.install_package(package_name)

    def install_packages(self, packages, wipe_others=True):
        if wipe_others:
            installed_packages = self.package_control.list_packages()

            for pkg in installed_packages:
                if pkg not in packages:
                    self.package_control.remove_package(pkg)

        for pkg in packages:
            if pkg in installed_packages:
                continue

            self.install_package(pkg)

    def reload(self):
        # We have to delete `Package Control.last-run` to not run into the cache
        last_run_file = os.path.join(self.user_dir, "Package Control.last-run")
        if os.path.isfile(last_run_file):
            os.remove(last_run_file)

        from package_control.package_cleanup import PackageCleanup
        sublime.set_timeout(lambda: PackageCleanup().start(), 2000)
