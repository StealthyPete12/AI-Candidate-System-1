import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report, accuracy_score

#This section defines all file and directory paths used by the training model 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(RESULTS_DIR, exist_ok=True)

#This part loads the training dataset containing the CV samples and their associated role labels

df = pd.read_csv(os.path.join(DATA_DIR, "sample_candidates.csv"))

df["skills"] = df["skills"].apply(lambda x: x.split(","))

#This is focused on transforming raw data into a numerical value so that the machine learning model can work with

mlb = MultiLabelBinarizer()
X = pd.DataFrame(mlb.fit_transform(df["skills"]), columns=mlb.classes_)
y = df["target_role"]

#This part splits training and tests sets 

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

#This section defines and trains the machine learning model using the prepared features.

model = DecisionTreeClassifier(
    max_depth=5,
    criterion="gini",
    random_state=42
)

model.fit(X_train, y_train)

#Once the model has been trained it then evaluates using the test set to understand how well it performs on unseen data

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

#This is just to ensure everything is saved 

joblib.dump(model, os.path.join(RESULTS_DIR, "candidate_classifier.pkl"))
joblib.dump(mlb, os.path.join(RESULTS_DIR, "skill_encoder.pkl"))

with open(os.path.join(RESULTS_DIR, "classification_report.txt"), "w") as f:
    f.write(f"Accuracy: {accuracy:.3f}\n\n")
    f.write(report)

print("Training complete")
print(f"Accuracy: {accuracy:.3f}")