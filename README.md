# Natural Language Processing (NLP) Pipeline using NLTK Basics

## Overview
This project demonstrates a Natural Language Processing (NLP) pipeline using the Natural Language Toolkit (NLTK) in Python. The script performs various text-processing tasks on a given passage about monarchs. The main steps include:

1. **Segmentation** - Splitting text into sentences.
2. **Tokenization** - Breaking down sentences into words.
3. **Stop Words Removal** - Eliminating common, non-informative words.
4. **Stemming** - Reducing words to their root form.
5. **Lemmatization** - Converting words to their base or dictionary form.
6. **Part-of-Speech (POS) Tagging** - Identifying the grammatical category of words.
7. **Named Entity Recognition (NER)** - Detecting proper nouns and entities in the text.

## Prerequisites
Ensure you have Python installed along with the required NLTK package. Before running the script, uncomment and execute the necessary downloads for NLTK datasets.

## Installation

```bash
pip install nltk
pip install numpy
```

## Required Downloads (Uncomment in the script before running)
```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
```

## Execution Steps
1. **Text Segmentation**
   - Uses `sent_tokenize()` to break text into sentences.
   
2. **Punctuation Removal**
   - Utilizes regular expressions to remove non-alphanumeric characters.

3. **Tokenization**
   - `word_tokenize()` splits text into individual words.

4. **Stop Words Removal**
   - Uses `stopwords.words("english")` to filter out common words.

5. **Stemming**
   - `PorterStemmer().stem()` reduces words to their root form.

6. **Lemmatization**
   - `WordNetLemmatizer().lemmatize()` converts words to their dictionary base form.

7. **Part-of-Speech Tagging**
   - `pos_tag()` assigns grammatical categories to words.

8. **Named Entity Recognition (NER)**
   - `ne_chunk()` identifies named entities such as people, places, and organizations.

## Example Output
The script processes a given text passage and provides outputs for each step, such as filtered words, stems, lemmas, POS tags, and identified named entities.

## License
This project is open-source and can be used freely for educational and research purposes.

## Author
@AryanNaik24 on github

