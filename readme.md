# NLP Learning

My learning path towards NLP / Machine Learning engineering.
Each week I build a small project and improve it step by step.

## Week 1: Mini Text Analyzer

Counts the words and long words in a text, and finds the most frequent word if there is only one.

## Week 2: Text Analyzer with Tests

Analyzes a text: splits it into words, removes stop words and calculates
word statistics. All functions are covered by pytest tests.

### Functions

- `tokenize` — finds words in the text and converts them to lowercase, ignoring punctuation.
- `most_frequent_words` — finds all words that occur more often than the others. If several words are tied, it returns them in alphabetical order.
- `load_stopwords` — loads stop words from a file into a set (e.g. "and", "the").
- `remove_stopwords` — removes words marked as unimportant from a list while keeping the remaining words in their original order.
- `analyze_text` — analyzes the text: counts all and unique words, finds long words, calculates the average word length, and lists the most frequent words. It can also exclude stop words.

## How to Run the Tests

```bash
pip install pytest
python -m pytest week2
```

## What I Learned

- How to split text into words and process them regardless of capitalization and punctuation.
- How to count word frequency and find words that occur equally often.
- How to use a list of stop words to exclude them from analysis.
- How to collect several text statistics and check a program with automated tests.
- Regular expressions (`re`), `collections.Counter`, sets
- Writing tests with `pytest`
- Version control with `git` and GitHub