import pytest
import main
import os.path

def test_database():
    
    assert os.path.exists(main.name_database) == True

def test_rowcountclients():

    assert len(main.CLIENTS.select()) == 10

def test_rowrountorders():
   
    assert len(main.ORDERS.select()) == 10

def test_testcollumnclients():
   
    try:
        x = main.CLIENTS.select(main.CLIENTS.ID,main.CLIENTS.NAME,main.CLIENTS.CITY, main.CLIENTS.ADDRESS)
    except:
        assert False

def test_testcollodders():
    
    try:
        x = main.ORDERS.select(main.ORDERS.ID,main.ORDERS.CLIENT_id,main.ORDERS.DATE, main.ORDERS.AMOUNT,main.ORDERS.DESCRIPTION)
    except:
        assert False
