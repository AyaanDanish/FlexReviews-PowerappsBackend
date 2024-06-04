# import nltk

# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# from nltk.corpus import stopwords

# from nltk.tokenize import word_tokenize

# from nltk.stem import WordNetLemmatizer


# # create preprocess_text function
# def preprocess_text(text):

#     # Tokenize the text

#     tokens = word_tokenize(text.lower())

#     # Remove stop words

#     filtered_tokens = [
#         token for token in tokens if token not in stopwords.words("english")
#     ]

#     # Lemmatize the tokens
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

#     # Join the tokens back into a string
#     processed_text = " ".join(lemmatized_tokens)

#     return processed_text


# # initialize NLTK sentiment analyzer

# analyzer = SentimentIntensityAnalyzer()


# # create get_sentiment function


# def get_sentiment(text):

#     scores = analyzer.polarity_scores(text)

#     max_sentiment = max(scores, key=scores.get)

#     sentiment_names = {"neu": "Neutral", "pos": "Positive", "neg": "Negative"}
#     return sentiment_names[max_sentiment]


# print(get_sentiment("hello"))

from profanity_check import predict, predict_prob

print(
    predict(
        [
            "predict() takes an array and returns a 1 for each string if it is offensive, else 0."
        ]
    )
)
# [0]

predict(["fuck you"])
# [1]

predict_prob(
    [
        "predict_prob() takes an array and returns the probability each string is offensive"
    ]
)
# [0.08686173]

predict_prob(["go to hell, you scum"])
# [0.7618861]
