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
        name = input("Please type in the name of the Power you would like to see the information of.")
        power = (name.upper(),)
        for row in self.c.execute('
        SELECT DISTINCT
            powers.power_name as Power,
            trees.tree_name as Tree,
            power_trees.tier as Tree_Tier,
            factions.subfaction as Splat
        from innate_tree 
        join factions on innate_tree.subfaction_id=factions.subfaction_id
        join trees on trees.tree_id=innate_tree.tree_id
        join power_trees on power_trees.tree_id=trees.tree_id
        join powers on powers.power_id=power_trees.power_id
        WHERE upper(powers.power_name) =?', power)   
            print(row)
    def tree_name(self):
        name = input("Please type in the name of the Tree you would like to see the powers of.")
        tree = (name.upper(),)
        for row in self.c.execute('
        SELECT DISTINCT
            powers.power_name as Power,
            trees.tree_name as Tree,
            power_trees.tier as Tree_Tier,
            factions.subfaction as Splat
        from innate_tree 
        join factions on innate_tree.subfaction_id=factions.subfaction_id
        join trees on trees.tree_id=innate_tree.tree_id
        join power_trees on power_trees.tree_id=trees.tree_id
        join powers on powers.power_id=power_trees.power_id
        WHERE upper(trees.tree_name) =?', tree)   
            print(row)
    def power_type(self):
        pow_type = input("Please type in a comma separated list of each power type you would like to see.  Touch, Damage, Self, Mental, Other, Status, Mask, Passive, Sensory.")
        type_list = (("".join(meta.split())).split(','))
        for selection in type_list:
            sel = (selection.upper(),)
            for row in self.c.execute('SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(type)=?', sel)
                print(row)
    def meta_type(self):
        meta = input("Please type in a comma separated list of each meta type you would like to see. None, Meta, Condition, Type, Counted.")
        meta_list = (("".join(meta.split())).split(','))
        for selection in meta_list:
            sel = (selection.upper(),)
            for row in self.c.execute('SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(meta)=?', sel)
                print(row)
    def st_only(self):
        for row in self.c.execute("SELECT DISTINCT power_name,type,meta,cost,call,text,breachable FROM powers WHERE st_only =1")
        print(row)
    def breach(self):
        for row in self.c.execute("SELECT DISTINCT power_name,type,meta,cost,call,text,st_only FROM powers WHERE breachable =1")
        print(row)
#
#
if __name__ = "__main__":
    db = DB('Powers_20151116.sqlite')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
#
