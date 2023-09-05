#
# CData Python Connector for MySQL 2023
#

The CData Python Connector for MySQL allows you to easily integrate
your Python applications with MySQL data. The supported environments are
each covered by either a whl file or a tar.gz file that is installed to your Python 
distribution with "pip install".

#
# Installing the Appropriate File
#

The setup archive may contain the following folders/files:
- help
- mac (Mac package only)
- unix (Linux package only)
- win (Windows package only)
- license.txt
- readme.txt

To install the Python Connector, open the terminal/command prompt. Depending on the execution
environment, the specific file to use will vary.

After extracting the zip archive, you should then navigate to the appropriate platform
folder, whether "win" for Windows users, "mac" for Mac users, or "unix" for Linux users.

For Windows users, there will be additional subfolders for the python version and bitness.
After selecting the appropriate subfolder, the pertinent whl file should be installed with
the "pip install" command. For example, a 64-bit Python 3.10 distribution on Windows would
require the following command:

pip install cdata_mysql_connector-23.0.8565-cp310-cp310-win_amd64.whl

For Linux or Mac users, there will instead be one a tar.gz file covering the supported
Python versions on that platform. The "pip install" command will be used on that
tar.gz file. For example, a Python 3.10 distribution on Linux will require the following command:

pip install cdata-mysql-connector-23.0.8565-python3.tar.gz

#
# Licensing the connector
#

After the installation, a separate step must be done to activate a license for the connector. Among
the CData assets in the distribution's site packages, there should be an install-license tool that
will activate this license. From the python distribution's site-packages folder, after navigating
to the "cdata/installlic_mysql" folder, simply use a command like the below to
activate the license. Omitting the <key> argument will activate a trial license:

Windows:
./install-license.exe <key>

Linux / Mac:
./install-license.sh <key>

#
# Using the connector
#

After installation and licensing, the module for this Python connector can be imported and used in code,
as in the below example:

import cdata.mysql as mod

#
# Additional Help Documentation
#

The connector comes provided with extensive help documentation which is found in the "help" folder
of the archive. To examine the documentation, open the "help.htm" file in any web browser.
