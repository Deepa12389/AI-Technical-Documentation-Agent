
import streamlit as st
import ollama
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Technical Documentation Assistant",
    layout="wide"
)

st.title("AI Technical Documentation Assistant")
st.caption("Powered by Ollama and Llama 3.2")

mode = st.sidebar.radio(
    "Select a feature",
    [
        "Technical Document Generator",
        "PDF Question Answering"
    ]
)

def generate_response(prompt):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional technical writer. "
                    "Generate clear, structured technical content. "
                    "Do not invent technical specifications. "
                    "Identify missing information."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response["message"]["content"]


if mode == "Technical Document Generator":

    st.header("Generate Technical Documentation")

    doc_type = st.selectbox(
        "Document type",
        [
            "User Guide",
            "Installation Guide",
            "API Documentation",
            "Troubleshooting Guide",
            "Release Notes",
            "FAQ"
        ]
    )

    topic = st.text_input("Product name or topic")

    audience = st.selectbox(
        "Target audience",
        ["End Users", "Developers", "Administrators"]
    )

    details = st.text_area("Provide technical details")

    if st.button("Generate Document"):
        if topic.strip():
            prompt = f"""
            Create a {doc_type}.

            Product or topic: {topic}
            Target audience: {audience}
            Technical details: {details}

            Use appropriate headings, clear instructions,
            examples and prerequisites where applicable.
            Mark missing technical information for verification.
            """

            with st.spinner("Generating documentation..."):
                try:
                    result = generate_response(prompt)
                    st.markdown(result)
                except Exception as e:
                    st.error(str(e))
        else:
            st.warning("Enter a product name or topic.")


elif mode == "PDF Question Answering":

    st.header("Ask Questions About a PDF")

    uploaded_file = st.file_uploader(
        "Upload a PDF document",
        type=["pdf"]
    )

    if uploaded_file:
        reader = PdfReader(uploaded_file)

        document_text = ""

        for page in reader.pages:
            document_text += (page.extract_text() or "") + "\n"

        st.success("PDF uploaded successfully")

        question = st.text_input("Enter your question")

        if st.button("Generate Answer") and question.strip():

            prompt = f"""
            Answer the question using the document below.
            If the answer is unavailable, say so.

            Document:
            {document_text[:12000]}

            Question:
            {question}
            """

            with st.spinner("Generating answer..."):
                try:
                    result = generate_response(prompt)
                    st.markdown(result)
                except Exception as e:
                    st.error(str(e))

st.caption("AI-generated content requires technical verification.")
