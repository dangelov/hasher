import string
import sublime
import sublime_plugin
import hashlib
import urllib

# test%20me%3B%28%29

class Md5Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)

            selected = self.view.substr(s)
            m = hashlib.md5()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)

class Sha1Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)

            selected = self.view.substr(s)
            m = hashlib.sha1()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)

class UrlEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)

            selected = self.view.substr(s)
            txt = urllib.quote(selected)
            self.view.replace(edit, s, txt)

class UrlDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)

            selected = self.view.substr(s)
            txt = urllib.unquote(selected)
            self.view.replace(edit, s, txt)