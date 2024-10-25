import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

def extract_text_from_pdf(pdf_file):
    # Open the PDF file
    document = fitz.open(pdf_file)
    text = ""
    for page in document:
        text += page.get_text()
    return text

def summarize_text(text):
    # Summarize the text
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Streamlit app layout
st.title("PDF Text Extractor and Summarizer")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the PDF
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.write(text)

    # Summarize the text
    if st.button("Summarize Text"):
        if text:
            summary = summarize_text(text)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("No text found to summarize.")
