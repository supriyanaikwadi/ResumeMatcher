import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

data = [
    ["Python developer with 3 years of experience", "Python backend developer", 1],
    ["Sales executive with client handling skills", "Backend developer with Python", 0],
    ["Data Scientist with NLP and ML experience", "NLP ML engineer", 1],
    ["Digital marketer, SEO expert", "NLP ML engineer", 0]
]

df = pd.DataFrame(data, columns=["resume", "jd", "label"])
df["combined"] = df["resume"] + " " + df["jd"]

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

pipeline.fit(df["combined"], df["label"])
joblib.dump(pipeline, "resume_match_model.pkl")
print("Model trained and saved.")
