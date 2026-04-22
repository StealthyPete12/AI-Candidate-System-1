import os
import joblib
import numpy as np

#This is used for extracting text and skills from the cv 

from cv_parser import extract_text_from_cv
from skill_extractor import extract_skills_from_text

#This is telling the script to run no matter where it is being executed 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#This was used for offline testing 

CV_PATH = os.path.join(BASE_DIR, "data", "my_cv.pdf")

#This was using the trained classified model

MODEL_PATH = os.path.join(BASE_DIR, "results", "candidate_classifier.pkl")

#This is was used as the multi-label encoder for the skills 

ENCODER_PATH = os.path.join(BASE_DIR, "results", "skill_encoder.pkl")

#This to to load the trained model and the other relevant encoders 

model = joblib.load(MODEL_PATH)
mlb = joblib.load(ENCODER_PATH)

#This is extracting the text from the PDF CV and list the extracted technical skills

text = extract_text_from_cv(CV_PATH)
skills = extract_skills_from_text(text)

#This is extracting the skills and running them against the set trained classification
#Predicting the most accurate position and then predicting its confidence scores 

encoded = mlb.transform([skills])
prediction = model.predict(encoded)[0]
confidence = float(np.max(model.predict_proba(encoded)[0]))

#This is just showing the output results 
print("==== AI CLASSIFICATION RESULT ====")
print({
    "extracted_skills": skills,
    "predicted_role": prediction,
    "confidence_score": round(confidence, 3)
})