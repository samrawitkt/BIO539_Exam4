from code import *

import pandas as pd

#Testing observed kmers
def test_observed_kmer_1():
  k = 1
  read = 'AGGT'
  actual_result = observed_kmer(read,k)
  expected_result= 4
  assert actual_result == expected_result
  
def test_observed_kmer_2():
  k = 5
  read = 'AATGGGGCA'
  actual_result = observed_kmer(read,k)
  expected_result= 6
  assert actual_result == expected_result
  
 
#Testing possible kmers

def test_possible_kmer_1():
   k = 2
   read = 'ATTTGGATT'
   actual_result = possible_kmer(read,k)
   expected_result= 9
   assert actual_result == expected_result
   
   
def test_possible_kmer_2():
   k = 4
   read = 'AGGT'
   actual_result = possible_kmer(read,k)
   expected_result= 2
   assert actual_result == expected_result
   
#The test for making the table function

def test_dataframe_kmer_1():
  data = [[4,4],[4,4],[3,3],[2,2],[13,13]] 
  expected = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  read = 'AGGT'
  actual_result = dataframe_kmer(read)
  result = expected_result.equals(actual_result)
  assert result == True
  
def test_dataframe_kmer_2():
  data = [[5,4],[7,9],[7,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2],[46,48]] 
  expected = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9, 'total'])
  read = 'AATGGGGCA'
  actual_result = dataframe_kmer(read)
  result = expected_result.equals(actual_result)
  assert result == True
  
#The test for the linguistic complexity function

def test_linguistic_complexity_1():
  data = [[5,4],[7,9],[7,8],[7,7],[6,6],[5,5],[4,4],[3,3],[2,2],[46,48]] 
  kmer_df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4,5,6,7,8,9, 'total'])
  actual_result = linguistic_complexity(kmer_df)
  expected_result = 0.9583333333333334
  assert actual_result == expected_result
  
def test_linguistic_complexity_2():
  data = [[4,4],[4,4],[3,3],[2,2],[13,13]] 
  kmer_df = pd.DataFrame(data, columns = ['observed_kmers', 'possible_kmers'], index = [1,2,3,4, 'total'])
  actual_result = linguistic_complexity(kmer_df)
  expected_result = 1.0
  assert actual_result == expected_result
