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
        fragments[0] = fragments[n-1] + fragments[0]
        del(fragments[n-1])
        x = [s.split(RE_site) for s in fragments[0]]
        for x in range (n-1):
            fragments[x] += RE_site
        new_fragments = fragments[0].split(RE_site)
        m = len(new_fragments)
        if m > 1:
            for i in range (m-1):
                new_fragments[i] += RE_site
        else:
            pass
        fragments = new_fragments + fragments
        return fragments
    
    def cut_shorter(self, RE_site):
        double_sequence = 2 * self.sequence
        x = double_sequence.find(RE_site)
        n = len(self.sequence)
        if x>0:
            fragments = double_sequence[x::]
            fragments = fragments[:-(n-x)]
            fragments = fragments.split(RE_site)
            del(fragments[0])
            k = len(fragments)
            for y in range (k):
                fragments[y] += RE_site
        else:
            return "There is no restriction ezyme cut in your sequence"
        #new_fragments = fragments[0].split(RE_site)
        #m = len(new_fragments)
        #if m > 1:
         #   for i in range (m-1):
          #      new_fragments[i] += RE_site
        #else:
         #   pass
        #fragments = new_fragments + fragments
        return fragments
    
    def number_of_fr(self, RE_site):
        return len(self.cut(RE_site))
        
    def fr_length(self, RE_site):
        x = self.cut(RE_site)
        # Use list comprehension.
        return [len(string) for string in x]
    

    

    
