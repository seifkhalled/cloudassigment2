import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def count_stopword_frequency(text):
    stop_words = set(stopwords.words('english'))
    # Remove punctuation and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Count only the stop words
    stopword_freq = Counter(word for word in words if word in stop_words)
    return stopword_freq

def main():
    # Read the contents of the file
    filename = "paragraphs.txt"  
    text = read_file(filename)

    # Count stop word frequency
    stopword_freq = count_stopword_frequency(text)

    # Display stop word frequency count
    print("Stopword Frequency Count:")
    for word, freq in stopword_freq.most_common():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
