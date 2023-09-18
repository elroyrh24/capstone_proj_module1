run:
	./dist/capstone_proj_module1

install:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

build:
	./venv/bin/python setup.py build bdist_wheel
	./venv/bin/pyinstaller src/__main__.py -F --name capstone_proj_module1 \
	 --add-data 'data/data.csv:data' \
	 --add-data 'src/employeefunctions.py:.' \
	 --hiddenimport 'pyinputplus' \
	 --hiddenimport 'tabulate' 

clean:
	rm -rf build
	rm -rf dist
	rm -rf capstone_proj_module1.egg-info
	rm -rf capstone_proj_module1.spec
	rm -rf venv
