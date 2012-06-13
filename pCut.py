# -*- coding:utf-8 -*-

# TODO:
# 3. Fill in the docstring.

import re
from string import maketrans

def rc(seq):
    """Convenience function to get the reverse complement of a sequence."""
    return seq.translate(maketrans("CATGcatg", "GTACgtac"))[::-1]

class Plasmid:
    #class variables
    restriction_enzymes = {
        'ClaI' :    'AT^CGAT',
        'BamHI':    'G^GATCC',
        'BglII':    'A^GATCT',
        'DraI':     'TTT^AAA',
        'DpnI':     'GA^TC',
        'DpnII':    '^GATC',
        'EcoRI':    'G^AATTC',
        'EcoRV':    'GAT^ATC',
        'HindIII':  'A^AGCTT',
        'I-SceI':   'AGTTACGCTAGGGATAA^CAGGGTAATATAG',
        'I-CeuI':   'TAACTATAACGGTCCTAA^GGTAGCGA',
        'NcoI':     'C^CATGG',
        'NlaIII':   'CATG',
        'NotI':     'GC^GGCCGC',
        'PstI':     'CTGCA^G',
        'SalI':     'G^TCGAC',
        'SmaI':     'CCC^GGG',
        'XbaI':     'T^CTAGA',
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
        
    def cut(self, arg):
        """Allow user to ask if there is any RE site independently of
        having this enzyme name in the dictionary.
        Arguments:
            'describe the arguments it takes.'
           ...
        Return:
           'describe what it returns.'
           ..."""
        
        def cut_in_single_orientation(fragments, RE_left, RE_right):
            """Please Olivera fill the docstring"""
            RE_site = RE_left + RE_right
            RE_site_with_cut = RE_left + '^' + RE_right
            
            all_fragments = []
            for frag in fragments:
                # Replace "GATC" by "GA^TC" and split on "^".
                all_fragments.extend(
                    re.sub(RE_site, RE_site_with_cut, frag).split('^')
                )
            return all_fragments

        #########################################
        ## Arguments processing
        #########################################
        try:
           # Try to get 'arg' from RE dictionary.
           RE_site_w_cut = self.restriction_enzymes[arg]
        except KeyError:
           # If not there, take the input as RE sequence.
           RE_site_w_cut = arg.upper()
        try:
           # separate RE site in left and right part at ^ site
           (RE_left, RE_right) = RE_site_w_cut.split('^')
        except ValueError:
           # If ^ is not specified, separare RE site in a half
           half_RE_length = len(RE_site_w_cut)/2
           RE_left = RE_site_w_cut[:half_RE_length]
           RE_right = RE_site_w_cut[half_RE_length:]
           
        RE_site = RE_left + RE_right

        #########################################
        ## Cut plasmid sequence on RE sites
        #########################################
        for seq in (self.sequence, rc(self.sequence)):
            # Try to find the RE site in each orientation. If both fail, return '[]'.
            try:
                # Change sequence offset and remove one RE site if present*.
                start = (2*seq).index(RE_site) + len(RE_site)
            except ValueError:
                continue
            
            end = start + len(seq) - len(RE_site)
            sequence = (2*seq)[start:end]
            
            # Cut in both orientations.
            fragments = cut_in_single_orientation([sequence], RE_left, RE_right)
            fragments = cut_in_single_orientation(fragments, rc(RE_right), rc(RE_left))
            
            # Fix the ends (site removed at line marked with *).
            fragments[0] = RE_right + fragments[0]
            fragments[-1] = fragments[-1] + RE_left
            
            return fragments
            
        # RE site found neither in forward nor in reverse orientation.
        return []


    def get_sizes(self, arg):
        """Return a list with fragment size."""
        return [len(frag) for frag in self.cut(arg)]