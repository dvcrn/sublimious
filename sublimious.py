from importlib.machinery import SourceFileLoader
import sublime, sublime_plugin
import os

config_path = "~/.sublimious"
if not os.path.exists(config_path):
    config_path = "%s/%s" % (os.path.dirname(os.path.realpath(__file__)), "templates/.sublimious")

config_file = SourceFileLoader("", config_path).load_module()

print(config_file.layers)
print(config_file.additional_packages)


class Sublimious(sublime_plugin.EventListener):
    def on_load(self, view):
        print(view.fileName(), "just got loaded")

    def on_pre_save(self, view):
        print(view.fileName(), "is about to be saved")

    def onPostSave(self, view):
        print(view.fileName(), "just got saved")

    def onNew(self, view):
        print("new file")

    def onModified(self, view):
        print(view.fileName(), "modified")

    def onActivated(self, view):
        print(view.fileName(), "is now the active view")

    def onClose(self, view):
        print(view.fileName(), "is no more")

    def onClone(self, view):
        print(view.fileName(), "just got cloned")
