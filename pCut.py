# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

import re

class Plasmid:
    #class variables
    
    #class methods
    def __init__(self, sequence):
        self.sequence = sequence
        
    def cut(self, RE_site):
        fragments = self.sequence.split(RE_site)
        n = len(fragments)
        if n == 1:
            return "There is no restriction enzyme site in your sequence"
        else:
            pass
        fragments[0] = fragments[n-1] + fragments[0]
        del(fragments[n-1])
        for g in range (n-1):
            fragments[g] += RE_site
        temporary = fragments.pop(0)
        new_fragments = temporary.split(RE_site)   
        i = len(temporary.split(RE_site))
        if i > 1:
            for m in range (i-1):
                new_fragments[m] += RE_site
        else:
            fragments[0] = temporary 
        fragments = new_fragments + fragments
        return fragments
        
    def fr_length(self, RE_site):
        x = self.cut(RE_site)
        return [len(string) for string in x]
        #stg
    

    

    
