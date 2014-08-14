"""
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont

config.py contains setup variables.
"""

from re import match
import time
import warnings
import cheetah
import coldstorage
import knox
import leopard
import piranha
import windmill

#database setup variables
server_link = '192.168.68.50'
user = None
pw = None
database = 'RCKHYVEDB'

#dictionary mapping rack type to functions
rack_type_script = {
                    'CHEETAH TYPE 3': cheetah.T3,
                    'COLD STORAGE TYPE 7': coldstorage.T7,
                    'KNOX TYPE 4': knox.T4,
                    'KNOX TYPE 5': knox.T5,
                    'LEOPARD TYPE 1': leopard.T1,
                    'LEOPARD TYPE 3': leopard.T3,
                    'LEOPARD TYPE 6': leopard.T6,
                    'PIRANHA TYPE 4': piranha.T4,
                    'PIRANHA TYPE 5': piranha.T5,
                    'WINDMILL TYPE 1 SINGLE': windmill.T1S,
                    'WINDMILL TYPE 1 TRIPLE': windmill.T1T,
                    'WINDMILL TYPE 6 SINGLE': windmill.T6S,
                    'WINDMILL TYPE 6 TRIPLE': windmill.T6T}

