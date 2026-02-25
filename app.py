
import streamlit as st
import PyPDF2
import spacy
import re

import spacy
nlp = spacy.blank("en")

st.title("ResumeIQ - Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("Extracted Text")
    st.write(text)

    doc = nlp(text)

    word_count = len([token for token in doc if token.is_alpha])
    sentence_count = len(list(doc.sents))
    st.subheader("Basic Analysis")
    st.write("Total Words:", word_count)
    st.write("Total Sentences:", sentence_count)

    email = re.findall(r'\S+@\S+', text)
    st.write("Email Found:", email if email else "Not found")

    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    st.write("Phone Number Found:", phone if phone else "Not found")

    skills_list = ["Python", "Java", "C++", "Machine Learning", "Data Analysis", "SQL", "HTML", "CSS"]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]

    st.subheader("Detected Skills")
    st.write(found_skills if found_skills else "No predefined skills detected")

    score = 0

    if word_count > 300:
        score += 1
    if email:
        score += 1
    if phone:
        score += 1
    if found_skills:
        score += 1

    st.subheader("Resume Strength Score (0-4)")
    st.write(score)