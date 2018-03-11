help:
	@echo "clean"
	@echo "dist - package"
	@echo "deploy - upload to PyPI and github"


clean:
	rm -rf dist/

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel


deploy: dist
	git push -u origin master
	twine upload dist/*
