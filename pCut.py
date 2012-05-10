# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

import re

class Plasmid:
    #class variables
    restriction_enzymes = {'Cla1' : 'AT^CGAT' , 'BamH1': 'GG^ATCC', 'Bgl II': 'A^GATCT'
                           , 'Dra1':'TTT^AAA' , 'EcoR1':'G^AATTC' , 'EcoRV':'GAT^ATC'
                           , 'HindIII':'A^AGCTT' , 'Pst1':'CTGCA^G' , 'Sal I':'G^TCGAC'
                           , 'SmaI':'CCC^GGG' , 'XmaI':'C^CCGGG'}
    
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
        
    def get_sizes(self, RE_site):
        """Return a list with fragment size."""
        return [len(frag) for frag in self.cut_(RE_site)]
    
    def cut_(self, RE_site):
        """Return a list of plasmid fragments delimited by the
        specified RE_site, and empty list if no site is found."""
        try:
           # Change plasmid offset (early exit if no RE site found).
           start = (2*self.sequence).index(RE_site) + len(RE_site)
           end = start + len(self.sequence) - len(RE_site)
           # Use list comprehension to add site sequence to fragments.
           return [ frag + RE_site for frag in \
                      (2*self.sequence)[start:end].split(RE_site) ]
        except ValueError:
           return []
    
    def RE_name(self, RE_name):
        # to call the method from the same object: self.cut_(...)
        x = self.restriction_enzymes[RE_name].replace('^' , '')
        if self.sequence.find(x) < 0:
           print "There is no restristion enzyme site in your sequence"
        else:
            M = self.restriction_enzymes[RE_name].split('^')
            y = self.sequence.split(x)
            #for i in [len(x)]: #self.sequence.len(x)]:
            y[0] += M[0]
            y[1] = M[1] + y[1]
            print y[0]
            print y[1]
        return None
    
   