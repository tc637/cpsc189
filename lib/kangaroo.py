# -*- coding: utf-8 -*-
"""
A.B. Downey, Chapter 17 Exercise 7
kangaroo.py
TC
"""

class Kangaroo(object):
    """A Kangaroo is a mammal with a pouch (marsupial)."""
    
    def __init__(self,pouch_contents=None):
        """Initializes objects"""
        
        # If object's pouch has None in it, initialize as empty list
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents
        
    def put_in_pouch(self,item):
        """Appends objects to kangaroo's pouch"""
        self.pouch_contents.append(item)
        
    def __str__(self):
        """Returns string of object and the contents of its pouch"""
        
        # list of strings for output
        full_str = [ object.__str__(self) + ' has in its belly:' ]
        
        # append each object in pouch to the full string list
        for thing in self.pouch_contents:
            thing_str = '\t' + object.__str__(thing)
            full_str.append(thing_str)
            
        # join the pieces of the full string list into one string with newlines 
        return '\n'.join(full_str)
        

# testing        
kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch('apples')
kanga.put_in_pouch('pears')
kanga.put_in_pouch('oranges')

# should work for items with int and float types too
roo.put_in_pouch(5)
roo.put_in_pouch(20.)
roo.put_in_pouch('pickles')

kanga.put_in_pouch(roo)

print(kanga)
print(roo)