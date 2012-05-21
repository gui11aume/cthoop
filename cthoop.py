#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import prettytable

import inputDNA
import pCut

if __name__ == '__main__':
   # Gather user parameters.
   (plasmid_file, RE_site) = sys.argv[1:]
   input_seq = inputDNA.DNAReader(plasmid_file).read()
   sizes = sorted(pCut.Plasmid(input_seq).get_sizes(RE_site), reverse=True)
   if sizes:
      output = prettytable.PrettyTable()
      output.add_column('Fragment', range(1, 1+len(sizes)))
      output.add_column('Size', sizes)
      output.printt()
   else:
      sys.stdout.write('No site found.\n')
