import pytest
import main
import os.path

def TestDatabase():
    
    assert os.path.exists(main.name_database) == True

def RowCountClients():

    assert len(main.CLIENTS.select()) == 10

def RowCountOrders():
   
    assert len(main.ORDERS.select()) == 10

def TestCollumnClients():
   
    try:
        x = main.CLIENTS.select(main.CLIENTS.ID,main.CLIENTS.NAME,main.CLIENTS.CITY, main.CLIENTS.ADDRESS)
    except:
        assert False

def TestCollOdders():
    
    try:
        x = main.ORDERS.select(main.ORDERS.ID,main.ORDERS.CLIENT_id,main.ORDERS.DATE, main.ORDERS.AMOUNT,main.ORDERS.DESCRIPTION)
    except:
        assert False
