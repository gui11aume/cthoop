# -*- coding:utf-8 -*-

import re

class Reader():

   def __init__(self, file_name):
      self.file = open(file_name)
  
   def read(self):
      self.file.seek(0)
      return self.file.read()
    
class Reader_fasta(Reader):
   """A class checking a input sequence in a fasta file"""

   #Class variables
   correct_nucleotide = "ATCGN"
   
   #Class methods
   
   def read(self):
      """clean the head"""
      self.file.seek(0)
      header = self.file.readline()
      if header[0] == ">":
         return self.file.read().replace("\n", "").replace("\r", "")
      else:
         raise Exception("It is not a fasta file!")

   def seq_check(self):
      """check whether a sequence containing reasonable letters"""
      read_seq = self.read()
      for letter in read_seq:
         if not letter in self.correct_nucleotide:
            print "The given sequence contains wrong nucleotides."
      return

   def seq_letter_convert(self):
      """convert letters to a correct form"""
      read_seq = self.read()
      return read_seq.upper()      


if __name__ == '__main__':
   print(DNA_seq(sys.argv[1]))


