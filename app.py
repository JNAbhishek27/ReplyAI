import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("emails.csv")

# Categorize (if not already labeled)
def label_email(subject, body):
    text = (str(subject) + " " + str(body)).lower()
    if "billing" in text or "pricing" in text or "refund" in text:
        return "Billing Issue"
    elif "login" in text or "password" in text or "access" in text or "verification" in text:
        return "Login/Access Issue"
    elif "down" in text or "critical" in text or "urgent" in text:
        return "Downtime Issue"
    elif "integration" in text or "api" in text or "crm" in text:
        return "Integration Query"
    else:
        return "General Query"

if "Category" not in df.columns:
    df["Category"] = df.apply(lambda x: label_email(x["subject"], x["body"]), axis=1)

# Streamlit UI
st.title("📧 AI-Powered Email Assistant")
st.write("Prototype dashboard to manage support emails")

st.subheader("All Emails")
st.dataframe(df[["sender","subject","sent_date","Category"]])

# Analytics
st.subheader("Analytics")
category_counts = df["Category"].value_counts()

fig, ax = plt.subplots()
sns.barplot(x=category_counts.index, y=category_counts.values, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Sample AI Response (demo only)
st.subheader("AI Draft Response")
sample = df.iloc[0]
st.write(f"**Incoming Mail**: {sample['subject']}")
st.write(f"**AI Draft Reply**: Hello {sample['sender'].split('@')[0]}, thanks for reaching out regarding *{sample['Category']}*. Our support team is already working on it and will get back to you shortly.")
