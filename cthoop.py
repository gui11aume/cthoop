#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import prettytable
import argparse

import inputDNA
import pCut

if __name__ == '__main__':
   # Gather user parameters.
   parser = argparse.ArgumentParser(
       prog='cthoop',
       description='Cut The Hell Out Of Plasmids.'
   )
   parser.add_argument(
       'plasmid',
       help = 'file containing the plasmid sequence'
   )
   parser.add_argument(
       'RE',
       nargs='+',
       help = 'restriction enzyme or sequence to cut the plasmid'
   )
   args = parser.parse_args()
   plasmid = args.plasmid
   RE = args.RE

   input_seq = inputDNA.DNAReader(plasmid).read()
   sizes = sorted(pCut.Plasmid(input_seq).get_sizes(RE), reverse=True)
   if sizes:
      output = prettytable.PrettyTable()
      output.add_column('Fragment', range(1, 1+len(sizes)))
      output.add_column('Size', sizes)
      output.printt()
   else:
      sys.stdout.write('No site found.\n')
