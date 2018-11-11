## SpeciesExplorer ([Project Tutorial](https://sssgrowth.github.io/SPECIESEXPLORER/))


#### As long as this paper is accepted, this toolkit can be downloaded.
SpeciesExplorer is a toolkit designed for species resarch in the biomedical area. This tutorial is a preview. The detailed descriptions are still in the making and it will soon be online.

### Contents

* [Data](#data)
  * [v0.2](#v0.2)
  * [v0.1](#v0.1)
  * [Biomedical Embeddings](#biomedical-embeddings)
* [Who can use](#who-can-use)
  * [Installation](#installation)
  * [Hyperparameters](#hyperparameters)
* [Updating](#updating)

## Data
### v0.2
[Download](https://pan.baidu.com/s/1sl-91yIlybtqjc67k67AvQ). The abstract and full-text datasets are uploaded to the Baidu Yun. It includes the following files:

+ Whole corpus datasets
	+ abstract (train/dev/test set), full-text (train/dev/test set)
	+ full-text (train/dev/test set), full-text (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Predefined (23) and extended (64) species

### v0.1 
[Download](https://drive.google.com/drive/folders/1VIHEbRtPeWo66L6zaEjyv30qizC_fdQB?usp=sharing). The abstract and full-text datasets are uploaded to the Google Drive. It includes the following files:

+ Whole corpus datasets
	+ abstract (train/dev/test set), full-text (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: abstract (train/test set), full-text (train/test set)
	+ implicit inference: abstract (train/test set), full-text (train/test set)
+ Predefined (23) and extended (64) species

The labels of training data is generated based on word occurences and rules. The labels of test/development set are manually refined.

### Biomedical Embeddings
This toolkit provides a pretrained version of [GloVe.PubMed.200d](d) and [FastText.PubMed.300d](d) embeddings for biomeidcal research.  This version is trained on the PubMed and PMC datasets for two days by the GloVe and the FastText respectively.  
PubMed [literature](https://www.ncbi.nlm.nih.gov/pubmed/)  
 <img src="./icon/pubmed.png" width="150">  <img src="./icon/wiki.png" width="80"><img src="./icon/pubmedcentral.jpg" width="110">
 
## Who can use
Users can define any interested species. This system might be helpful to different domains, i.e. the brain science, cell line, gene/protein, disease, chemicals, etc.  
It provides three modes, the extraction, the inference and the exploration modes which are adaptive to different demands. If researchers only care about the predefined species, it can run in the extraction/inference mode. If they want to infer the species from the literature, it can run in the inference mode. If they are interested in discovering what unexpected species are involved, it can run in the exploration mode.


### Installation
```
usage: run.py [-h] [-m MODE] [-mp MODEL] [-u USER] [-f FILE] [-t TYPE]
              [-s SPLIT] [-a ATTENTION]

This list provides the options to control the runing status.

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  The runing mode: train or test
  -mp MODEL, --model MODEL
                        Set the model path.
  -u USER, --user USER  Different training process: train, train, test
  -f FILE, --file FILE  The input file that users want to extract or infer
                        species.
  -t TYPE, --type TYPE  Select a model to run. backen, attention, exploriation
                        ... corresponding to different models
  -s SPLIT, --split SPLIT
                        0,1
  -a ATTENTION, --attention ATTENTION
                        Output the animal attention. 0,1, 0=False, 1=True
```
## Updating...

* 2018-Aug-26, Abstract and Full-text dataest v0.1, initial version
* 2018-Nov-03, Abstract and Full-text dataest v0.2, refine some labels

