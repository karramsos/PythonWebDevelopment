This is a README file for the SQLite Python tutorial.
The ZIP package contains a PDF file and all the code examples
from the tutorial. The SQL files contain statements that
create tables which are used in the tutorial.

Python is available on most Linux distributions by
default. Windows users can download Python binaries
from http://python.org/download/ webpage. Currently, 
Python 2.x is more widespread than Python 3.x. Therefore,
we use Python 2.x in our tutorial. 

SQLite can be installed easily from the packages of any
Linux distro. For example, on Debian based systems, we use
the following command:

$ sudo apt-get install sqlite3

Precompiled binaries for the Windows OS
can be found at http://sqlite.org/download.html webpage.

In addition to Python and SQLite, we need to have the 
SQLAlchemy and PySide installed on our systems.
Installation of these tools is easy too. 

******************************

Installing SQLAlchemy od Windows

We need to install the Distribute and the Pip packages 
from the http://www.lfd.uci.edu/~gohlke/pythonlibs/ webpage.
Then we istall the SQLAlchemy from the console window (cmd.exe).

C:\Python27\Scripts\pip.exe install SQLAlchemy

******************************


Intalling SQLAlchemy on Debian based Linux

$ sudo pip install SQLAlchemy

******************************


Installing PySide

Windows

Download and install the PySide binaries from the 
http://qt-project.org/wiki/PySide_Binaries_Windows webpage. 

Linux

Installation instructions for different Linux distributions
can be found at http://qt-project.org/wiki/PySide_Binaries_Linux webpage.

******************************

The code examples were tested with the following
versions of libraries:

Windows 7

Python 2.7.5
SQLite 3.7.17
SQLAlchemy 0.8.1
PySide 1.1.2

Windows XP

Python 2.7.0
SQLite 3.6.21
SQLAlchemy 0.8.1
PySide 1.1.2

Ubuntu Linux

Python 2.7.2
SQLite 3.7.7
SQLAlchemy 0.8.1
PySide 1.0.6