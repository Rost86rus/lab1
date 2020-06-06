import sys
import os.path
from peewee import *
import peewee
import datetime
import random as rand

name_database = 'database.db'

db = SqliteDatabase(name_database)
    
class CLIENTS(Model):
    
    ID = PrimaryKeyField()
    NAME = CharField()
    CITY = CharField()
    ADDRESS = CharField()
    
    class Meta:
        db_table = 'clients'
        order_by = ('ID',)
        database = db
    
                
class ORDERS(Model):
    
    ID = PrimaryKeyField()
    CLIENT = ForeignKeyField(CLIENTS,backref='client')
    DATE = DateTimeField(default=datetime.datetime.today())
    AMOUNT = IntegerField()
    DESCRIPTION = CharField()
    
    class Meta:
        db_table = 'orders'
        order_by = ('ID',)
        database = db
        

if __name__ == '__main__':

    if sys.argv[1] == 'init':
        
        if os.path.exists(name_database):
            os.remove(name_database)
        
        try:
            db.connect()
            db.create_tables([ CLIENTS,ORDERS ])
        except peewee.InternalError as p:
            print(str(p))
        
    elif sys.argv[1] == 'fill':
        
        try:
            db.connect()
            for i in range(10):
                CLIENTS.create(NAME='NAME'+str(i+1),CITY='CITY'+str(i+1),ADDRESS='ADDRESS'+str(i+1))
                ORDERS.create(CLIENT=rand.randint(0,10),AMOUNT=i+1,DESCRIPTION='Lab1')
        except peewee.InternalError as p:
            print(str(p))
            
    elif sys.argv[1] == 'show':
        
        TABLES_NAME = ['CLIENTS','ORDERS']
        if sys.argv[2].upper() not in TABLES_NAME:
            print('There is no such table in the database')
        try:
            db.connect()
            if sys.argv[2].upper()=='CLIENTS':
                print('--------TABLES CLIENTS--------')
                print(' ID\tNAME\tCITY\tADDRESS')
                for row in CLIENTS.select():
                    print(row.ID,'\t',row.NAME,'\t',row.CITY,'\t',row.ADDRESS)

            if sys.argv[2].upper()=='ORDERS':
                print('--------TABLES ORDERS--------')
                print(' ID\tCLIENT_id\tDATE\t\t\tAMOUNT\tDESCRIPTION')
                for row in ORDERS.select():
                    print(row.ID,'\t',row.CLIENT_id,'\t',row.DATE,'\t',row.AMOUNT,'\t',row.DESCRIPTION)
                
        except peewee.InternalError as p:
            print(str(p))

    else:
        print('Incorrect input of program arguments')
