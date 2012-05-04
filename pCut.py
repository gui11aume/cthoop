# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

import re

class Plasmid:
    #class variables
    
    #class methods
    def __init__(self, sequence, check_and_fmt=True):
        sequence = self.check_and_fmt(sequence)
        self.sequence = sequence

    def check_and_fmt(self, sequence):
        """Check that sequence contains only DNA letters, otherwise
        raise an Exception, then format sequence to upper-case."""
        sequence = sequence.upper()
        if re.search('[^GATCN]', sequence):
           raise Exception ('Not a DNA sequence')
        else:
           return sequence
        
    def cut(self, RE_site):
        """Return a list of plasmid fragments delimited by the
        specified RE_site, and 'None' if no site is found."""
        fragments = self.sequence.split(RE_site)
        n = len(fragments)
        if n == 1:
            return None
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
    
    def cut_(self, RE_site):
        """Return a list of plasmid fragments delimited by the
        specified RE_site, and 'None' if no site is found."""
        try:
           # Change plasmid offset (early exit if no RE site found).
           start = (2*self.sequence).index(RE_site) + len(RE_site)
           end = start + len(self.sequence) - len(RE_site)
           # Use list comprehension to add site sequence to fragments.
           return [ frag + RE_site for frag in \
                      (2*self.sequence)[start:end].split(RE_site) ]
        except ValueError:
           return None
