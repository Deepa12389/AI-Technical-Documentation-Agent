# AI Technical Documentation Assistant

An AI-powered application designed to assist technical writers in generating structured technical documentation and extracting information from existing PDF documents.

## Features

- User guide generation
- Installation guide generation
- API documentation generation
- Troubleshooting guide generation
- Release notes and FAQ generation
- PDF-based question-answering
- Local LLM integration without paid API dependencies

## Technology Stack

- Python
- Streamlit
- Ollama
- Llama 3.2
- PyPDF

## Application Workflow

User Input → Streamlit Interface → Python Processing → Ollama → Llama 3.2 → Generated Documentation

## Installation

1. Install Python and Ollama.
2. Download the Llama 3.2 model using `ollama pull llama3.2`.
3. Clone this repository.
4. Install dependencies using `pip install -r requirements.txt`.
5. Launch the application using `streamlit run app.py`.

## Future Enhancements

- Retrieval-Augmented Generation (RAG)
- Vector embeddings and semantic search
- Word and Markdown export
- Documentation quality validation
- Source citations

## About the Project

Developed by a technical writer with 12+ years of professional documentation experience to explore practical applications of generative AI in technical communication.

AI-generated documentation requires technical review and validation before publication.