from text_analyzer import tokenize, most_frequent_words, remove_stopwords, analyze_text


def test_tokenize_lowercase():
    assert tokenize("Кот, пёс") == ["кот", "пёс"]


def test_tokenize_empty_string():
    assert tokenize("") == []


def test_most_frequent_words_tie():
    assert most_frequent_words(["кот", "пёс", "кот", "пёс", "мышь"]) == ["кот", "пёс"]


def test_most_frequent_words_empty():
    assert most_frequent_words([]) == []


def test_remove_stopwords():
    assert remove_stopwords(["кот", "и", "пёс", "на", "крыше"], {"и", "на"}) == ["кот","пёс", "крыше"]


def test_analyze_text_min_length():
    result = analyze_text("Программирование помогает понимать язык", min_length=10)
    assert result["long_word_count"] == 1
    assert result["word_count"] == 4
    

def test_analyze_text_empty():
    result = analyze_text("")
    assert result["avg_word_length"] == 0.0
    assert result["word_count"] == 0


def test_analyze_text_with_stopwords():
    result = analyze_text("Кот и пёс, и ещё кот!", stopwords={"и"})
    assert result["word_count"] == 4


    

    
