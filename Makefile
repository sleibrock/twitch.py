install:
	python setup.py install

build:
	python setup.py sdist bdist_wheel
upload:
	twine upload dist/*

