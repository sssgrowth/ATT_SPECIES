## SpeciesExplorer ([Project Tutorial](https://sssgrowth.github.io/SPECIESEXPLORER/))


#### As long as this paper is accepted, this toolkit can be downloaded.
SpeciesExplorer is a toolkit designed for species resarch in the biomedical area. This is a preview version of the tutorial. The detailed descriptions are still in the making.

### Contents

* [Data](#data)
  * [v0.3](#v0.3)
  * [v0.2](#v0.2)
  * [v0.1](#v0.1)
  * [Biomedical Embeddings](#biomedical-embeddings)
* [Who can use](#who-can-use)
  * [Installation](#installation)
  * [Hyperparameters](#hyperparameters)
* [Updating](#updating)

## Data
### v0.3
[Download](https://pan.baidu.com/s/1PY-_mxds7A_HoyWysjsxlA). This version of data will be accessed by an api for convenient query and management. Currently, the abstract and full-text datasets have been uploaded to the Baidu Yun for temporary management. It includes the following files:

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
 

```
## Updating...

* 2018-Aug-26, Abstract and Full-text dataest v0.1, initial version
* 2018-Nov-03, Abstract and Full-text dataest v0.2, refine some labels
* 2019-Mar-29, Abstract and Full-text dataest v0.3, refine some labels
