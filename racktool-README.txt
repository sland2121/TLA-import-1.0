/*
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont
*/

To run TLAdb_import.py:

Download:
1. Python 2.7.6 (64 bit)
2. Download MYSQLdb: (http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python)
-search for MYSQLdb, click on link
-download for python 2.7, 64 bit
-place folder in Python27/Lib/site-packages
3. Download xlrd module: (https://pypi.python.org/pypi/xlrd)
-extract 'xlrd' folder and place in Python27/Lib/site-packages 

Run:
1. Run TLAdb_import_tool.py
2. Load the spreadsheet. Ensure spreadsheet is a '.xls'.
3. Choose 'import all' or input specific TLAs to import.

Requirements:
1. Rack template must exist in 192.168.68.50: RCKHYVEDB.
2. Rack type must exist in config.py
3. Racks with components of mixed part #s must be manually entered into db.

