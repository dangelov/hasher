import sublime_plugin
import binascii
import hashlib
try:
    from urllib import quote as urlquote
    from urllib import unquote as urlunquote
except ImportError:
    from urllib.parse import quote as urlquote
    from urllib.parse import unquote as urlunquote
import time
import base64
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser
try:
    from htmlentitydefs import codepoint2name as cp2n
except ImportError:
    from html.entities import codepoint2name as cp2n


class Md5Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.md5()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class Sha1Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.sha1()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class Sha224Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.sha224()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class Sha256Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.sha256()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class Sha384Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.sha384()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class Sha512Command(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            m = hashlib.sha512()
            m.update(selected)
            txt = m.hexdigest()
            self.view.replace(edit, s, txt)


class NtlmCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = str(self.view.substr(s))
            m = hashlib.new('md4', selected.encode('utf-16le')).digest()
            if(type(m) is str):
                txt = str(binascii.hexlify(m)).upper()
            elif(type(m) is bytes):
                txt = str(binascii.hexlify(m)).split('\'')[1].upper()
            else:
                txt = s
            self.view.replace(edit, s, txt)


class Base64EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s).encode('utf-8')
            txt = base64.b64encode(selected).decode('utf-8')
            self.view.replace(edit, s, txt)


class Base64DecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)

            # pad to 4 characters
            if len(selected) % 4 != 0:
                selected += "=" * (4 - len(selected) % 4)

            txt = base64.b64decode(selected).decode('utf8')
            self.view.replace(edit, s, txt)


class UriComponentEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)
            txt = urlquote(selected.encode('utf8'), '')
            self.view.replace(edit, s, txt)


class UriComponentDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)
            try:
                txt = urlunquote(selected.encode('utf8')).decode('utf8')
            except TypeError:
                txt = urlunquote(selected)
            self.view.replace(edit, s, txt)


class EntityEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            buf = []
            for pt in range(s.begin(), s.end()):
                ch = self.view.substr(pt)
                ch_ord = ord(ch)
                try:
                    ch = '&%s;' % cp2n[ch_ord]
                except:
                    pass
                buf.append(ch)
            self.view.replace(edit, s, ''.join(buf))


class EntityDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)
            parser = HTMLParser()
            selected = parser.unescape(selected)
            self.view.replace(edit, s, selected)


class UnicodeEscapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)
            self.view.replace(edit, s, selected.encode('ascii', 'backslashreplace').decode('utf-8'))

class UnicodeUnescapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            if s.empty():
                s = self.view.word(s)
            selected = self.view.substr(s)
            self.view.replace(edit, s, bytes(selected, 'utf8').decode('unicode_escape'))

class CurrentUnixTimestamp(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            txt = time.asctime(time.gmtime())
            txt = time.ctime()
            txt = "%.0f" % round(time.time(), 3)
            self.view.replace(edit, s, txt)
