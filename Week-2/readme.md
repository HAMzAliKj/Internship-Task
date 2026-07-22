
# 📄 Mini RAG Chatbot using LangChain + Gemini

A simple Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **Google Gemini**, **Hugging Face Embeddings**, and **Chroma Vector Database**. The chatbot loads a PDF document, splits it into chunks, creates embeddings, stores them in a vector database, and answers user questions based only on the document's content.

---

## 🚀 Features

* Load PDF documents
* Split text into smaller chunks
* Generate embeddings using Hugging Face
* Store embeddings in Chroma Vector Database
* Retrieve the most relevant document chunks
* Answer questions using Google Gemini
* Prevents hallucinations by answering only from the provided document

---

## 🛠️ Technologies Used

* Python
* LangChain
* Google Gemini
* Hugging Face Embeddings (BAAI/bge-small-en-v1.5)
* Chroma
* PyPDFLoader

---

## 📁 Project Structure

```text
.
├── rag_mini_chatbot.py
├── hamza cv pdf.pdf
├── chroma_db/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv env
env\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file (recommended) or set your Google Gemini API key as an environment variable.

Example:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

Do **not** hardcode your API key in the source code.

---

## ▶️ Run the Project

```bash
python rag_mini_chatbot.py
```

Example question:

```text
What is the name of the person in the CV?
```

---

## 🔄 How It Works

1. Load the PDF using `PyPDFLoader`.
2. Split the document into smaller chunks.
3. Generate embeddings using Hugging Face.
4. Store embeddings in Chroma.
5. Retrieve the most relevant chunks for the user's question.
6. Send the retrieved context to Google Gemini.
7. Return an answer based only on the document.

---

## 📌 Notes

* This project uses **Retrieval-Augmented Generation (RAG)**.
* Chroma is used instead of FAISS because it is compatible with newer Python versions.
* The chatbot answers only from the uploaded document.

---

## 📦 Requirements

* Python 3.10+
* Google Gemini API Key
* Internet connection (for Gemini and initial model download)

---

## 📄 License

This project is licensed under the MIT License.
