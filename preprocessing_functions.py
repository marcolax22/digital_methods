import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem.snowball import SnowballStemmer

# remove user names
def remove_users(data, column):
    data[column] = data[column].str.replace(r'@\w+ ', '', regex = True)
    return data

# Lowercase all tweet text
def lowercase_text(data, column):
    data[column] = data[column].str.lower()
    return data

# Remove numbers.
def remove_numbers(data, column):
    data[column] = data[column].str.replace(r'\d+', '', regex = True)
    return data

# Remove extra whitespace.
def remove_whitespace(data, column):
    data[column] = data[column].str.replace(r'\s+',' ', regex = True)
    return data

# Remove punctuation. 
def remove_punctuation(data, column):
    data[column] = data[column].str.translate(str.maketrans('', '', string.punctuation))
    return data

# Remove stopwords
def remove_stopwords(data, column):
    from nltk.corpus import stopwords
    stopword_match = r"\b(" + r"|".join(stopwords.words('english')) + r")\b"
    data[column] = data[column].str.replace(stopword_match, '', regex=True)
    return data

# Stem words
def stem_words(data, column):
    stemmer = SnowballStemmer(language='english')
    data['stemmed_text'] = data[column].apply(lambda x: " ".join([stemmer.stem(word) for word in word_tokenize(x)]))
    return data 

# Lemmatize words. (Hint: lemmatization requires part-of-speech tags)
def lemmatize_words(data, column):
    lemmatizer = WordNetLemmatizer()
    
    # Mapping NLTK POS tags to WordNet POS tags
    tag_map = {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'R': wordnet.ADV,
        'N': wordnet.NOUN
    }
    
    # Apply lemmatization to the specified column
    data['lemmatized_text'] = data[column].apply(lambda x: " ".join([
        lemmatizer.lemmatize(word, tag_map.get(tag[0], wordnet.NOUN)) 
        for word, tag in pos_tag(word_tokenize(x))
    ]))
    
    return data

# conver date format
def convert_date_format(df, column_name):
    # Convert the column to datetime
    df[column_name] = pd.to_datetime(df[column_name])
    
    # Format the dates back to 'dd mm yyyy' strings
    df[column_name] = df[column_name].dt.strftime('%Y-%m-%d')
    
    return df

#Defining a function that will create bigrams 
def bigrams(doc): 
    
    bigrams = [] 
    
    for bigram in list(nltk.bigrams(doc)): 
        bigrams.append("_".join(bigram))    
    
    return bigrams



