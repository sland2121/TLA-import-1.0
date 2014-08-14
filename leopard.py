"""
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont

leopard.py contains methods for creating MySQL database tables for
various leopard rack types.
"""

import config
import MySQLdb

config.warnings.filterwarnings('ignore', category = MySQLdb.Warning)
"""
T1: type 1
"""
def T1(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    
    #copy table structure
    sql = "CREATE TABLE %s like TLALeopardT1T6Template" %TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #copy entire table
    sql = "INSERT INTO %s SELECT * FROM TLALeopardT1T6Template"%TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #update parameters unique to WMT1S
    #bloodhound
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Bloodhound PN'], 'bldhound-%')
    cursor.execute(sql)
    
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], '10gsw-%')
    cursor.execute(sql)

    #powershelves
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['PowerShelf PN'], 'pwrshelf-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE col1_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                '01-000092')
    cursor.execute(sql)

    sql = "UPDATE %s SET col1_B='%s'\
        WHERE col1_B LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                '01-000092')
    cursor.execute(sql)

    sql = "UPDATE %s SET col1_C='%s'\
        WHERE col1_C LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                '01-000092')
    cursor.execute(sql)

    #update timestamp
    sql = "UPDATE %s SET TIMESTAMP = '%s'"%(TLA_dict['TLA_name'], config.time.strftime("%Y-%m-%d %H:%M:%S",\
                                                                config.time.localtime(config.time.time())))
    cursor.execute(sql)
    db.commit()
    
    #final database commit
    cursor.close()
    db.close()

"""
T3: type 3
"""
def T3(TLA_dict):
    pass

"""
T6: type 6
"""
def T6(TLA_dict):
    T1(TLA_dict)
