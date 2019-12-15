Setup
=====

Linux
-----

Make sure that python3 is installed. Depending on the default python version of
your distribution you might need to install the python package or the python3
package.

For Ubuntu 18.04: `apt-get install python3`

You can check the python version with `-V`. Try `python -V` or `python3 -V`.

Furthermore, we need the python package `ply` that provides a lexer. You can
install it via your package manager or via `pip`.

 * On Ubuntu: `apt-get install python3-ply`

 * Via pip: `pip3 install --user ply`

Mac OS
------

Download and install python3. Recommended way is to use Homebrew as a package
manager for Mac.

 * Install XCode (or XCode Developer Tooling): `xcode-select --install`

 * Install Homebrew: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)`

 * Install Python3: `brew install python3`

 * Install pip: `brew install pip3`

 * After the installer completed open a new terminal and install `ply` with the
   following command: `pip3 install --user ply`

Windows
-------

Download and install python3
(https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe). Make sure to add
python to the PATH when the installer asks.

After the installer completed, open a command line to install ply with the
following command: `pip install --user ply`


Execution
=========

To run the compiler, open a command line and navigate to the parent directory
of the directory containing this file. You can pass a programm to the compiler
using the `echo` command and the pipe operaor:

```
echo "(2+3)*5" | python -m <package>.main
```

Thereby, `<package>` is a placeholder for the directory that contains the main
module that you want to execute. In the first tutorial, this will be
`ll_parser.main`. For instance:

```
cd <path/to/this/directory>
cd ..
echo "3*9" | python -m ll_parser.main
```

Depending on your distribution, you might need to run `python3` instead of
`python`.
