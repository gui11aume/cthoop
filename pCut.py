# -*- coding:utf-8 -*-

import re
from string import maketrans

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

def rc(seq):
    """Convenience function to get the reverse complement."""
    return seq.translate(maketrans("CATGcatg", "GTACgtac"))[::-1]


def cut_forward(fragments, RE_left, RE_right):
   """Sub-cut a series of fragments in a single orientation
   looking for the RE site only on the forward strand.
   Arguments:
      fragments: list of restriction fragments
      RE_left: part of the restriction site left of the cut
      RE_right: part of the restriction site right of the cut
   Return:
      List of fragments.
   """
   
   # The trick used below is to replace the restriction 
   # enzyme site ('RE_left + RE_right') by the split site
   # ('RE_left + "^" + RE_right') and split the string
   # on the ^ character.
   sub_fragments = []
   for fragment in fragments:
      sub_fragments.extend(
         fragment.replace(
            RE_left + RE_right,
            RE_left + '^' + RE_right,
         ).split('^')
      )
   return sub_fragments


class Plasmid:
   
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
      
   def cut(self, arg_list):
      """Allow user to ask if there is any RE site independently of
      having this enzyme name in the dictionary.
      Arguments:
         arg: list of either enzyme names or a restriction sites
      Return:
         List of restriction fragments, or [] if no site."""

      # Return value.
      fragments = []

      for arg in arg_list:

         ##########################################
         ##           Process arguments          ##
         ##########################################

         try:
            # Try to get 'arg' from RE dictionary.
            RE_site_w_cut = restriction_enzymes[arg]
         except KeyError:
            # If not there, take the input as RE sequence.
            RE_site_w_cut = arg.upper()
         try:
            # Separate RE site in left and right part (split on ^).
            (RE_left, RE_right) = RE_site_w_cut.split('^')
         except ValueError:
            # If ^ is not specified, separare RE site in a half.
            half_RE_length = len(RE_site_w_cut)/2
            RE_left = RE_site_w_cut[:half_RE_length]
            RE_right = RE_site_w_cut[half_RE_length:]
            

         #############################################
         ##    Cut plasmid sequence on RE sites     ##
         #############################################

         RE_site = RE_left + RE_right

         # If plasmid was cut on previous iterations just subcut.
         if fragments:
            fragments = cut_forward(fragments, RE_left, RE_right)
            fragments = cut_forward(fragments, rc(RE_right), rc(RE_left))
            continue

         # Otherwise cut the circular plasmid (needs extra care).
         for seq in (self.sequence, rc(self.sequence)):
            # Try to find the RE site in each orientation.
            # If both fail, return '[]'.
            try:
               # Get offset and remove one RE(*) (if found).
               # This deletion will be corrected below.
               start = (2*seq).index(RE_site) + len(RE_site)
            except ValueError:
               continue
            
            # Change offset. Set it on first RE site found.
            end = start + len(seq) - len(RE_site)
            sequence = (2*seq)[start:end]
            
            # Cut in both orientations.
            fragments = cut_forward([sequence], RE_left, RE_right)
            fragments = cut_forward(fragments, rc(RE_right), rc(RE_left))
            
            # Fix the ends (site removed at line marked with *).
            fragments[0] = RE_right + fragments[0]
            fragments[-1] = fragments[-1] + RE_left
            
      # No more arguments to process.
      return fragments


   def get_sizes(self, arg):
      """Return list with restriction fragment size."""
      return [len(frag) for frag in self.cut(arg)]
