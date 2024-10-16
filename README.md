# Paragraph Analyzer

## Description

A comprehensive paragraph analyzer web application built using Python Flask that provides in-depth analysis of text. It counts words, letters, vowels, consonants, digits, symbols, and spaces, while also identifying unique words, uppercase, and lowercase letters. Additionally, it detects the most and least repeated characters. The application also features emotion detection using machine learning, analyzing the emotional tone of the text based on pre-trained models.

## Features

- Count words, letters, vowels, consonants, digits, symbols, and spaces
- Identify most and least repeated characters
- Detect uppercase and lowercase letters
- Extract unique words
- Detect emotional tone of the text using machine learning models
- Simple and user-friendly web interface

## Technologies Used

- Frontend: HTML, CSS
- Backend: Python Flask
- Machine Learning: scikit-learn, numpy, pandas
- Pre-trained emotion detection model

## Installation

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn, Numpy, Pandas
- Git (optional)

### Steps

1. **Clone the repository** (or download the zip file):

    ```bash
    git clone https://github.com/yourusername/paragraph-analyzer.git
    cd paragraph-analyzer
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app**:

    ```bash
    python app.py
    ```

4. **Open your browser** and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your browser.
2. Input a paragraph of text.
3. View the analysis, which includes:
   - Total word and letter counts
   - Breakdown of vowels and consonants
   - Most and least repeated characters
   - Uppercase, lowercase, and space counts
   - Unique words
   - Emotion detected from the text

## Machine Learning Model

The emotion detection is powered by machine learning models trained using scikit-learn. The models are stored in the following files:
- **Emotion Detector Model**: `static/models/emotion_detector.pkl`
- **Emotion Encoder**: `static/models/emotion_encoder.pkl`
- **Emotion Vectorizer**: `static/models/emotion_vectorizer.pkl`

## Project Structure
```
Paragraph-Analyzer/
│
├── static/
│   └── models/
│       ├── emotion_detector.pkl
│       ├── emotion_encoder.pkl
│       └── emotion_vectorizer.pkl
│   └── css/
│       └── styles.css
│
├── templates/
│   └── index.html
│
├── app.py
└── README.md
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure to follow the existing code style and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
