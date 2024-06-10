# Digital Methods - Data Collection

**Table of Contents:**

1. [Project](#project)
    - [Data Collection](#data-collection)
    - [Outline](#outline-of-the-study)
    - [Immersion Journal](#immersion-journal)
    - [Code Book](#code-book)
5. [Technical Requirements](#requirements)


## Project

This repository is related to the Exam **Digital Methods** at the **University of Copenhagen** for the Masters degree **Social Data Science**. The underlying project aims to explore Climate Contrarian Narratives.

The project includes the code, qualitative and quantitative data, as well as the documentation of the qualitative and quantitative approaches.

Write a Request for the data to: marco.l@correlaid.org

### Abstract of Methodology

> To examine how climate contrarians claims are developing and spreading throughout the
internet, this paper builds on three different analyses. Firstly, we will share the findings
of our qualitative analysis using open and focused coding techniques. This approach will
allow us to immerse ourselves in the dynamics of the community and comprehensively
analyse the claims made in the comments on the selected videos. Secondly, we will show
the results of our quantitative analysis to describe the distribution of the found claims
within the qualitative analysis and thus confirm our assumptions about their separation
into "old" and "new” claims. In addition, we will capture through our classifier the
interaction between these claims and assess their linkage. The last analyses is focusing
on this connection with the integration of a network analysis.

### Data Collection

- The process and code of the data collection can be found in the script `data-collection.ipynb`.

- The list of sampled channels can be found [here](data/channel_sampling.xlsx).
    - The related Codebook can be found in the following section: [Code Book](#code-book).

### Outline of the Study

The Data Analysis is staged into different parts.

1. Explorative Sampling of the Comments. Through the sampling function of the script `sampling-open-coding.ipynb`.
    - The related Open Coding file can be found [here](#immersion-journal).
2. Focused analysis of the comments with the Helper script `focused_coding.ipynb` where we can insert keywords which were identified through topic modelling in the script `topic-modelling.ipynb` or `Word2vec.ipynb`.
    - The related Immersion Journal from the Focused Coding, keywords and reflection on the explored comments up to that point, can be found [here](#immersion-journal).
4. Classification of the comments in a qualitative way with a closed coding approach. The related Codebook can be found in the section [Code Book](#code-book).
3. The quantitative dictionary classifier of the comments can be found in the script `dictionary-classifier.ipynb`.

The script `preprocessing_functions.py` includes functions which where used in the different scripts. Each function is descript in the file.

### Immersion Journal

The Immersion Journal captures the comments from the focused and open Coding approach used in this study. The Immersion Journal can be found [here](immersion_journal/immersion_journal.xlsx).

- The related Codebook can be found in the following section: [Code Book](#code-book).

### Code Book

- Find the Codebook for the Channel Sampling [here](documentation/codebook_sampling.md).
- Find the Codebook for the Immersion Journal [here](documentation/codebook_immersion-journal.md).
- Find the Codebook for the Closed Coding [here](documentation/closed-codebook_immersion-journal.md).

## Requirements

### API Key

To run the code and get YouTube comments, you have to get an API key for YouTube. The explanation to create a key, you can find [here](https://developers.google.com/youtube/v3/getting-started#before-you-start).

The Script `data-collection.ipynb` will ask you for the API key. You can read it in with creating a `api_key.py` file and store it as a variable api_key_1 or directly inserting it into the code.

Dependend on your quota from the Youtube API, you have to run the code multiple times with single `channel_id`. Therefore the list channel_ids is stored with all related channels we sampled on.

### Code Requirements

Use pip install for the project requirements:

`pip install -r requirements.txt` 

Used Python Version: `Python3.11.1`



