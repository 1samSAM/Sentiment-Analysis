from transformers import pipeline


# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(user_input):
    """
    Analyze the sentiment of the user's input text.
    Args:
        user_input (str): The input text to analyze.
    Returns:
        dict: Sentiment analysis results.
    """
    result = sentiment_analyzer(user_input)
    return result[0]  # Return the first result

# Example usage: Real-time input
print("Real-Time Sentiment Analysis")
print("Type 'exit' to quit.")

while True:
    # Take input from the user
    user_text = input("\nEnter your text: ")
    if user_text.lower() == "exit":
        print("Exiting...")
        break

    # Perform sentiment analysis
    sentiment_result = analyze_sentiment(user_text)

    # Display the result
    print(f"Sentiment: {sentiment_result['label']}")
    print(f"Confidence Score: {sentiment_result['score']:.2f}")