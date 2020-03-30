## SpeciesExplorer ([Project Tutorial](https://sssgrowth.github.io/SPECIESEXPLORER/))
### + Updating... +
This project contains the experimental datasets and codes. This is a preview version of the tutorial. The detailed descriptions are still in the making. 

### Contents

* [Data](#data)
  * [v0.6](#v0.6)
  * [v0.5](#v0.5)
  * [v0.4](#v0.4)
  * [v0.3](#v0.3)
  * [v0.2](#v0.2)
  * [v0.1](#v0.1)
  * [Biomedical Embeddings](#biomedical-embeddings)
* [Updating](#updating)

## Data
### v0.6
[Download](https://drive.google.com/drive/folders/1I34zw3ZMB7d1AQrKTDdwJ0TndU85BVwl?usp=sharing) on Google drive.
+ Experimental datasets
	+ PMC Mention Mention (train/dev/test set)
	+ PMC Semantics (train/dev/test set)
	+ PubMed (train/dev/test set)

The entire corpus will be organized and released soon.[Download]()

### v0.5
[Download]
+ Experimental datasets
	+ PMC Mention Mention (train/dev/test set)
	+ PMC Semantics (train/dev/test set)
	+ PubMed (train/dev/test set)

### v0.4
[Download]
+ Experimental datasets
	+ PMC Mention Mention (train/dev/test set)
	+ PMC Semantics (train/dev/test set)
	+ PubMed (train/dev/test set)


### v0.3
[Download](https://pan.baidu.com/s/163Ferpz9ZCvcQgRXTRQSqw). Code: f5ic This version of data will be accessed by an api for convenient query and management. Currently, the abstract and full-text datasets have been uploaded to the Baidu Yun for temporary management. It includes the following files:

+ Whole corpus datasets
	+ abstract (train/dev/test set), full-text (train/dev/test set)
+ Experimental datasets
	+ PubMed (train/dev/test set)
	+ PMC (train/dev/test set)
+ Predefined (23) species  

### v0.2
[Download](https://pan.baidu.com/s/1PY-_mxds7A_HoyWysjsxlA). The abstract and full-text datasets have been uploaded to the Baidu Yun for temporary management. It includes the following files:

+ Whole corpus datasets
	+ PubMed (train/dev/test set)
	+ PMC (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: PubMed (train/test set), PMC (train/test set)
	+ implicit inference: PubMed (train/test set), PMC (train/test set)
+ Predefined (23) and extended (64) species  


### v0.1 
[Download](https://drive.google.com/drive/folders/1VIHEbRtPeWo66L6zaEjyv30qizC_fdQB?usp=sharing). The abstract and full-text datasets are uploaded to the Google Drive. It includes the following files:

+ Whole corpus datasets
	+ PubMed (train/dev/test set)
	+ PMC (train/dev/test set)
+ Experimental 8,000/2,000 datasets
	+ explicit extraction: PubMed (train/test set), PMC (train/test set)
	+ implicit inference: PubMed (train/test set), PMC (train/test set)
+ Predefined (23) and extended (64) species

The labels of training data is generated based on word occurences and rules. The labels of test/development set are manually refined.

### Biomedical Embeddings
This toolkit provides a pretrained version of [GloVe.PubMed.200d](d) and [FastText.PubMed.300d](d) embeddings for biomeidcal research.  This version is trained on the PubMed and PMC datasets for two days by the GloVe and the FastText respectively.  
PubMed [literature](https://www.ncbi.nlm.nih.gov/pubmed/)  
 <img src="./icon/pubmed.png" width="150">  <img src="./icon/wiki.png" width="80"><img src="./icon/pubmedcentral.jpg" width="110">
 

## Updating...
* 2020-Mar-20, SpecExplorer v0.7, refactoring the code 

* 2019-Dec-20, SpecExplorer v0.6, enhance the result analysis. Work toward semi-automated species mining, knowledge transfer and data analysis. Strengthen knowledge mining to help resolve human healthcare problems. Introduce the biomedical ontologies, gene terms, bioNLP, etc.    
* 2019-Dec-01, SpecExplorer v0.5, resample and redivide the datasets. Update the glossary with NCBI Taxonomy. Propose a new symbol \*SPECIES\* to mask species mentions. Hide more complete speices mentions.  
* 2019-Oct-01, update the name to SpecExolorer. Apply BERT to species classification task. Create two versions of dataset. Update the glossary and manually check and refine the labels of some samples in PubMed and PMC datasets v0.4.  
* 2019-Mar-29, propose sequence-to-sequence classification model. Formulate the species classification task. Update the glossary and manually check and refine the labels of some samples in PubMed and PMC datasets v0.3. Summarize and upgrade the standard of semantic-based annotation.  
* 2018-Nov-03, summarize the tasks of extracting explicit mentions of species and the task of species inferences. Update the glossary and manually check and refine the labels of some samples in PubMed and PMC datasets v0.2.  
* 2018-Aug-26, build SpeciesExplorer for mining the biomedical literature from a species perspective to help resolve healthcare problems of humans. Create the PubMed and PMC datasets v0.1, initial version.  

