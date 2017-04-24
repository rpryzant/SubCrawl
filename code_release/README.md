
## Requirements
These can all be installed with pip.

* python >= v2.7.11
* `pysrt`
* `guessit`
* `tqdm`
* `pyunpack`
* `ffmpy`
* `nltk`

Additionally, some of the corpus_processing scripts make use of [google/sentencepiece](https://github.com/google/sentencepiece):


## Description

Welcome to the SubCrawl code release! What follows are each of the subdirectories, their constitutent programs, and a brief description of what each program does.

For an implementation of the proxy-A-distance algorithm outlined in the paper, please refer to [this repository](https://github.com/rpryzant/proxy-a-distance). 


### corpus_generation

Scripts for downloading, parsing, and aligning subtitles from the internet.

### corpus_cleaning

Scripts for converting file formats, thresholding on length ratios, and spellchecking.

### corpus_processing

Scripts for manipulating completed datasets, including tokenization and train/test/dev splitting.


