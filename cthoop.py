#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import inputDNA
import pCut

if __name__ == '__main__':
   # Gather user parameters.
   (plasmid_file, re_site) = sys.argv[1:]
   try:
      input_seq = inputDNA.Reader(plasmid_file).read()
   except:
      input_seq = inputDNA.Reader_fasta(plasmid_file).read()
   return pCut.REcutter(input_seq).cut(re_site)
