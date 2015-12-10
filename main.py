#!/usr/bin/env python3
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
class DB_Functions:
    """Functions to be called from the Menu."""
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
    def power_name(self):
        pname = input("Please type in the name of the Power you would like to see the information of:  ")
        power = (pname.upper(),)
        for row in self.c.execute('''SELECT DISTINCT powers.power_name as Power, trees.tree_name as Tree, power_trees.tier as Tree_Tier, factions.subfaction as Splat from innate_tree join factions on innate_tree.subfaction_id=factions.subfaction_id join trees on trees.tree_id=innate_tree.tree_id join power_trees on power_trees.tree_id=trees.tree_id join powers on powers.power_id=power_trees.power_id WHERE upper(powers.power_name) =?''', power):
            print(row)
    def tree_name(self):
        tname = input("Please type in the name of the Tree you would like to see the powers of:  ")
        tree = (tname.upper(),)
        for row in self.c.execute('''SELECT DISTINCT powers.power_name as Power, trees.tree_name as Tree, power_trees.tier as Tree_Tier, factions.subfaction as Splat from innate_tree join factions on innate_tree.subfaction_id=factions.subfaction_id join trees on trees.tree_id=innate_tree.tree_id join power_trees on power_trees.tree_id=trees.tree_id join powers on powers.power_id=power_trees.power_id WHERE upper(trees.tree_name) =?''', tree): 
            print(row)
    def power_type(self):
        pow_type = input("Please type in a comma separated list of each power type you would like to see.  Touch, Damage, Self, Mental, Other, Status, Mask, Passive, Sensory.:  ")
        type_list = (("".join(pow_type.split())).split(','))
        for selection in type_list:
            sel = (selection.upper(),)
            for row in self.c.execute('''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(type)=?''', sel):
                print(row)
    def meta_type(self):
        meta = input("Please type in a comma separated list of each meta type you would like to see. None, Meta, Condition, Type, Counted.:  ")
        meta_list = (("".join(meta.split())).split(','))
        for selection in meta_list:
            sel = (selection.upper(),)
            for row in self.c.execute('''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(meta)=?''', sel):
                print(row)
    def st_only(self):
        for row in self.c.execute('''SELECT DISTINCT power_name,type,meta,cost,call,text,breachable FROM powers WHERE st_only =1'''):
            print(row)
    def breach(self):
        for row in self.c.execute('''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only FROM powers WHERE breachable =1'''):
            print(row)
#
#
class Menu:
    def __init__(self, db):
        self.db = db
    def selector(self, selection):
        if selection == '1':
            self.db.power_name()
        elif selection == '2':
            self.db.tree_name()
        elif selection == '3':
            self.db.power_type()
        elif selection == '4':
            self.db.meta_type()
        elif selection == '5':
            self.db.st_only()
        elif selection == '6':
            self.db.breach()
        else:
            print("You have not selected a valid option.  Please select again.")
            selection = input("Please select what function you would like.\n\t[1] Search by name(s)\n\t[2] Search by Tree\n\t[3] Search by Power Type\n\t[4] Search by Power Meta\n\t[5] View all ST_Only power\n\t[6] View all powers that are Breachable\n\n")
            self.selector(selection)
#
#
if __name__ == "__main__":
    db = DB_Functions('Powers_20151116.sqlite')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
    selection = input("Please select what function you would like.\n\t[1] Search by name(s)\n\t[2] Search by Tree\n\t[3] Search by Power Type\n\t[4] Search by Power Meta\n\t[5] View all ST_Only power\n\t[6] View all powers that are Breachable\n\n")
    Menu(db).selector(selection)
