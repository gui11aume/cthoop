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

   def selection(self):
      """Categorise the correct file format regarding the given sequence."
      self.file.seek(0)
      start = self.file.readline().upper()
      if start[0] == ">":
         print "This is a fasta file."
      elif start[0:1] == "ID" and start[-1] == "//":
         print "This is an EMBL file."
      elif start[0:1] == "ID" and start[-1] != "//":
         print "This is a GCG file.""
      elif start[0:5] == "LOCUS":
         print "This is a GenBank file."
      elif start[0] == ";":
         print "This is an IG file."
      elif re.search('[^GATCN]', start[0:-1]) == 0:
         print "This is a plain file."
      else:
         print "No corret file format is found."
      return

   def check(self):
      if re.search('[^GATCN]', self.read()):
         raise Exception ('Not a DNA sequence')

    
class FastaReader(DNAReader):
   """A class checking an input sequence in a fasta file"""

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

   def seq_read(self):
      """read throgh only the nucleotide sequence in a fasta file"""
      fc = self.read().upper()
      fc_nucleotide = re.finall([GATCN]+,fc)
      fc_seq = "".join.(fc_nucleotide[:])
      return fc_seq

class GCGReader(DNAReader):
   """A class checking and orginasing an input sequence in a GCG file"""
   
   #Class methods

   def seq_read(self);
      fc = self.file.read().upper()
      fc_start = fc[fc.index('..')+2:]
      fc_nucleotide = re.findall([ATCG]+,fc_start)
      fc_seq = "".join(fc_nucleotide[:])
      return fc_seq

class EMBLReader(DNAReader):
   """A class checking and orginasing an input sequence in a EMBL file"""
   
   #Class methods
   
   def seq_start(self):
      """find the first line of the aequence start"""
      fc = self.file.readlines()
      for fc_start in fc:
         if fc_start[0:1] == "SQ":
            fc_nucleotide += fc
      
   def seq_read(self):
      """elimiating spaces within the sequence context"""
      fc_nuc = self.seq_start().repalce("//","")
      fc_seq = "".join(fc_nuc[:])
      return fc_seq

class GenBankReader(DNAReader):
   """A class checking and orginasing an input sequence in a GenBank file"""

   #Class variables
   correct_nucleotide = "ATCGN"

   #Class methods
      
   def seq_read(self):≈
      fc = self.file.read()
      # Substring from after "ORIGIN" till end of file.
      fc_start = fc[fc.index('ORIGIN')+6:]
      fc_nucleotide = re.findall([GATCN]+,fc_start)
      fc_seq = "".join(fc_nucleotide[:])
      return fc_seq

class IGReader(DNAReader):

  #Class methods
  
  def seq_read(self):
     fc = self.file.read().replace(";","").repace("comment","").upper()
     fc_seq = re.findall([GATCN]+,fc)
     return fc_seq

class PlainReader(DNAReader):

   def seq_read(self):
      return self.file.read()


if __name__ == '__main__':
   print(DNA_seq(sys.argv[1]))


