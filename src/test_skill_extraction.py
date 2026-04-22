from cv_parser import extract_text_from_cv
from skill_extractor import extract_skills_from_text
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CV_PATH = os.path.join(BASE_DIR, "data", "my_cv.pdf")

text = extract_text_from_cv(CV_PATH)
skills = extract_skills_from_text(text)

print("==== EXTRACTED SKILLS ====")
print(skills)