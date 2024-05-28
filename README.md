# Digital Methods - Data Collection

**Table of Content:**

1. [Project](#project)
2. [Data Collection](#data-collection)
3. [Data Analysis](#data-analysis)
4. [API Key](#api-key)
5. [Code Requirements](#code-requirements)
6. [Code Book](#code-book)

## Project

This repository is related to the Exam **Digital Methods** at the **University of Copenhagen** for the Masters degree **Social Data Science**. The undelying project aims to explore Climate Contrarian Narratives.

The project includes the code, qualitative and quantative data, as well as the documentation.

## Data Collection

- The process and code of the data collection can be found in the script `data-collection.ipynb`.

- The list of sampled channels can be found [here](data/channel_sampling.xlsx).
    - The related Codebook can be found in the following section: [Code Book](#code-book).

## Data Analysis

The Data Analysis is staged into different parts.

1. Explorative Sampling of the Comments. Through the sampling function of the script `sampling-open-coding.ipynb`.
2. Focused anaylsis of the comments with the help of the keywords which were identified through topic modeling in the script `topic-modelling.ipynb`. Furthermore keywords were found through the word2vec model in the script `Word2vec.ipynb`.
3. The final classifier of the comments can be found in the script ``.

The script `preprocessing_functions.py` includes functions which where used in the different scripts. Each functions is descript in the file.

## Immersion Journal

The Immersion Journal captures the comments from the focused and open Coding approach used in this study. The Immersion Journal can be found [here](#immersion-journal).

- The related Codebook can be found in the following section: [Code Book](#code-book).

## API Key

To run the code and get YouTube comments, you have to get an API key for YouTube. The explanation to create a key, you can finde [here](https://developers.google.com/youtube/v3/getting-started#before-you-start).

The Script `data-collection.ipynb` will ask you for the API key. You can read it in with creating a `api_key.py` file and store it as a variable api_key_1 or directly inserting it into the code.

Dependend on your quota from the Youtube API, you have to run the code multiple times with single `channel_id`. Therefore the list channel_ids is stored with all related channels we sampled on.

## Code Requirements

Use pip install for the project requirements:

`pip install -r requirements.txt` 

Used Python Version: `Python3.11.1`

## Code Book

- Find the Codebook for the Channel Sampling [here](documentation/codebook_sampling.md).
- Find the Codebook for the Immersion Journal [here](documentation/codebook_immersion-journal.md).



