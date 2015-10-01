import threading


class PackageResolver(threading.Thread):
    def __init__(self, package_control, packages, to_remove, callback):
        self.package_control = package_control
        self.packages = packages
        self.to_remove = to_remove
        self.callback = callback
        threading.Thread.__init__(self)

    def run(self):
        for pkg in self.to_remove:
            self.package_control.remove_package(pkg)

        for pkg in self.packages:
            self.package_control.install_package(pkg)

        self.callback()
