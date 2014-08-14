"""
piranha.py contains methods for creating MySQL database tables for
various piranha rack types.
"""

import config
import MySQLdb

config.warnings.filterwarnings('ignore', category = MySQLdb.Warning)
"""
T4: type 4
"""
def T4(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    #copy table structure
    sql = "CREATE TABLE %s like TLAPiranhaT4Template" %TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #copy entire table
    sql = "INSERT INTO %s SELECT * FROM TLAPiranhaT4Template"%TLA_dict['TLA_name']
    cursor.execute(sql)
    
    
    #update parameters unique to KnoxT4
    #bloodhound
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Bloodhound PN'], 'bldhound-%')
    cursor.execute(sql)
    
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], '10gsw-%')
    cursor.execute(sql)
    
    #powershelf
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['PowerShelf PN'], 'pwrshelf-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s', col1_C='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'], TLA_dict['Server PN'],\
                                TLA_dict['Server PN'],'compute-%')
    cursor.execute(sql)
    
    #piranha
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['KNOX Chassis PN'],
                                'piranha-%')
    cursor.execute(sql)
    

    #update timestamp
    sql = "UPDATE %s SET TIMESTAMP = '%s'"%(TLA_dict['TLA_name'], config.time.strftime("%Y-%m-%d %H:%M:%S",\
                                                                config.time.localtime(config.time.time())))
    cursor.execute(sql)
    db.commit()

    cursor.close()
    db.close()

"""
T5: type 5
"""
def T5(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    #copy table structure
    sql = "CREATE TABLE %s like TLAPiranhaT5Template" %TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #copy entire table
    sql = "INSERT INTO %s SELECT * FROM TLAPiranhaT5Template"%TLA_dict['TLA_name']
    cursor.execute(sql)
    
    
    #update parameters unique to KnoxT5
    #bloodhound
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Bloodhound PN'], 'bldhound-%')
    cursor.execute(sql)
    
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], '10gsw-%')
    cursor.execute(sql)
    
    #powershelf
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['PowerShelf PN'], 'pwrshelf-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s', col1_C='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'], TLA_dict['Server PN'],\
                                TLA_dict['Server PN'],'compute-%')
    cursor.execute(sql)
    
    #piranha
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['KNOX Chassis PN'],
                                'piranha-%')
    cursor.execute(sql)
    

    #update timestamp
    sql = "UPDATE %s SET TIMESTAMP = '%s'"%(TLA_dict['TLA_name'], config.time.strftime("%Y-%m-%d %H:%M:%S",\
                                                                config.time.localtime(config.time.time())))
    cursor.execute(sql)
    db.commit()

    cursor.close()
    db.close()
