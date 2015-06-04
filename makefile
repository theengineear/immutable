all : convert-readme

convert-readme :
	@echo "Converting markdown readme to ReSTructured text for PyPI using pandoc"
	pandoc --from=markdown --to=rst --output=README.rst README.md
