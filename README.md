# Cecilia Schramm - Semi-supervised learning for data creation in the A-PROOF project

# Overview
This repository contains the code used in the thesis "Using Semi-supervised Learning to Automatically Annotate Dutch Medical Notes for Patients’ Functioning Levels" by Cecilia Schramm, supervised by Dr. Piek Vossen of the VU Amsterdam, in partial fulfilment of the requirements for the degree of an MA in Linguistics.

This is part of the [A-PROOF](https://cltl.github.io/a-proof-project/) project and used data provided by the [AUMC](https://www.amsterdamumc.org/en/about/organization/about-amsterdam-umc.htm) on their secure servers. The A-PROOF repository can be found at <https://github.com/cltl/a-proof-zonmw> and files that remained unchanged from their original files are not included in this project.

This thesis is based on and uses the [A-PROOF ICF-domains Classification](https://huggingface.co/CLTL/icf-domains) system for its experiments, created by Jenia Kim.

This thesis also uses code from the [KeywordMatcher](https://github.com/cltl/KeywordMatcher) repository, though unchanged files from there or files that are needed in combination with the data for this project are also not included in this repository.

# Project structure

```
thesis-project
└───a-proof-zonmw
│       │   predict_copy_binary.py
│       │   predict_copy.py
│       │   train_model_copy.py
│       │   config.json
└───KeywordMatcher
│       │   all_sents_inspection.ipynb
│       │   cs_eval_new3.ipynb
│       │   cs_inspection.ipynb
│       │   index_inspection.ipynb
│       │   matched_notes.ipynb
│       │   convert copy.json
│       │   get_relevant_sents_copy.py
│       │   get_relevant_sents.py
└───Baseline
│       │   bl_eval_cm.png
│       │   bl_eval_cm2.png
│       │   bl_test_cm.png
│       │   bl_test_cm2.png
│       │   eval_eval.ipynb
│       │   eval_test.ipynb
└───hq_data1
│       │   eval_ell_sh.ipynb
│       │   eval.ipynb
│       │   hq1_cm_test.png
│       │   hq1_cm.png
│       │   hq1_cm2_test.png
└───hq_data2 - lqhq_data3
│       │   eval.ipynb
│       │   [data name]_cm.png
│   .gitignore
│   LICENSE
│   README.md
│   requirements.tx
│   eval_best_model.ipynb
│   jenia_test.ipynb
│   test_separation_ell_sh.ipynb
│   test_separation_jenia.ipynb
│   tfidf_scores_final.ipynb
```

**a-proof-zonmw**
```predict_copy_binary.py```: Using [Cecilia Kuan's](https://github.com/lececefifi/a-proof-zonmw) binary classifier for predictions

```predict_copy.py```: Using Jenia Kim's multi-label classification system for predictions, but adding confidence scores to the outcome

```train_model_copy.py```: Training Jenia Kim's model, either from the start or checkpoints

```config.json```: Configurations for my experiments

**KeywordMatcher**
```all_sents_inspection.ipynb```: Inspecting the matched notes returned from KeywordMatcher and dividing their sentences into equal amounts per ICF category

```cs_eval_new3.ipynb```: Dividing the final data by confidence score into high or low quality data

```cs_inspection.ipynb```: Inspecting the confidence scores given to the data

```index_inspection.ipynb```: Inspecting the matched notes from KeywordMatcher by year and category

```matched_notes.ipynb```: Inspecting the matched notes from KeywordMatcher by amounts

```convert copy.json```: Configurations for my experiments

```get_relevant_sents_copy.py```: Get sentences matched with a keyword and category, no duplicates

```get_relevant_sents.py```: Get sentences matched with a keyword and category

**Baseline**
```eval_eval.ipynb```: Evaluating the baseline on the development set

```eval_test.ipynb```: Evaluating the baseline on the test set

**hq_data1**
```eval_ell_sh.ipynb```: Evaluating ModelHQ1 on the test set

```hq_data1 - eval.ipynb```: Evaluating ModelHQ1 on the development set

**hq_data2 - lqhq_data3**
```hq_data2 - lqhq_data3```: Each of these folders includes one ```eval.ipynb```file, that evaluates the model on the development set, and one .png file that shows its confusion matrix as a picture

**General**
```eval_best_model.ipynb```: Inspecting all models' performances

```test_separation_ell_sh.ipynb```: Removing all none's from the original test set, after running them through Cecilia Kuan's binary classifier

```test_separation_jenia.ipynb```: Removing all none's from the original development set, after running them through Cecilia Kuan's binary classifier

```tfidf_scores_final.ipynb```: Calculating 20 highest ranked TF-IDF words per category



# Data 
The path to the data used for this project on the secure AUMC servers is
```mnt/data/Users/A-PROOF/Cecilia_S/```
All data used or necessary for this project can be found in this location and its subsequent folders within.

# Requirements
All code must be run on the secure servers on the AUMC, where the necessary data for this thesis is stored and cannot be moved from. All requirements are stored there.

