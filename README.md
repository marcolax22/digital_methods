# Digital Methods - Data Collection

**Table of Content:**

1. [Data Collection](#data-collection)
2. [API Key](#api-key)
3. [Code Requirements](#code-requirements)
4. [Code Book](#code-book)

## Data Collection


## API Key

To run the code and get YouTube comments, you have to get an API key for YouTube. The explanation to create a key, you can finde [here](https://developers.google.com/youtube/v3/getting-started#before-you-start).

The Script `data-collection.ipynb` will ask you for the API key. You can read it in with creating a `api_key.py` file and store it as a variable api_key_1 or directly inserting it into the code.

Dependend on your quota from the Youtube API, you have to run the code multiple times with single `channel_id`. Therefore the list channel_ids is stored with all related channels we sampled on.

## Code Requirements

Use pip install for the project requirements:

`pip install -r requirements.txt` 

Python Version: `Python3.11.1`

## Code Book

- Find the Codebook for the Channel Sampling [here](documentation/codebook_sampling.md).
- Find the Codebook for the Immersion Journal [here](documentation/codebook_immersion-journal.md).



