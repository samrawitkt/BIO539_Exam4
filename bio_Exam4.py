#!/usr/bin/env python3

import pandas as pd
import operator
import sys 
import argparse


def observed_kmer(read,k):
  
  """
    This function generates number of observed k-mers taking read and k arguments.
    
    Parameters: 
    read: the string that need to be read
    k: the input kmer value, where length starts from 1 to length of string 
  
    Returns:
    integer: the number of observed kmers
  """

  poss_val = [] #empty list uses to store all possible kmers
  obse_val= []  # empty list to store observed kmers i.e only unique kmers
  count = 0       # start from 0
  #string = len(read)  # find length of read string
  read = read.strip() # used to remove all the leading and trailing spaces from the string
  
  for i in range(0,len(read)-k+1):  # Loop over the kmer start positions
    poss_val.append(read[i:i+k]) # Slice the string to get the kmer and adding all possible kmer to df
    
    #to calculate only observed kmers(unique) from df of possible kmer
  
    for item in poss_val:   
      if item not in obse_val:  # Add the kmer to the df if it's not there 
        count += 1   # Increment the count for this kmer
        obse_val.append(item)
  #print(count)
  return(count) 

def possible_kmer(read,k):
  """
    This function generates number of possible k-mers taking read and k arguments.
    takes the minimum possible kmers after calculating length of string minus k plus 1
    then 4^k
    
    read: the string that need to be read
    k: the input kmer value, where length starts from 1 to length of string 
  
    Returns:
    integer: the number of all possible kmers
    """
  #string = len(read) # find length of read string
  read = read.strip()# used to remove all the leading and trailing spaces from the string

  poss_val = [] #empty list uses to store all possible kmers

  poss_val.append(min(len(read)-k+1,4**k)) # calculates the possible kmers taking the formula and append
  
  print(poss_val) 
  return poss_val


def dataframe_kmer(read):
  """
    This function generates dataframe with columns kmers(k), observed kmers and possible kmers
    
    Parameters: 
    read: the string/sequence of the argument as input
    
    Return:
    dataframe: with index number k, lenth of observed kmers and length of possible kmers
    """
  kk = []       #empty list for kmers
  poss_kmer = []#empty list for possible kmers
  obse_kmer = []#empty list for observed kmers

  string = len(read.strip()) # change length of read(input string from user) to be added with int value and remove extra spaces from string
  #print(string)
  kk = list(range(1,string+1))
  #print(kk)  
  for i in kk: #looping each kmers
    poss_kmer.append(min(string-i+1,4**i))# calculates the possible kmers taking the formula and append in list

  for i in kk:
    k_obs = observed_kmer(read,i)
    obse_kmer.append(k_obs)
  
#  print(obse_kmer)
    
  kmer_df = pd.DataFrame(     # creating pandas the data frame
    {
      'k':kk,
      'Observed kmers':obse_kmer, #assigning each values to the data frame columns k, observed kmers and possible kmers
      'Possible kmers':poss_kmer
    }
  )
  return kmer_df

def linguistic_complexity(read): 
  
  """
    This function takes data frame as input argument and produces the linguistic complexity, 
    the proportion of k-mers that are observed compared to the total number that are theoretically possible
        
    Parameters: 
     Pd.dataframe: A table (data frame) created by the table function
    
    Return:
    ling_comp: linguistic complexity
  """
  kmer_df = dataframe_kmer(read)                    # calling the dataframe and assign to new variable
  total_obse_kmer = sum(kmer_df['Observed kmers'])  #sum of observed kmers to find total observed kmers
  total_poss_kmer = sum(kmer_df['Possible kmers'])  #sum of possible kmers to find total possible kmers
  ling_comp = total_obse_kmer/total_poss_kmer       #linguistic complexity calculated
  return ling_comp

if __name__ =='__main__':
  
  myfile = sys.argv[1]
  with open(myfile,'r') as current_file:
    for line in current_file: # reads line by line
    #print(read[i])
      read = line
      #print(read)
      df= dataframe_kmer(line)
      df.to_csv(read+'file.csv') #creates csv file
      lc_seq = linguistic_complexity(read)
      print("The linguistic complexity of", read, "is", lc_seq) # print a message reading the linguistic complexity
     

