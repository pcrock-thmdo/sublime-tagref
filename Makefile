default:
	echo "no default target... yet."
.PHONY: default

install:
	ln --symbolic "$$PWD" ~/.config/sublime-text/Packages/sublime_tagref
.PHONY: install
