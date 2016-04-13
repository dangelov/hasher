# String Hasher

Hasher is a small Sublime Text 2 & 3 Plugin that generates hashes from the selected text and some miscellaneous **Unicode aware** string conversions. Currently supported:

* MD5
* SHA1
* Base64 Encode
* Base64 Decode
* URI Component Encode
* URI Component Decode
* Entity Encode
* Entity Decode
* Unicode Escape
* Unicode Unescape

## Key bindings

Use _Cmd + Shift + P_ on Mac or _Ctrl + Shift + P_ on Windows and type the command you need. Type _hasher_ to see available commands. More to come.

## Hasher commands in the Context Menu

IF you wish to add hasher commands to the context menu, you may add the following to the end of your User/Context.sublime-menu

```
[
	{ "caption": "-" },
	{
		"caption": "Hasher",
		"children":
		[
			{
				"caption": "MD5",
				"command": "md5",
				"args": {}
			},
			{
				"caption": "SHA1",
				"command": "sha1",
				"args": {}
			},
			{
				"caption": "Base64 Encode",
				"command": "base64_encode",
				"args": {}
			},
			{
				"caption": "Base64 Decode",
				"command": "base64_decode",
				"args": {}
			},
			{
				"caption": "URI Component Encode",
				"command": "uri_component_encode",
				"args": {}
			},
			{
				"caption": "URI Component Decode",
				"command": "uri_component_decode",
				"args": {}
			},
			{
				"caption": "Entity Encode",
				"command": "entity_encode",
				"args": {}
			},
			{
				"caption": "Entity Decode",
				"command": "entity_decode",
				"args": {}
			},
			{
				"caption": "Unicode Escape",
				"command": "unicode_escape",
				"args": {}
			},
			{
				"caption": "Unicode Unescape",
				"command": "unicode_unescape",
				"args": {}
			},
			{
				"caption": "Insert UNIX Timestamp",
				"command": "current_unix_timestamp",
				"args": {}
			}
		]
	}
]
```

## How to install
#### [Package Control](https://github.com/wbond/sublime_package_control)
Just look for _Hasher_ and install.

#### Git Clone
Clone this repository in to the Sublime Text 2 or 3 "Packages" directory, which is located where ever the
"Preferences" -> "Browse Packages" option in Sublime Text takes you.

## Thanks to
- [titoBouzot](https://github.com/titoBouzout) - ST3 compatibility, fixes & additions
- [earshinov](https://github.com/earshinov) - base64 fixes
- [alimony](https://github.com/alimony) - Fixes for HTML Entities + enabled support for both ST2 & 3 in a single package
- [ohaucke](https://github.com/ohaucke) - Context menu for the included commands

## License
Copyright (C) 2012-2013 Dino Angelov & Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
