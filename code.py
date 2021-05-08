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
  obse_val= []  # again to store observed kmers i.e only unique kmers
  count = 0       # start from 0
  #string = len(read)  # find length of read string
  
  for i in range(0,len(read)-k+1):  # Loop over the kmer start positions
    poss_val.append(read[i-1:i-1+k]) # Slice the string to get the kmer and adding all possible kmer to df
  #to calculate only observed kmers(unique) from df of possible kmer
  for item in poss_val:   
      if item not in obse_val:  # Add the kmer to the df if it's not there 
        count += 1   # Increment the count for this kmer
        obse_val.append(item)
  return (count) 

def possible_kmer(read,k):
    """
    This function generates number of possible k-mers taking read and k arguments
    
    read: the string that need to be read
    k: the input kmer value, where length starts from 1 to length of string 
  
    Returns:
    integer: the number of all possible kmers
    """
    #string = len(read) # find length of read string
    poss_val = [] #empty list uses to store all possible kmers
    if k == 1:   
        return 4; # if k equal to 1, 4^1=4
    else:
        for i in range(0,len(read)-k+1):
            poss_val.append(read[i-1:i-1+k]) # adding possible kmers to a df
            
        return len(poss_val)
        
  
def dataframe_kmer(read):
    """
    This function generates dataframe with columns kmers(k), observed kmers and possible kmers
    
    Parameters: 
    read: the string/sequence of the argument as input
    
    Return:
    dataframe: with index number k, lenth of observed kmers and length of possible kmers
    """
    data = [] # start with setting an empty data frame 
    string = len(read) # Find the length of the string 
    for i in range(1, string): # loop over the kmer start position 
        data.append([observed_kmer(read,i), possible_kmer(read,i)]) # add the calculated poss & obs kmers and add to the df 
    # compiling the df with respective column values and total row at the bottom    
    kmer_df = pd.DataFrame(data, index = range(1,string), columns = ['observed_kmers', 'possible_kmers'])  
    kmer_df.loc['total']= kmer_df.sum()
    return(kmer_df)
    
def linguistic_complexity(kmer_df): 

    """
    This function takes data frame as input argument and produces the linguistic complexity, 
    the proportion of k-mers that are observed compared to the total number that are theoretically possible
        
    Parameters: 
     Pd.dataframe: A table (data frame) created by the table function
    
    Return:
    ling_comp: linguistic complexity
    """
    ling_comp= kmer_df.loc['total','observed_kmers']/kmer_df.loc['total','possible_kmers'] # linguistic completity calculated
    return ling_comp


if __name__ =='__main__':
    myfile = sys.argv[1]
    with open(myfile,'r') as current_file:
         for line in current_file: # reads line by line
            #print(read[i])
             read = line
             df= dataframe_kmer(line)
             df.to_csv(read+'file.csv') #creates csv file
             lc_seq = linguistic_complexity(df)
             print("The linguistic complexity of", read, "is", lc_seq) # print a message reading the linguistic complexity
        #plot_kmer_prop(read[i]) # produce the plot for kmer proportion

    
    
          
        
