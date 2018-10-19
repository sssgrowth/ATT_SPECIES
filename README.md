## SPECIES EXTRACTION AND INFERENCE

Here is the project [page](https://sssgrowth.github.io/ATT_SPECIES/).    

### Data

Abstract and Full-text datasets are listed [here](https://drive.google.com/drive/folders/1VIHEbRtPeWo66L6zaEjyv30qizC_fdQB?usp=sharing). It includes the following files:

+ Whole corpus datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Predefined (23) and extended (64) species

This data set is relativly large. We will upload the result part on the Google Drive.

The pretrained [GloVe.PubMed.200d](d)  
PubMed [literature](https://www.ncbi.nlm.nih.gov/pubmed/)  
 <img src="./icon/pubmed.png" width="150">  <img src="./icon/wiki.png" width="80">
 
### Who can use?
This system can be applied to different domains, i.e. the brain science, cell line, gene/protein, disease, chemicals etc. This system provides three modes: the explicit extraction mode, the implicit inference mode and the increment mode.  
It is adaptive to different demands. If researchers only care about the predefined species, they can run the system in the extraction mode. If researchers want to infer some literature that didn’t explicitly mention the species, they can run the system in the inference mode. If researchers are interested in discovering what other species are involved, they can run the system in the increment mode. 


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


