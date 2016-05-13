# String Hasher

Hasher is a small Sublime Text 2 & 3 Plugin that generates hashes from the selected text and some miscellaneous **Unicode aware** string conversions. Currently supported:

* MD5
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512
* NTLM
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

IF you wish to add hasher commands to the context menu, see this [wiki entry](https://github.com/dangelov/hasher/wiki/Context-menu-instructions).

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
- [alphaskade](https://github.com/alphaskade) - SHA256, SHA384, SHA512 and NTLM Hashing
- [komaflash](https://github.com/komaflash) - SHA224, SHA256, SHA384 and SHA512

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
