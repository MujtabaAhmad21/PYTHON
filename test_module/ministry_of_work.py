from textblob import TextBlob
import pyttsx3
import art

print(art.text2art("MINISTRY OF WORK"))

def get_polarity(quote):
    return TextBlob(quote).sentiment.polarity  # Extract the polarity value

engine = pyttsx3.init()
engine.say("What's up, Mujtaba! Enter a statement so we can analyze its sentiment.")
engine.runAndWait()

print("Enter your employee wellness statement: ")
phrase = input("> ")
blob = TextBlob(phrase)

while get_polarity(phrase) < 0.5:
    print("The sentiment is negative. Please try again.")
    phrase = input("> ")  # Get a new statement

print("Sentiment analysis result:", blob.sentiment)