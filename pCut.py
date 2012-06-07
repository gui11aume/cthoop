# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

import re

class Plasmid:
    #class variables
    restriction_enzymes = {
        'ClaI' :    'AT^CGAT',
        'BamHI':    'G^GATCC',
        'BglII':    'A^GATCT',
        'DraI':     'TTT^AAA',
        'DpnI':     'GA^TC',
        'DpnII' :   '^GATC',
        'EcoRI':    'G^AATTC',
        'EcoRV':    'GAT^ATC',
        'HindIII':  'A^AGCTT',
        #'I-SceI' :  'AGTTACGCTAGGGATAA^CAGGGTAATATAG',
        'NcoI':     'C^CATGG',
        'NlaIII' :  'CATG',
        'NotI' :    'GC^GGCCGC',
        'PstI':     'CTGCA^G',
        'SalI':     'G^TCGAC',
        'SmaI':     'CCC^GGG',
        'XbaI' :    'T^CTAGA',
        'XmaI':     'C^CCGGG',
    }

    
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
        
    def cut(self, RE_name):
        """Return a list of plasmid fragments delimited by the
        specified RE_site, and 'None' if no site is found."""
        RE_site_w_cut = self.restriction_enzymes[RE_name]
        RE_site_wo_cut = RE_site_w_cut.replace('^', '')
        (RE_left, RE_right) = RE_site_w_cut.split('^')
        # Change sequence offset.
        try:
            start = (2*self.sequence).index(RE_site_wo_cut) + len(RE_site_wo_cut)
            end = start + len(self.sequence) - len(RE_site_wo_cut)
            sequence = (2*self.sequence)[start:end] 
            fragments = sequence.split(RE_site_wo_cut)
            for i in range (len(fragments)):
                fragments[i] = RE_right + fragments[i] + RE_left
            return fragments
        except ValueError:
            return []
    
        #return [RE_right + frag + RE_left for frag in sequence.split(RE_site_wo_cut)]
        #n = len(fragments)
            
            
            
        #if n == 1:
        #    return fragments
        #else:
        #    pass
        #temporary = fragments.pop(n-1)
        #fragments[0] = temporary + fragments[0]
        #temporary2 = fragments.pop(0)
        #new_fragments = temporary2.split(y)
        #if len(new_fragments) == 1:
        #  #  print 'There is one RE_site'
        #    return fragments
        #else:
        #  new_fragments [0] = new_fragments[0] + L[0]
        #  new_fragments [1] = L[1] + new_fragments[1]
        #fragments = new_fragments + fragments
        #return fragments
        
    def get_sizes(self, RE_site):
        """Return a list with fragment size."""
        return [len(frag) for frag in self.cut_(RE_site.upper())]
    
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
           return []
    
    
    def cut_2(self, RE_site):
        """Return a list of plasmid fragments delimited by the
        specified RE_site, and empty list if no site is found."""
        try:
           # Change plasmid offset (early exit if no RE site found).
           start = (2*self.sequence).index(RE_site) + len(RE_site)
           end = start + len(self.sequence) - len(RE_site)
           # Use list comprehension to add site sequence to fragments.
           if len[(2*self.sequence)[start:end].split(RE_site)] %2 == 0 :
            return [ frag + RE_site in \
                      (2*self.sequence)[start:end].split(RE_site) ]
           else:
                return [ RE_site + frag in \
                      (2*self.sequence)[start:end].split(RE_site) ]
        except ValueError:
           return []
    

    def separate(self, RE_site):
        #for RE_site in restriction_enzymes:
         #   print self.RE_site()
        x= self.restriction_enzymes.get(RE_site)
        L= x.split('^')
       # self.cut(self, RE_site)
        print L
        
       # L[0], L[1]
      
        return None
