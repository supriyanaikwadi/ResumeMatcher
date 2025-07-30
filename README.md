# ResumeMatcher

'ResumeMatcher' is a simple web application that matches resumes to job descriptions using natural language processing (NLP). It helps recruiters quickly identify how well a candidate’s resume aligns with a job posting.

## Features

- Upload and analyze resumes
- Match resumes to job descriptions
- Scores candidates based on relevance
- Simple web interface using Flask
- Pretrained model for matching logic

## Tech Stack

- Python
- Flask – Web framework
- scikit-learn – Machine learning
- NLTK / SpaCy – NLP processing (if applicable)
- HTML/CSS – Frontend

## Project Structure

```
ResumeMatcher/
├── app.py                    # Main Flask app
├── index (1).html            # Frontend interface
├── model.py                  # Logic for matching resumes
├── resume_match_model.pkl    # Pre-trained matching model
└── README.md                 # Project documentation
```

##  How It Works

1. The user uploads a resume and provides a job description.
2. The backend processes both using NLP techniques.
3. A similarity score is calculated using the pre-trained model.
4. The result is displayed on the web interface.

##  Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository or unzip the project folder.
2. Navigate to the project directory:

   ```bash
   cd ResumeMatcher
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Open your browser and visit `http://127.0.0.1:5000`

##  Model

The file `resume_match_model.pkl` is a serialized machine learning model trained to compute the similarity between resumes and job descriptions.

##  To Do

- Add support for multiple resume uploads
- Improve UI with better frontend design
- Use advanced NLP models (like BERT or spaCy)
- Add unit testing

