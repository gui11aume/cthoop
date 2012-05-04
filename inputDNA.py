# -*- coding:utf-8 -*-

import re

class Reader():
   def __init__(self, file_name):
      self.file = open(file_name)
      self.check()

   def __del__(self):
      """Ensure that file is properly closed when the Reader
      instance is destroyed."""
      self.file.close()

   def check(self):
      """Implemented only in subclasses."""
      pass
  
   def readon(self):
      return self.file.read()

   def read(self):
      self.file.seek(0)
      return self.readon()



class DNAReader(Reader):
   """Implements a 'check' method to make sure that the content
   of the file is a pure DNA sequence."""

   def readon(self):
      return self.file.read().replace("\n", "").replace("\r", "").upper()

   def check(self):
      if re.search('[^GATCN]', self.read()):
         raise Exception ('Not a DNA sequence')

    
class FastaReader(DNAReader):
   """A class checking a input sequence in a fasta file"""

   #Class variables
   correct_nucleotide = "ATCGN"
   
   #Class methods
   
   def read(self):
      """clean the head"""
      self.file.seek(0)
      header = self.file.readline()
      if header[0] == ">":
         return self.readon()
      else:
         raise Exception("It is not a fasta file!")

   def seq_check(self):
      """check whether a sequence containing reasonable letters"""
      read_seq = self.read()
      for letter in read_seq:
         if not letter in self.correct_nucleotide:
            print "The given sequence contains wrong nucleotides."
      return


if __name__ == '__main__':
   print(DNA_seq(sys.argv[1]))


