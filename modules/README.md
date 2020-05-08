# Modules in Python

An module in Python is simple a file with number of methods and its variables.

## Import whole module

The module file can be imported into another file using import keyword. With import we have access to all methods and top level (module) variables.

```python
# import and assign alias (short name)
import module as mm

mm.method(params)

```

## Import specific functions from module/file

We can also import specific function or top level variables from module/file using the approach below. We can also use aliasing for method names

```python
# import specific function from module
from module import myFunction as Fn, TopLevelVariable

myFunction(params)

print (TopLevelVariable)
```

Not preffered approach is to use \* to import all methods. This approach makes it more difficult to trace the origin of a methods.

```python
# avoid this
from module1 import *
from module2 import *
# where does this methods comes from?
myFunction(params)
```

## How the module file is found?

When import statements is used in py file, Python looks at multple locations to find the file/module with the specified name. To see what paths are included use sys module and print path. The first path is the path of the project file the python is runned. If the file is not found there we proceed to next definition.

```python
import sys
# show me included paths
print(sys.path)

# example output from one of my machines
sys.path = [
  # this is current directory
  '/home/dusan/iis/demo/python/concepts/modules',
  # python PATH variable
  '/usr/lib/python36.zip',
  '/usr/lib/python3.6',
  '/usr/lib/python3.6/lib-dynload',
  '/usr/local/lib/python3.6/dist-packages',
  '/usr/lib/python3/dist-packages',
  '/usr/lib/python3.6/dist-packages'
]
```

### Importing module from other directories (not in path)

If you want to import module that is not in current project directory and NOT in one of default paths defined, you can append new path to sys.path. For example

```python
# import sys to add path
import sys
# add module path to sys path
sys.path.append("/LocationToMyModule/")
# import module
import ModuleFile as module
```

However, IT IS BETTER to add path to environment variable. Adding env variables is different per OS.

Linux and Mac OS: edit yout local bash profile file ~/.bash_profile

`/.bashrc and ~/.bash_profile are scripts that might be executed when bash is invoked. The ~/.bashrc file gets executed when you run bash using an interactive shell that is not a login shell.`

So basically bashrc is run when you run an interactive shell that you're not logged in for and bash_profile is executed when you are a logged in user.
