# BIO539_Exam4
# Finding The linguistic complexity of the string

## What Is This?

This is a simple Python script intended to provide the linguistic complexity of the string defined as the number of kmers that are observed for all possible k-mer lengths, divided by the total number that are theoretically possible.
The goal of this script is to get one output file for each string containing a data frame, and a statement about linguistic complexity printed to the command line.\

## Development

The steps followed to write the linguistic complexity of the string(sequence) after initializing python script (bio_Exam4.py) :\

**1,** Created a function that calculates observed k-mers (unique k_mers) taking read(string) and K(int) values as an argument.\
**2,** Created a function calculates all the possible k-mers also taking read and K values as an argument.\
       Possible Kmers is calculated as the minimum of the length of the string minus k plus 1, and 4^k.\
**3,** Created a panda data frame function taking read value as an argument containing expected kmers(K), observed k-mers and all possible k-mers columns.\
**4,** Created a function that calculates linguistic complexity taking dataframe as an argument.\
**5,** Created a main function that reads any string given by user and calculates the lingustic complexity.\
**6,** Created a separate string.csv excel file with some sequence examples.\
#### When a python script run, using the command line, outputs the linguistic complexity of each sequence in a file of sequences.\

## Testing

**1,** created a separate testing python script using the same python script name adding test infront(test_bio_Exam4.py).\
**2,** Import all the data from the main python script (bio_Exam4.py).\
**3,** Call each funtion at a time provide one kmer value and a sequence from our string.csv excel file to assert the actual result with expected result.
