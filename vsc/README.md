# Visual Studio Code setup for Python

The tips are taken over from [this Youtube video](https://www.youtube.com/watch?v=06I63_p-2A4&list=PLRiZb4DNOVQdTOd1-n2TkU06Dgdzpv4nx&index=5).

Here is the short summary.

## Install plugins and themes

- Install Predawn Theme Kit: open prompt (Ctrl+Shift+P). Search for themes. Download custom theme "Predawn Theme Kit". I did not liked thisone
- Install Python plugin for linting etc. from Microsoft

## Setup adjustments

VSC can be customized in lot of ways to fit your needs. This is done by addition custom user settings. The settings can be viewed as JSON file with paramaters. To setup VSC to show settings as JSON.

```JSON
// show json file insted of ui
  "workbench.settings.editor":"json",
// split default and user settings
  "workbench.settings.useSplitJSON":true,
```

There are plugins that enable you to save and share your VSC settings as Github gist.

### Default python path

We can set default python path in settings.

```bash
# get location of python3 version
which python3
# save it in settings in this case
# "python.pythonPath": "/usr/bin/python3",
```

```JSON
// save custom default path to python3
"python.pythonPath": "/usr/bin/python3",
```

## Virtual environments

It is good practice for larger projects to use local project environments. Using virtual env you ensure the package versions used in the project are locked (similar to package.lock file). In python there are 3 major ways to do this.

- Standard venv package. This is the latest one and it is baked standard into pyhon. It requires python 3.3 or higher. You do not have to install anythin. NOTE! after creating venv you use `python` and `pip` commands even if you normally use `python3` and `pip3` as default commands on your machine to activate python v3. Standard venv package does not support loading various python versions than the standard ones you have on your machine. If you need virtual environement with specific python version (not your default versions) you need to use package `virtualenv` (see point 2). For detailed walk trough see this [instruction video](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

```bash
# list all
pip3 list
# create virtual environment at the current folder
python3 -m venv p36env
# activate p36env - it will show
source p36env/bin/activate
# validate python version
which python
# list packages in selected env
pip list
# install required packages
pip install flask
# create requirements file
pip freeze
# create requirements file from global env
pip3 freeze --local > requirements.txt
# install requirements
pip install -r requirements.txt
# deactivate virtual environment
decativate
```

Note you might need to install wheel package if you get error during installation of other packages: "Failed building wheel for wrapt".

```bash
# solves Failed building wheel for wrapt error at package install
pip install wheel
```

- virtualenv: older package that was quite popular before venv module is introduced. See this [instruction video](https://www.youtube.com/watch?v=N5vscPTWKOk) for more info.

```bash
# install virtualenv
pip3 install virtualenv
# list all global packages
pip3 list
```

### Create requirements file

On an existing project you can extract libraries used in the project to a requirements.txt file.

```bash
# save dependencies in the requirements file
pip3 freeze --local > requirements.txt
# install dependencies
pip3 install -r requirements.txt
```

## PIP with Linux

Python package installer. The default version of python in Linux is 2.7 at the time of writing. Generally we want to use v3 python in our projects. For linux then we do need to use

```bash
# get python version
python3 --version
# get pip3 version
pip3 --version
```

## Formatting and linting

There are plugins for python code formatting and linting. With Linux when working with python3 you might need to install pip and pep8 before you can install autopep8 code formatter.

```bash
# install code formatter
pip3 install autopep8
```

If you want code to be autoformated in save, you need to indicate this in the settings. You can do this by language. As I usually run lot of web development I also have auto formatters and linters enabled per language: html, js (react/vue flavours), css, markdown etc.

For linting after installing python plugin it will have pylint linter installed and enabled. You can also run linter to command pallet.

## Tests

Defining testing tool for Python will add testing icon to toolbar on the left side. The python testing definitions are saved in settings.
