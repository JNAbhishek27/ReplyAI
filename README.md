# ReplyAI - Smart Email Categorization & Reply Assistant

## Overview
ReplyAI is an AI-powered tool that reads incoming emails, categorizes them 
(Work, Personal, Spam, etc.), and suggests smart replies.  
It uses NLP + ML models and has a user-friendly Streamlit dashboard.

## Files
- `app.py` → Streamlit app  
- `emails.csv` → Sample dataset  
- `notebook.ipynb` → Colab notebook (training + preprocessing pipeline)  
- `requirements.txt` → Dependencies  

## Run Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
