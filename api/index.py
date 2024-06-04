from flask import Flask, jsonify, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from profanity_check import predict, predict_prob

nltk.data.path.append("/var/task/api/nltk_data/")


app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Join the tokens back into a string
    processed_text = " ".join(lemmatized_tokens)
    return processed_text


# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    max_sentiment = max(scores, key=scores.get)
    sentiment_names = {"neu": "Neutral", "pos": "Positive", "neg": "Negative"}
    return sentiment_names[max_sentiment]


@app.route("/sentiment", methods=["POST"])
def sentiment():
    text = request.json.get("text")
    sentiment_result = get_sentiment(text)
    return jsonify({"sentiment": sentiment_result})


# def check_profanity(text):
#     profanity_result = predict([text])[0]
#     return "Inappropriate" if profanity_result == 1 else "Appropriate"


# @app.route("/profanity", methods=["POST"])
# def profanity():
#     text = request.json.get("text")
#     profanity_result = check_profanity(text)
#     return jsonify({"profanity": profanity_result})
