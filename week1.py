from collections import Counter
from pathlib import Path
import re


def clean_text(text):
    """Normalize text and return its alphanumeric tokens separated by spaces."""
    words = re.findall(r"[^\W_]+", text.casefold())
    return " ".join(words)


def analyze_text(text=None, min_length=5):
    """Count tokens and long tokens, and find a unique most frequent token.

    Read text.txt when text is omitted. The most frequent word is None when
    there is no unique most frequent word or the text contains no tokens.
    """
    if text is None:
        file_path = Path(__file__).with_name("text.txt")
        text = file_path.read_text(encoding="utf-8")

    words = clean_text(text).split()
    long_word_count = sum(1 for word in words if len(word) >= min_length)
    frequency = Counter(words)
    most_common = frequency.most_common(2)
    if not most_common or (
        len(most_common) > 1 and most_common[0][1] == most_common[1][1]
    ):
        most_frequent_word = None
    else:
        most_frequent_word = most_common[0][0]

    return {
        "word_count": len(words),
        "long_word_count": long_word_count,
        "most_frequent_word": most_frequent_word,
    }


if __name__ == "__main__":
    assert clean_text("Привет, мир! (тест) «кавычки» — dash...") == (
        "привет мир тест кавычки dash"
    )
    assert analyze_text("cat cat dog") == {
        "word_count": 3,
        "long_word_count": 0,
        "most_frequent_word": "cat",
    }
    assert analyze_text("I study Python every day") == {
        "word_count": 5,
        "long_word_count": 3,
        "most_frequent_word": None,
    }
    assert analyze_text("extraordinary cat", min_length=12) == {
        "word_count": 2,
        "long_word_count": 1,
        "most_frequent_word": None,
    }
    assert analyze_text("   ") == {
        "word_count": 0,
        "long_word_count": 0,
        "most_frequent_word": None,
    }
