from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity_percentage = sentiment.polarity * 100
    subjectivity_percentage = sentiment.subjectivity * 100

    sentiment_label = 'positive' if sentiment.polarity > 0 else 'negative' if sentiment.polarity < 0 else 'neutral'

    return sentiment_label, polarity_percentage, subjectivity_percentage

def on_analyze():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        sentiment_label, polarity, subjectivity = analyze_sentiment(text)
        messagebox.showinfo("Sentiment Analysis Result", 
                            f"Sentiment: {sentiment_label}\nPolarity: {polarity}%\nSubjectivity: {subjectivity}%")
    else:
        messagebox.showwarning("Input Error", "Please enter some text to analyze.")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis with TextBlob")

# Create a text input area
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Create an analyze button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=on_analyze)
analyze_button.pack(pady=5)

# Run the application
root.mainloop()