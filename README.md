![](src/figures/section_header.png)

# Genetic Engineering Attribution

by Jacob Prebys

### Overview

Here I will have all of my work for the Genetic Engineering Attribution Challenge competition from DrivenData. The site gives the following motivation and overview for the competition:

> Genetic engineering attribution is the process of identifying the source of a genetically engineered piece of DNA. Reducing anonymity can encourage more responsible behavior within scientific and entrepreneurial communities, without stifling innovation. The objective of this competition is to predict the laboratory of origin for plasmid DNA sequence

### Data Acquisition

Like all DataDriven competitions, you must make an account and register for the competition before you can download the data. Once you have done that you can download the training features and training labels, both of which are ~300 MB .csv files. 

### Data Understanding

![](src/figures/samplecounts.png)

First thing to note is that there is a huge class imbalance here. One laboratory accounts for over 8,000 samples, while the average is 47 samples per lab. Two labs are only represented by one sample, so dealing with class imbalance will be a huge factor in increasing model performace. Here is 

### Modeling

As seen in the competition benchmark, one way of breaking down the gene sequences is to just count the individual subsequences. I used both overlapping and non-overlapping counters, but I have not been able to get a score higher than about 60%. My next idea was encode each subsequence as a number, and then turn the sequences into Numpy arrays representing the order oof the subsequences. This way, all


# Contact Info


|  Github |         email         | LinkedIn |
|:-------:|:---------------------:|:--------:|
| jprebys | jacobprebys@gmail.com |  jprebys |

*Header illustration by Brian Stauffer*
