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

You can create virtual env for each project. In fact that is advised approach for larger projects to keep python version locked.
On linux you need to install venv module for python 3

```bash
# install
apt-get install python3-venv
# setup virtual environment for this project with the name venv
python3 -m venv venv
```

After creating venv for the project you need to selected in VSC to be used. At the bottom taskbar python runtimes can be selected. Use the one with the name you specified, in my case the name is venv.

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
