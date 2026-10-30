import re
from collections import Counter
from pathlib import Path


def tokenize(text): #Сортивка и списки слов
    """Return a list of alphanumeric tokens in the text, normalized to Lowercase."""
    return re.findall(r"[^\W_]+", text.casefold())


def load_stopwords(path):
    """Return a set of stop words read from a file, one word per line."""
    return {
        line.strip().casefold()
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def most_frequent_words(words):
    counts = Counter(words)
    if not counts:
        return []
    top = max(counts.values())
    result = []
    for word, count in counts.items():
        if count == top:
            result.append(word)
    return sorted(result)


def remove_stopwords(words, stopwords):
    """Return words without stopwords."""
    result = []
    for word in words:
        if word not in stopwords:
            result.append(word)
    return result


def analyze_text(text, min_length=5, top_n=3, stopwords = None): #ПРОЕКТ NLP/ML
    """Return statistics about the word in the text"""
    words = tokenize(text)
    if stopwords:
        words = remove_stopwords(words, stopwords)
    long_count = 0
    total_letters = 0
    for word in words:
        total_letters += len(word)
        if len(word) >= min_length:
            long_count += 1
    avg_word_length = 0.0
    if words:
        avg_word_length = total_letters / len(words)
    return { # return на уровне тела функции
        "word_count": len(words),   
        "unique_word_count": len(set(words)),
        "long_word_count": long_count,  
        "avg_word_length": round(avg_word_length, 2),
        "top_words": Counter(words).most_common(top_n),
        "most_frequent": most_frequent_words(words)
        } 

    


if __name__ == "__main__":
    print(tokenize("привет, мир!"))
    print(most_frequent_words(["кот", "пёс", "кот", "пёс", "мышь"]))
    print(most_frequent_words(["я", "люблю", "python"]))
    stopwords_path = Path(__file__).with_name("stopwords.txt")
    stopwords = load_stopwords(stopwords_path)
    print(remove_stopwords(["кот", "и", "пёс", "на", "крыше"], stopwords))
    print(analyze_text("Кот и пёс, и ещё кот!"))
    print(analyze_text("Программирование помогает понимать язык"))
    print(analyze_text("Программирование помогает понимать язык", min_length=10))
    print(analyze_text(""))
    print(analyze_text("Кот и пёс, и ещё кот!", stopwords=stopwords))