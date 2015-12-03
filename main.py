# Powers - Original Beginning Scope is to be able to query Powers from a SQLite DB
# Potential to be used as a spring board for other offerings
#
# Original Author: Kyle Ricks
# Organization: Shadow Accord - NW LARPers
#
# Imports
#
import sys
import sqlite3
#
#
# class Menu: will also go here in time
#
class DB:
    """Menu for selecting functions for how to return a power set.

    """
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = conn.cursor()
    def menu(self): #Do last

        pass
    def power_name(self):
        
        pass
    def tree_name(self):
        pass
    def power_type(self):
        pass
    def meta_type(self):
        meta = input("Please type in a comma separated list each meta type you would like to see. None, Meta, Condition, Type, Counted")
        meta_list = (("".join(meta.split())).split(','))
        for selection in meta_list:
            sel = (selection,)
            for row in self.c.execute('SELECT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE meta=?', sel)

    def st_only(self):
        for row in self.c.execute("SELECT power_name,type,meta,cost,call,text,breachable FROM powers WHERE st_only =1")
        print(row)
    def breach(self):
        for row in self.c.execute("SELECT power_name,type,meta,cost,call,text,st_only FROM powers WHERE breachable =1")
        print(row)
#
#
if __name__ = "__main__":
    db = DB('Powers_20151116.sqlite')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
#
