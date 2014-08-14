"""
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont

windmill.py contains methods for creating MySQL database tables for
various windmill rack types.
"""

import config
import MySQLdb

config.warnings.filterwarnings('ignore', category = MySQLdb.Warning)
"""
T1S: type 1 single
"""
def T1S(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    
    #copy table structure
    sql = "CREATE TABLE %s like TLAWindmillT1STemplate" %TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #copy entire table
    sql = "INSERT INTO %s SELECT * FROM TLAWindmillT1STemplate"%TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #update parameters unique to WMT1S
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], '10gsw-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s'\
        WHERE col1_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                TLA_dict['Server PN'],'01-001089')
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
T1T: type 1 Triple
"""
def T1T(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    #copy table structure
    sql = "CREATE TABLE %s like TLAWindmillT1TTemplate" %TLA_dict['TLA_name']
    cursor.execute(sql)
    #copy entire table
    sql = """INSERT INTO %s SELECT * FROM TLAWindmillT1TTemplate""" %TLA_dict['TLA_name']
    cursor.execute(sql)
    #update parameters unique to WMT1T
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s', col2_A = '%s', col3_A = '%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], \
                                TLA_dict['10G Switch PN'], TLA_dict['10G Switch PN'],\
                                '10gsw-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s'\
        WHERE col1_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
    cursor.execute(sql)

    sql = "UPDATE %s SET col2_A='%s', col2_B = '%s'\
        WHERE col2_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
    cursor.execute(sql)

    sql = "UPDATE %s SET col3_A='%s', col3_B = '%s'\
        WHERE col3_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
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
T6S: type 6 Single
"""
def T6S(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    #copy table structure
    sql = "CREATE TABLE %s like TLAWindmillT6STemplate" %TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #copy entire table
    sql = "INSERT INTO %s SELECT * FROM TLAWindmillT6STemplate"%TLA_dict['TLA_name']
    cursor.execute(sql)
    
    #update parameters unique to WMT1S
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], '10gsw-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s'\
        WHERE col1_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                TLA_dict['Server PN'],'01-000991')
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
T6T: type 6 Triple
"""
def T6T(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    #copy table structure
    sql = "CREATE TABLE %s like TLAWindmillT6TTemplate" %TLA_dict['TLA_name']
    cursor.execute(sql)
    #copy entire table
    sql = """INSERT INTO %s SELECT * FROM TLAWindmillT6TTemplate""" %TLA_dict['TLA_name']
    cursor.execute(sql)
    #update parameters unique to WMT1T
    #10G Switch
    sql = "UPDATE %s SET col1_A='%s', col2_A = '%s', col3_A = '%s'\
        WHERE desc1 LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['10G Switch PN'], \
                                TLA_dict['10G Switch PN'], TLA_dict['10G Switch PN'],\
                                '10gsw-%')
    cursor.execute(sql)
    
    #compute
    sql = "UPDATE %s SET col1_A='%s', col1_B = '%s'\
        WHERE col1_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
    cursor.execute(sql)

    sql = "UPDATE %s SET col2_A='%s', col2_B = '%s'\
        WHERE col2_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
    cursor.execute(sql)

    sql = "UPDATE %s SET col3_A='%s', col3_B = '%s'\
        WHERE col3_A LIKE '%s'"%(TLA_dict['TLA_name'], TLA_dict['Server PN'],\
                                 TLA_dict['Server PN'],'01-000969')
    cursor.execute(sql)
    
    #update timestamp
    sql = "UPDATE %s SET TIMESTAMP = '%s'"%(TLA_dict['TLA_name'], config.time.strftime("%Y-%m-%d %H:%M:%S",\
                                                                config.time.localtime(config.time.time())))
    cursor.execute(sql)
    db.commit()
    
    #final database commit
    cursor.close()
    db.close()
       



