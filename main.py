import streamlit as st
from transformers import pipeline

# Load models for text summarization and document question answering
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Streamlit app interface
st.set_page_config(page_title="RightBrothers", page_icon=":sparkles:")
st.title("RightBrothers")

# Display the logo
st.image("2.png", use_column_width=True)

# Option for text summarization
option = st.selectbox("Select an option:", ("Text Summarization", "Document Question Answering"))

if option == "Text Summarization":
    st.header("Text Summarization")
    text_input = st.text_area("Enter text to summarize:", height=200)
    if st.button("Summarize"):
        if text_input:
            summary = summarizer(text_input, max_length=150, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.write(summary[0]['summary_text'])
        else:
            st.warning("Please enter text to summarize.")

elif option == "Document Question Answering":
    st.header("Document Question Answering")
    doc_input = st.text_area("Enter the document text:", height=200)
    question_input = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if doc_input and question_input:
            answer = question_answerer(question=question_input, context=doc_input)
            st.subheader("Answer:")
            st.write(answer['answer'])
        else:
            st.warning("Please enter both the document and the question.")
