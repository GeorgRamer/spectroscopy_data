help:
	@echo "clean"
	@echo "dist - package"
	@echo "deploy - upload to PyPI and github"


dist: README LICENSE spectroscopy_blog/*.py
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf dist/

deploy: dist
	git push -u origin master
	twine upload dist/*
