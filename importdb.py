"""
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont

importdb.py provides functions enabling TLA data to be extracted
from spreadsheet and imported into RCKHYVDB tables.
"""

import config
import MySQLdb
import xlrd
import tkMessageBox as tkmb

config.warnings.filterwarnings('ignore', category = MySQLdb.Warning)

"""
extractTLAData:
extract TLA data contained in spreadsheet row
"""
def extractTLAData(TLA_row_num, TLA_sheet): 
    TLA_dict = {}
    last_col = 21
    col_num = 0
    for label in TLA_sheet.row_values(0,0,last_col):
        #handling null cells
        if TLA_sheet.cell(TLA_row_num,col_num).ctype == 0:
            TLA_dict[str(label).strip()] = 0
            
        elif TLA_sheet.cell(TLA_row_num,col_num).ctype == 2:
            TLA_dict[str(label).strip()] = TLA_sheet.cell_value(TLA_row_num, col_num)  
        else:
            TLA_dict[str(label).strip()] = str(TLA_sheet.cell_value(TLA_row_num, col_num)).strip()
        col_num += 1
      
    TLA_dict['TLA_name'] = 'TLA'+ TLA_dict['TLA PN'][0:2] + \
                           TLA_dict['TLA PN'][3:]

    return TLA_dict

"""
importMODELCONFIG: import TLA data into
RCKHYVEDB MODELCONFIG table.
"""
def importMODELCONFIG(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                     config.pw, config.database)
    cursor = db.cursor()
    
    #if TLA exists, delete and perform record update
    sql = "SELECT COUNT(1) FROM MODELCONFIG WHERE pn = '%s'" %TLA_dict['TLA PN']
    if cursor.execute(sql):
        sql = "DELETE FROM MODELCONFIG WHERE pn = '%s'" %TLA_dict['TLA PN']
        cursor.execute(sql)
        db.commit()  
    sql = "SELECT * FROM MODELCONFIG"
    cursor.execute(sql)
    sql = "INSERT INTO MODELCONFIG (pn, description, type, node, sw10g, sw1g, jbod,\
                        pshelf, bldhound, server, slot, stress_in_minutes)\
                        VALUES(%(TLA PN)s,%(DESCRIPTION)s,\
                        %(TYPE)s,%(#Nodes per Tray)s,%(#10G Switch)s,%(#1G Switch)s,%(#JBOD)s,%(#PowerShelves)s,\
                        %(#BloodHound)s,%(#Servers)s,%(#Slots)s,%(#Hrs to test)s*60)"
    cursor.execute(sql,TLA_dict)
    cursor.close()
    db.commit()
    db.close()
    
"""
importTLATable: create TLA table in RCKHYVEDB
and import TLA data.
"""
def importTLATable(TLA_dict):
    db = MySQLdb.connect(config.server_link, config.user, \
                 config.pw, config.database)
    cursor = db.cursor()
    
    #if table already exists, delete to allow update
    sql = "DROP TABLE IF EXISTS %s" %TLA_dict['TLA_name']
    cursor.execute(sql)
    cursor.close()
    
    #create table and import data
    config.rack_type_script[TLA_dict['TYPE']](TLA_dict)
    #print "Created TLA table for '%s'"%TLA_dict['TLA_name']
    db.commit()
    db.close()
        
"""
importTLAtoDB:
import all TLAs in spreadsheet into RCKHYVEDB.
"""
def importTLAtoDB(TLA_workbook):
    font = TLA_workbook.font_list
    TLA_sheet = TLA_workbook.sheet_by_name('TLA - TOP SKUs')
    
    for i in range(1,TLA_sheet.nrows):
        #skip racks with mixed component p/n
        if font[TLA_workbook.xf_list\
                            [TLA_sheet.cell_xf_index(i,0)].font_index].italic == 1:
            mixed_TLAs.append(str(TLA_sheet.cell_value(i,0)))
            continue
        
        #import 
        TLA_row_num = i

        try:
            #pull TLA info from inputted spreadsheet
            TLA_dict = extractTLAData(TLA_row_num, TLA_sheet)
            
            #import into MODELCONFIG table
            importMODELCONFIG(TLA_dict)
            
            #create TLA table and import
            importTLATable(TLA_dict)

            tkmb.showinfo("Successful Update!", \
                      "Database has been updated for '%s'.\n"%TLA_dict['TLA_name'])
            
        except:
            tkmb.showerror("Error", \
                           "Check if rack type '%s' for '%s' exists in config.py.\n\
If notElse try again."%(TLA_dict['TYPE'],TLA_dict['TLA_name']))
        
    if len(mixed_TLAs) > 0:
        tkmb.showerror("Error", \
                           "Update database manually for following TLAs with mixed \
component part #s:\n'%s'"%str(mixed_TLAs).strip('[]').replace("'",""))
        
"""
importTLAtoDB:
import TLAs contained in list input_TLAs into RCKHYVEDB.
"""
def importTLAtoDB(TLA_workbook, input_TLAs):
    font = TLA_workbook.font_list
    TLA_sheet = TLA_workbook.sheet_by_name('TLA - TOP SKUs')

    mixed_TLAs = []
    for i in range(1,TLA_sheet.nrows):
        #skip TLAs not in inputted TLAs
        if TLA_sheet.cell_value(i,0) not in input_TLAs:
            continue
        
        if TLA_sheet.cell_value(i,0) in input_TLAs:
            input_TLAs.remove(TLA_sheet.cell_value(i,0))
            
            #skip racks with mixed component p/n
            if font[TLA_workbook.xf_list\
                                [TLA_sheet.cell_xf_index(i,0)].font_index].italic == 1:
                mixed_TLAs.append(str(TLA_sheet.cell_value(i,0)))
                continue

            #import
            TLA_row_num = i
        
            try: 
                #pull TLA info from inputted spreadsheet
                TLA_dict = extractTLAData(TLA_row_num, TLA_sheet)
                
                #import into MODELCONFIG table
                importMODELCONFIG(TLA_dict)
                
                #create TLA table and import
                importTLATable(TLA_dict)

                tkmb.showinfo("Successful Update!", \
                      "Database has been updated for '%s'.\n"%TLA_dict['TLA_name'])

            except:
                tkmb.showerror("Error", \
                           "Check if rack type '%s' for '%s' exists in config.py.\n\
Else try again."%(TLA_dict['TYPE'],TLA_dict['TLA_name']))
    
    if len(input_TLAs) > 0:
        tkmb.showerror("Error", \
                           "Following TLAs do not exist in spreadsheet:\n'%s'"\
                       %str(input_TLAs).strip('[]').replace("'","")) 
    if len(mixed_TLAs) > 0:
        tkmb.showerror("Error", \
                           "Update database manually for following TLAs with mixed \
component part #s:\n'%s'"%str(mixed_TLAs).strip('[]').replace("'",""))
