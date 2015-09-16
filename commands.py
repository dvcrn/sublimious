import sublime
import sublime_plugin


class ShowSublimiousShortcutsCommand(sublime_plugin.TextCommand):
    def run(self, edit, arr):
        if len(arr) == 0:
            return;

        self.view.set_read_only(False)
        self.view.erase(edit, sublime.Region(0, self.view.size()))
        s = []
        for key, definition in arr.items():
            s.append("%s -> %-20s" % (key, definition))

        self.view.insert(edit, self.view.size(), 'Key Commands\n\n')
        for i, val in enumerate(s):
            if (i + 1) % 4 == 0:
                self.view.insert(edit, self.view.size(), "%s\n" % val)
                continue

            self.view.insert(edit, self.view.size(), val)

        self.view.settings().set("word_wrap", False)
        self.view.set_read_only(True)
        self.view.show(self.view.size())

class StatusCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.set_read_only(False)
        self.view.insert(edit, self.view.size(), "%s\n" % text)
        self.view.set_read_only(True)
        self.view.show(self.view.size())

