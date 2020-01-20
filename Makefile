SOURCE_DIR = source
BUILD_DIR = build

.PHONY: html github

html:
	@sphinx-build -M html source build -E

github: html
	@cp -r build/html/* docs/
