from flask import Flask, request, render_template
import joblib
import PyPDF2
import io

app = Flask(__name__)

# Load your trained ML model
model = joblib.load("resume_match_model.pkl")

# Function to extract text from PDF
def extract_text_from_pdf(file_storage):
    reader = PyPDF2.PdfReader(file_storage)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    resume_text = request.form.get("resume", "").strip()
    jd_text = request.form.get("jd", "").strip()

    # Handle Resume File Upload
    resume_file = request.files.get("resume_file")
    if resume_file and resume_file.filename:
        if resume_file.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        elif resume_file.filename.endswith(".txt"):
            resume_text = resume_file.read().decode("utf-8")

    # Handle Job Description File Upload
    jd_file = request.files.get("jd_file")
    if jd_file and jd_file.filename:
        if jd_file.filename.endswith(".pdf"):
            jd_text = extract_text_from_pdf(jd_file)
        elif jd_file.filename.endswith(".txt"):
            jd_text = jd_file.read().decode("utf-8")

    # Only predict if both texts are present
    if resume_text and jd_text:
        combined_text = resume_text + " " + jd_text
        result = model.predict([combined_text])[0]
        prediction = "Match" if result == 1 else "Not a Match"
    else:
        prediction = "Please provide both Resume and Job Description (either by text or file upload)."

    return render_template("index.html", prediction=prediction, request=request)

if __name__ == "__main__":
    app.run(debug=True)
