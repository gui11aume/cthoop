# @Olivera: this is your file. Change the name the way you want.
# I suggest you start by creating a 'Plasmid' class that contains
# the basic information about a plamid (mostly the sequence).
# You can write a 'cut(self, RE_site)' method that returns a
# list with the length of the fragments.

class Plasmid:
    #class variables
    
    #class methods
    def __init__(self, sequence):
        self.sequence = sequence
        
    def cut(self, RE_site):
        fragments = self.sequence.split(RE_site)
        return fragments
    
    def number_of_fr(self, RE_site):
        return len(self.cut(RE_site))
        
    def fr_length(self, RE_site):
        x = self.cut(RE_site)
        for string in x:
            print len(string)
        return 
    

    

    
