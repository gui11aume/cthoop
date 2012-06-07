# -*- coding:utf-8 -*-

import sys
import re

class Reader():
   def __init__(self, file_name):
      self.file = open(file_name)

   def __del__(self):
      """Ensure that file is properly closed when the Reader
      instance is destroyed."""
      self.file.close()
  
   def read(self):
      self.file.seek(0)
      return self.file.read()


class DNAReader(Reader):
   """Implements a 'check' method to make sure that the content
   of the file is a pure DNA sequence."""

   def __init__(self, file_name):
      Reader.__init__(self, file_name)
      self.selection()

   def selection(self):
      """Categorise the correct file format regarding the given sequence."""
      self.file.seek(0)
      start = self.file.readline().rstrip().upper()
      if start[0] == ">":
         self.file_type = "fasta"
      elif start[0:1] == "ID":
         self.file_type = "embl_gcg"
      elif start[0:5] == "LOCUS":
         self.file_type = "genbank"
      elif start[0] == ";":
         self.file_type = "ig"
      elif not re.search('[^GATCN]', start):
         self.file_type = "plain"
      else:
         self.file_type = None
      return self.file_type

   def filter_nt(self, string):
      return ''.join(re.findall('[GATCN]+', string.upper()))
 

   #######################################
   def read_fasta(self):
      # Skip header.
      self.file.readline()
      return self.filter_nt(self.file.read())

   def read_embl_gcg(self):
      fcontent = self.file.read()
      return self.filter_nt(fcontent[fcontent.index("SQ")+2:])

   def read_genbank(self):
      fcontent = self.file.read()
      # Substring from after "ORIGIN" till end of file.
      return self.filter_nt(fcontent[fcontent.index('ORIGIN')+6:])

   def read_ig(self):
      fc = self.file.read().replace(";","").repace("comment","").upper()
      fc_seq = re.findall('[GATCN]+', fc)
      return fc_seq

   def read_plain(self):
      return self.file.read().upper().replace('\n','').replace('\r','')
   #######################################


   def read(self):
      self.file.seek(0)
      if self.file_type == "fasta":
         return self.read_fasta()
      elif self.file_type == "embl_gcg":
         return self.read_embl_gcg()
      elif self.file_type == "genbank":
         return self.read_genbank()
      elif self.file_type == "ig":
         return self.read_ig()
      elif self.file_type == "plain":
         return self.read_plain()
      else:
         raise Exception('unknown file format')


if __name__ == '__main__':
   print(DNAReader(sys.argv[1]).read())


