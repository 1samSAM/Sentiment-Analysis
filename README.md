
# Simple Sentiment Analysis Program

This repository contains a **Simple Python Program for Sentiment Analysis** using the `transformers` library by Hugging Face. The program performs real-time sentiment analysis on user input text and determines whether the sentiment is positive, negative, or neutral with a confidence score.

---

## Features

- Real-time sentiment analysis.
- Easy-to-use command-line interface.
- Uses pre-trained models from Hugging Face's `transformers` library for accurate results.
- Displays the sentiment label and confidence score for the analyzed text.

---

## Prerequisites

- Python 3.8 or higher.
- Install the Hugging Face `transformers` library:
  ```bash
  pip install transformers
  ```


---

## Installation and Usage

1. Clone this repository to your local machine:
```
git clone <repository_url>
cd <repository_name>
```

2. Install the required dependencies:

pip install transformers


3. Run the program:

python sentiment_analysis.py


4. Enter your text when prompted. Type exit to quit the program.




---

## How It Works

1. Pipeline Initialization:
The pipeline method from Hugging Face's transformers library is used to create a sentiment analysis pipeline. It automatically loads a pre-trained sentiment analysis model.


2. Real-Time Input:
The program takes real-time text input from the user in a loop until the user types exit.


3. Sentiment Analysis:
The user's input is passed to the sentiment analysis pipeline, which returns:

The sentiment label (POSITIVE or NEGATIVE).

The confidence score for the result.



4. Output:
The program displays the sentiment and confidence score in a readable format.




---

## Example Usage

Real-Time Sentiment Analysis
Type 'exit' to quit.

Enter your text: I love this product!
Sentiment: POSITIVE
Confidence Score: 0.99

Enter your text: This is terrible.
Sentiment: NEGATIVE
Confidence Score: 0.98

Enter your text: exit
Exiting...


---

## File Structure
```
.
├── sentiment_analysis.py   # Main Python script for sentiment analysis
└── README.md               # Documentation file
```

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as per the license terms.


---

Enjoy coding and exploring the world of NLP with Transformers!

You can save this content as `README.md` in your GitHub repository. Replace `<repository_url>` and `<repository_name>` with the actual details of your repository.

