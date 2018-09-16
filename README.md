## SPECIES EXTRACTION AND INFERENCE

Here is the project [page](https://sssgrowth.github.io/ATT_SPECIES/).    

### Data

Abstract and Full-text datasets are listed [here](https://drive.google.com/drive/folders/1VIHEbRtPeWo66L6zaEjyv30qizC_fdQB?usp=sharing). It includes the following files:

+ Whole corpus datasets
+ Experimental 8,000/2,000 datasets
+ Predefined and extended species

The pretrained [GloVe.PubMed.200d](d)  
PubMed [literature](https://www.ncbi.nlm.nih.gov/pubmed/)  
 <img src="./icon/pubmed.png" width="200">

### Usage
```
usage: run.py [-h] [-m MODE] [-mp MODEL] [-q QUESTION] [-a ANSWERS] [-u USER]
              [-f FILE] [-t TYPE] [-s SPLIT]

process some parser

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  train or test
  -mp MODEL, --model MODEL
                        None or model path
  -q QUESTION, --question QUESTION
                        question path
  -a ANSWERS, --answers ANSWERS
                        answer path
  -u USER, --user USER  train test inter
  -f FILE, --file FILE  train test inter
  -t TYPE, --type TYPE  backen,aspect
  -s SPLIT, --split SPLIT
```
### Updating...

* 2018-Aug-26, Abstract and Full-text dataest v0.1, initial version


