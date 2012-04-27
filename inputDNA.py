import re

class Reader:
  """A class checking a input sequence"""

   #Class variables
   input_seq:""
   correct_nucleotide: "ATCGN"
   
   #Class methods
   def __init__(self, input_seq):
      """remove the first line in data without sequence"""
      file = open("self.input_seq"))
      for line in file:
         if line[0] == ">":
            pass
         else:
            print line
      return
  
   def read_least(self, inout_seq):
      """remove the least symbol in a sequence"""
      file = open("self.input_seq")
      read_seq = file.read()
      read_seq = read_seq("\n", "")
      return read_seq

      def seq_check(self, input_seq):
         """check whether a sequence containing reasonable letters"""
         self.input_seq = input_seq
         file = open("self.input_seq")
         read_seq = file.read()
         for letter in read_seq:
            if not letter in self.correct_nucleotide:
               print "The given sequence contains wrong nucleotides."
         return


if __name__ == '__main__':
   print(DNA_seq(sys.argv[1]))


