import sublime_plugin
import hashlib
import urllib
import time
import base64
import re

# test

class Md5Command(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s).encode('utf8')
			m = hashlib.md5()
			m.update(selected)
			txt = m.hexdigest()
			self.view.replace(edit, s, txt)

class Sha1Command(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s).encode('utf8')
			m = hashlib.sha1()
			m.update(selected)
			txt = m.hexdigest()
			self.view.replace(edit, s, txt)

class Base64EncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s).encode('utf8')
			txt = base64.b64encode(selected)
			self.view.replace(edit, s, txt)

class Base64DecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = base64.b64decode(selected).decode('utf8')
			self.view.replace(edit, s, txt)

class UriComponentEncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = urllib.quote(selected.encode('utf8'), '')
			self.view.replace(edit, s, txt)

class UriComponentDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = urllib.unquote(selected.encode('utf8'))
			txt = unicode(txt.decode('utf8'));
			self.view.replace(edit, s, txt);

class EntityEncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		from htmlentitydefs import codepoint2name as cp2n
		for s in self.view.sel():
			if s.empty():
							s = self.view.word(s)
			buf = []
			for pt in xrange(s.begin(), s.end()):
				ch = self.view.substr(pt)
				ch_ord = ord(ch)
				try:
					ch = '&%s;' % cp2n[ch_ord]
				except:
					pass
				buf.append(ch)
			self.view.replace(edit, s, ''.join(buf));

class EntityDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = unicode(self.view.substr(s))
			import HTMLParser
			HTMLParser = HTMLParser.HTMLParser()
			selected = HTMLParser.unescape(selected)
			self.view.replace(edit, s, selected);

class CurrentUnixTimestamp(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():

			txt = time.asctime(time.gmtime())
			txt = time.ctime()
			txt = "%.0f" % round(time.time(), 3)
			self.view.replace(edit, s, txt)