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
        pass
    def st_only(self):
        pass
    def breach(self):
        pass
#
#
if __name__ = "__main__":
    db = DB('Powers_20151116.sqlite')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
#
