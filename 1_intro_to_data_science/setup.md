# Setting Up Your Environment

There are many utilities that may be useful throughout this course to manage your environment. These include:

1. Python - Python is currently on version 3.4
2. [Sublime Text](http://www.sublimetext.com/)
3. git - a version control system to manage code you write
4. brew (Mac only) - a package manager to install software and manage updates
5. cygwin (Windows only) - an alternative command line enviroment to mimic a Unix enviroment
6. brew (Mac only) - a package manager to install software and manage updates

Note: If you have issues with the brew install because of an XCode error, you may need to upgrade XCode or install XCode Developer tools.

## Anaconda Python

### Anaconda

You can install Python with all of the relevant libraries by using the Anaconda installation package.

More detailed instructions are here: http://continuum.io/downloads

### Other Installation Options

If do not want the full Anaconda package, there are other ways to install Python as well.  1) You probably have it by default, but you may want to upgrade it.


If you have brew:
```sh
brew install python
```

### Installing Packages
If you chose not to install Anaconda but want to install some of the packages, the best options are `pip` or `easy_install`.  `easy_install` sometimes requires root permissions, so might be more difficult to use.

```sh
brew install pip
```

Once those are installed you can use them to install Python packages as follows:

```sh
pip install numpy
pip install scipy
pip install scikit.learn
```

### VirtualEnv
If you are using Python actively for other purpose, you may not want to upgrade Python without some safety. Some of the packages we use might require a more modern Python/ Virtual environments allow you to do that (as does Anaconda).

## Installing Homebrew

Brew is a fantastic package manager for Mac that will allow you to easily install packages.
http://mxcl.github.io/homebrew/

To install:

```sh
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

## GitHub
```sh
brew install git
```

Alternatively, you can choose an OS based installation from this guide:  http://git-scm.com/book/en/Getting-Started-Installing-Git
On Windows, there's an installer available here: http://git-scm.com/download/win

