install: uninstall
	pip3 install --upgrade git+https://github.com/fxl0206/mkdocs-includex.git

tests:
	cd mkdocs_includex && python plugin.py

uninstall:
	pip3 uninstall mkdocs-includex