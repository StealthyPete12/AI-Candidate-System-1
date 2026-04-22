# AI Candidate Role Matcher

An ATS‑style application that analyzes a CV and ranks the top 3 most suitable technical roles using eligibility rules, skill normalization, and machine learning assisted scoring. 

---

## Live Demo

Try the application here:  
https://ai-candidate-system-1-34hyurh2hevdqdtzqtsjgl.streamlit.app/

---

## Project Overview

Most job‑matching demos rely on a single machine‑learning prediction to decide what role a candidate “is”.  
In reality, hiring decisions are way more complex:

- One CV can match multiple roles
- Some roles should be excluded if core requirements are missing
- Machine learning should act as a confluence, not the final authority
- Results should be ranked and explained 

This system produces a ranked list of the Top 3 Suitable Roles, with clear reasoning behind each recommendation.

---

## Key Features

- Upload CVs in PDF or DOCX format
- Skills extraction
- Eligibility gatingto exclude roles that arent suitable 
- Hybrid scoringcombining ML predictions with skill similarity
- Role ranking visualization
- Human‑readable explanationsfor each suggested role
- Seniority estimation (Junior / Mid / Senior)

---

## Design Philosophy

### From “Prediction Accuracy” to “Precision of Exclusion”

Instead of asking:

> “What job title does this CV belong to?”

the system asks:

> “Which roles are plausible for this CV, and how strong is the evidence for each?”

Accuracy is improved by:
- excluding roles that clearly do not fit
- ranking remaining roles by skills matched 
- avoiding overconfidence from limited or biased training data

---

## Eligibility Gating

Each role defines a set of non‑negotiable signals.

Examples:
- Data Analyst → SQL, BI tools, reporting
- DevOps Engineer → cloud, containers, CI/CD
- Frontend Engineer → JavaScript, UI frameworks

If these signals are missing, the role is excluded regardless of ML confidence.  
This should reduces false positives and increases result quality.

---

## Hybrid Scoring (ML + Skills)

Machine learning is used as a signal, not a decision boundary:

- When ML confidence is high, it contributes strongly
- When ML confidence is low or zero, skill overlap and frequency provide a fallback
- Plausible roles are never discarded solely due to sparse training data

This allows the system to handle hybrid and less common profiles gracefully.

---

## Skill Normalization & Weighting

- Skills are normalized to set rule names to avoid vocabulary mismatches
- Skills mentioned multiple times contribute more than one‑off mentions
- This helps distinguish genuine experience from keyword stuffing

---

## Seniority Detection

The system performs a lightweight seniority assessment using:
- responsibility related language
- experience indicators
- leadership and ownership signals

Output categories:
- Junior / Entry level
- Mid‑level
- Senior / Lead

This reflects how recruiters interpret CV context beyond job titles.

---

## Technology Stack

- Python
- Streamlit (UI & deployment)
- scikit‑learn (machine learning)
- joblib (model persistence)
- pdfplumber / python‑docx (CV parsing)
- pandas / numpy (data processing)

---

## Limitations

- The training dataset is intentionally small and illustrative
- Skill extraction is rule‑based and relies on specific skills 
- Eligibility rules and scoring weights are a rule of thumb 

---

## Summary

This project is not a job title decision maker.

It is a decision‑support system that:
- filters out irrelevant roles
- ranks valid ones
- explains every recommendation
