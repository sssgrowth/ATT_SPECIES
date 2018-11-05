## SpeciesExplorer

Here is the project [page](https://sssgrowth.github.io/ATT_SPECIES/).    

#### As long as this paper is accepted, this toolkit can be downloaded.

### Data
#### v0.2: 
[Download](https://pan.baidu.com/s/1sl-91yIlybtqjc67k67AvQ). The abstract and full-text datasets are uploaded to the Baidu Yun. It includes the following files:

+ Whole corpus datasets
	+ abstract (train/dev/test set), full-text (train/dev/test set)
	+ full-text (train/dev/test set), full-text (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Predefined (23) and extended (64) species

#### v0.1: 
[Download](https://drive.google.com/drive/folders/1VIHEbRtPeWo66L6zaEjyv30qizC_fdQB?usp=sharing). The abstract and full-text datasets are uploaded to the Google Drive. It includes the following files:

+ Whole corpus datasets
	+ abstract (train/dev/test set), full-text (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Predefined (23) and extended (64) species

The labels of training data is generated based on word occurences and rules. The labels of test/development set are manually refined.

The pretrained [GloVe.PubMed.200d](d)  
PubMed [literature](https://www.ncbi.nlm.nih.gov/pubmed/)  
 <img src="./icon/pubmed.png" width="150">  <img src="./icon/wiki.png" width="80"><img src="./icon/pubmedcentral.jpg" width="110">
 
### Who can use?
Users can define any interested species. This system might be helpful to different domains, i.e. the brain science, cell line, gene/protein, disease, chemicals, etc. This system provides three modes: the explicit extraction mode, the implicit inference mode and the increment mode.  
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
* 2018-Nov-03, Abstract and Full-text dataest v0.2

