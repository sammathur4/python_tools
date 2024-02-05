import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


def summarize_journal(text, max_words=15):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    filtered_words = [
        word for word in words if word.isalnum() and word not in stop_words
    ]

    # Calculate word frequency distribution
    word_freq = FreqDist(filtered_words)

    # Get the 5 most common keywords
    relevant_keywords = [word for word, _ in word_freq.most_common(5)]

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Sort sentences by relevance (number of relevant keywords)
    sentences_with_relevance = [
        (
            sentence,
            sum(1 for keyword in relevant_keywords if keyword in sentence.lower()),
        )
        for sentence in sentences
    ]
    sentences_with_relevance.sort(key=lambda x: x[1], reverse=True)

    # Generate the summary
    summary = ""
    word_count = 0
    for sentence, _ in sentences_with_relevance:
        words_in_sentence = word_tokenize(sentence.lower())
        words_in_sentence = [
            word
            for word in words_in_sentence
            if word.isalnum() and word not in stop_words
        ]

        if len(words_in_sentence) + word_count <= max_words:
            summary += sentence + " "
            word_count += len(words_in_sentence)
        else:
            break

    return summary.strip()


# Example usage:
journal_text = "Your journal text goes here..."
summary = summarize_journal(journal_text)
print(summary)
