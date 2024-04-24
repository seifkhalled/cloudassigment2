import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def count_stopword_frequency(text):
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    stopword_freq = Counter(word for word in words if word in stop_words)
    return stopword_freq

def main():
    filename = "paragraphs.txt"  
    text = read_file(filename)

    stopword_freq = count_stopword_frequency(text)

    print("Stopword Frequency Count:")
    for word, freq in stopword_freq.most_common():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
