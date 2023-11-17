DIST_ARCHIVE = dist/sublime-tagref.sublime-package

default: install
.PHONY: default

install: bundle
	cp "${DIST_ARCHIVE}" ~/.config/sublime-text/Installed\ Packages
.PHONY: install

bundle:
	rm -f "${DIST_ARCHIVE}"
	./bin/bundle.sh "${DIST_ARCHIVE}"
.PHONY: bundle
