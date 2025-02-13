#Note: To run the code first uncomment all the nltk.download()s

# All the steps
# 1] segmentation 
# 2] Tokenisation
# 3] Stop Words Removal
# 4] stemming
# 4] Lemmatation
# 5] Part of Speech Tagging
# 6] Name Entity Recognition

# Uncomment these before running the code --------------------------------------------------------------->


# nltk.download("punkt_tab")
# nltk.download("punkt")
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')

#<---Till here ------------------------------------------------------------------------------------------>
import nltk
from nltk.tokenize import sent_tokenize
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
from nltk import ne_chunk

text = "King is the title given to a male monarch in a variety of contexts. A king is an absolute monarch if he holds the powers of government without control, or the entire sovereignty over a nation; he is a limited monarch if his power is restrained by fixed laws; and he is an absolute, when he holds the whole legislative, judicial, and executive power, or when the legislative or judicial powers, or both, are vested in other people by the king. Kings are hereditary sovereigns when they hold the powers of government by right of birth or inheritance, and elective when raised to the throne by choice."

# Segmentation karpak
#split text into sentences 
sentences = sent_tokenize(text)
print(sentences)
print("-------------------------------------------------")

#punctuations remove
upText = re.sub(r"[^a-zA-Z0-9]"," ",sentences[2])
print(upText)
print("-------------------------------------------------")

# Tokenisation
words = word_tokenize(upText)
print(words)
print("-------------------------------------------------")

# Stopword removal
words = [w for w in words if w not in stopwords.words("english")]
print (words)
print("-------------------------------------------------")


# Stemming and Lemmatization
    #stemming
stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)
print("-------------------------------------------------")
    #lemmatize
lemmatized = [WordNetLemmatizer().lemmatize(w) for w in words ]
print(lemmatized)
print("-------------------------------------------------")

# Speech Tagging
print(pos_tag(words))
print("-------------------------------------------------")

#Named Entity Recognition
ner_tree = ne_chunk(pos_tag(word_tokenize(text)))
print(ner_tree)
print("-------------------------------------------------")



