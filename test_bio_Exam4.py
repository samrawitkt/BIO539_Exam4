from bio_Exam4 import *
  
import pandas as pd


#Testing observed kmers

def test_observed_kmer_1():      
  read = 'ATTTGGATT'                     
  k = 1                                  
  actual_result = observed_kmer(read,k)  
  expected_result = 3                   
  assert actual_result==expected_result

def test_observed_kmer_2():      
  read = 'ATTTGGATT'                      
  k = 9                                 
  actual_result = observed_kmer(read,k)   
  expected_result = 1                   
  assert actual_result==expected_result
  
#Testing possible kmers

def test_possible_kmer_1():
  read = 'ATTTGGATT'
  k = 3
  actual_result = possible_kmer(read,k)
  expected_result = 7
  assert actual_result!=expected_result
  
#Testing the data frame 

def test_dataframe_kmer_1():
 
  data = [[1,3,4],[2,3,3],[3,2,2],[4,1,1]] 
  expected_result = pd.DataFrame(data, columns = ['k','observed_kmers', 'possible_kmers'], index = [1,2,3,4])
  read = 'AGGT'
  actual_result = dataframe_kmer(read)
  result = expected_result.equals(actual_result)
  assert result == False
  
#Testing linguistic complexity
  
def test_linguistic_complexity_1():
  read = 'AGGT'
  actual_result = linguistic_complexity(read)
  expected_result = 0.9
  assert actual_result==expected_result
  
def test_linguistic_complexity_2():
  read = 'ATTTGGATT'
  actual_result = linguistic_complexity(read)
  expected_result = 0.875
  assert actual_result==expected_result
  
