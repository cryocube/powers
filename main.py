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
#
#
class DB_Functions:
    """Functions to be called from the Menu."""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
    def power_name(self):
        query = '''SELECT DISTINCT powers.power_name as Power, trees.tree_name as Tree, power_trees.tier as Tree_Tier, factions.subfaction as Splat from innate_tree join factions on innate_tree.subfaction_id=factions.subfaction_id join trees on trees.tree_id=innate_tree.tree_id join power_trees on power_trees.tree_id=trees.tree_id join powers on powers.power_id=power_trees.power_id WHERE upper(powers.power_name) =?'''
        names=("absolution","aggravated_1","aggravated_claws","appear","avert","avoidance","balefire","beast_mind","black_ichor","body_wrack","break_attunement","brittle_bones","brutal_strike","clawed_form","cleanse","cloak","cloak_gathering","cloak_sight","cognizance","conditioning","confusion","control_body","control_voice","corrupted_powers","craving","dark_sword","daze","decay","derange","despair","detect_fetter","detect_taint","disable","disarm","disembodied","disquiet","dreamshape","endure","entrancement","exorcism","expel_corpus","fabricate_armor","fast_healing","fetter_consumption","fetter_creation","fire_2","fire_4","fire_sword","forgetful_mind","form_of_vapor","frenzy","frenzy_control","gauntlet_walk","give_energy","god's_grace","grant_power","hallucination","hasty_escape","healing_touch","health_exchange","hellborn_investiture","hero's_stand","hidden_taint","hide_of_the_wyrm","horrid_reality","hypnotism","imitate","induce_catharsis","induce_sin","insight","leech_of_fear","light_sword","majesty","mask_of_a_thousand_faces","materialize","meditate","meld","might","mimic","monsters","move_object","obedience","paralyze","passion","pathos_exchange","pathos_investment","pence_from_heaven","poison_immunity","possession","powerful_form","purify","ranged_2","ranged_4","razor_claws","read_magic","realm_grasp","release_spirit","rend_the_lifeweb","resilience","resist_gauntlet","resist_taint","restore_essence","revive","root","sanctuary","scion_of_evil","secret_angst","sense_amaranth","sense_confidence","sense_demon","sense_desire","sense_emotion","sense_essence","sense_faction","sense_fetter","sense_gnosis","sense_health","sense_item","sense_maximum_health","sense_mental","sense_patron","sense_power","sense_shadow","sense_spirit","sense_subfaction","sense_vitae","serenity","shadow_coax","shatter","shunt","silence","silver_armor","silver_claws","silver_tongue","smell_fear","snarl","song_of_rage","spirit_drain","stonehand_punch","strength","subjugate","taint","taunt","telepathy","tentacles","terror","test_generation","test_oath","totemic_form","tough_form","toughness","true_form","umbra_drain","umbra_sight","umbra_strike","vengeance_of_samiel","venom","visions","weaponry","wither","withstand","woadling","wounding_lies")
        pname = input("Please type in the names of the Powers (if it is two words, replace the space with a _) you would like to see the information of, in a comma separated list:  ")
        proc_pname = (Sanitizer().sanitize_pname(pname)).lower()
        pow_list = ("".join(proc_pname.split())).split(',')
        pow_list = [v for v in pow_list if v in names]
        print("\n\nDisplaying all text for: " + str(pow_list) + "\n\n")
        for v in pow_list:
            vstring = str(v)
            proc_vstring = str()
            for c in vstring:
                if ord(c) == 95:
                    proc_vstring += ' '
                else:
                    proc_vstring += c
            power = ((str(proc_vstring).upper()),)
            print(str(power))
            for row in self.c.execute(query, power):
                print(row)
    def tree_name(self):
        query = '''SELECT DISTINCT powers.power_name as Power, trees.tree_name as Tree, power_trees.tier as Tree_Tier, factions.subfaction as Splat from innate_tree join factions on innate_tree.subfaction_id=factions.subfaction_id join trees on trees.tree_id=innate_tree.tree_id join power_trees on power_trees.tree_id=trees.tree_id join powers on powers.power_id=power_trees.power_id WHERE upper(trees.tree_name) =?'''
        tnamelist = ("animal", "body", "curse", "healer", "perception", "mind", "patterns", "protection", "spirit", "warrior", "ahl-i-batin", "messianic_voices", "old_faith", "order_of_hermes", "spirit_talkers", "valdaermen", "veneficti", "enticer", "ferectori", "gorehound", "toad", "animalism", "auspex", "celerity", "chimerstry", "daimoinon", "deimos", "dementation", "dominate", "fortitude", "mortis", "mytherceria", "necromancy", "obfuscate", "obtenebration", "potence", "presence", "protean", "quietus", "serpentis", "valeren_healer", "valeren_warrior", "vicissitude", "visceratika", "thaumaturgy:_creo_ignem", "thaumaturgy:_rego_aquam", "thaumaturgy:_rego_vitae", "dark_thaumaturgy:_path_of_the_defiler", "dark_thaumaturgy:_rego_dolor", "dark_thaumaturgy:_rego_manes", "dark_thaumaturgy:_rego_pestes", "dark_thaumaturgy:_rego_phobos", "homid", "metis", "lupus", "ahroun", "galliard", "philodox", "ragabash", "theurge", "black_furies", "bone_gnawers", "children_of_gaia", "fenrir", "fiana", "red_talons", "shadow_lords", "silent_striders", "silver_fangs", "warders_of_man", "bagheera", "bubasti", "ceilican", "swara", "ananasi", "corax", "ratkin", "corruption", "cunning", "defiling", "strength", "argos", "castigate", "embody", "fatalism", "flux", "inhabit", "intimation", "keening", "lifeweb", "mnemosynis", "moliate", "outrage", "pandemonium", "phantasm", "puppetry", "usury", "contaminate", "hive_mind", "larceny", "maleficence", "tempest_weaving", "black_spiral_dancer")
        tname = input("Please type in the names of the Trees you would like to see the powers of:  ")
        proc_tname = (Sanitizer().sanitize_tname(tname)).lower()
        tree_list = ("".join(proc_tname.split())).split(',')
        tree_list = [v for v in tree_list if v in tnamelist]
        print("\n\nDisplaying the following Trees: " + str(tree_list) + "\n\n")
        for v in tree_list:
            vstring = str(v)
            proc_vstring = str()
            for c in vstring:
                if ord(c) == 95:
                    proc_vstring += ' '
                else:
                    proc_vstring += c
            tree = ((str(proc_vstring).upper()),)
            print(str(tree))
            for row in self.c.execute(query, tree):
                print(row)
    def power_type(self):
        query = '''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(type)=?'''
        types = ('touch', 'damage', 'self', 'mental', 'other', 'status', 'mask', 'passive', 'sensory')
        pow_type = input("Please type in a comma separated list of each power type you would like to see.\nOptions are:\n " + str(types) + "  :  ")
        proc_type = Sanitizer().sanitize_input(pow_type)
        type_list = (("".join(pow_type.split())).split(','))
        # Note: Using list comprehension.  Note for self.        
        type_list = [v for v in type_list if v in types]
        print("Displaying all options for: " + str(type_list))
        for selection in type_list:
            sel = (selection.upper(),)
            for row in self.c.execute(query, sel):
                print(row)
    def meta_type(self):
        query = '''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only,breachable FROM powers WHERE upper(meta)=?'''
        metas = ('none', 'meta', 'condition', 'type', 'counted')
        meta = input("Please type in a comma separated list of each meta type you would like to see.\nOptions are:\n " + str(metas) + "  :  ")
        proc_meta = Sanitizer().sanitize_input(meta)
        meta_list = (("".join(proc_meta.split())).split(','))
        # Note: Using list comprehension.  Note for self.
        meta_list = [v for v in meta_list if v in metas]
        print("Displaying all options for: " + str(meta_list))
        for selection in meta_list:
            sel = (selection.upper(),)
            for row in self.c.execute(query, sel):
                print(row)
    def st_only(self):
        query = '''SELECT DISTINCT power_name,type,meta,cost,call,text,breachable FROM powers WHERE st_only =1'''
        for row in self.c.execute(query):
            print(row)
    def breach(self):
        query = '''SELECT DISTINCT power_name,type,meta,cost,call,text,st_only FROM powers WHERE breachable =1'''
        for row in self.c.execute(query):
            print(row)
#
#
class Menu:
    def __init__(self, db):
        self.db = db
    def prompt(self):
        selection = input("Please select what function you would like.\n\t[1] Search by name(s)\n\t[2] Search by Tree\n\t[3] Search by Power Type\n\t[4] Search by Power Meta\n\t[5] View all ST_Only power\n\t[6] View all powers that are Breachable\n\n")
        return selection
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
            sel = Menu(db).prompt()
            self.selector(sel)
#
#
class Sanitizer:
    def __init__(self):
        pass
    def sanitize_input(self, raw_string):
        string = str()
        slist = list()
        for c in raw_string:
            if ord(c) == 32 or ord(c) == 44 or 65<=ord(c)<=90 or 97<=ord(c)<=122:
                string += c
            else:
                string += ''
        return string
    def sanitize_pname(self, raw_string):
        string = str()
        slist = list()
        for c in raw_string:
            if ord(c) == 39 or ord(c) == 95 or ord(c) == 32 or ord(c) == 44 or 48<=ord(c)<=57 or 65<=ord(c)<=90 or 97<=ord(c)<=122:
                string += c
            else:
                string += ''
        return string
    def sanitize_tname(self, raw_string):
        string = str()
        slist = list()
        for c in raw_string:
            if ord(c) == 45 or ord(c) == 39 or ord(c) == 95 or ord(c) == 32 or ord(c) == 44 or 48<=ord(c)<=57 or 65<=ord(c)<=90 or 97<=ord(c)<=122:
                string += c
            else:
                string += ''
        return string
#
#
#
if __name__ == "__main__":
    db = DB_Functions('powers.sqlite')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
    sel = Menu(db).prompt()
    Menu(db).selector(sel)
