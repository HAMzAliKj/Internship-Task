from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from operator import itemgetter


# Define the model name from Hugging Face
model_name = "BAAI/bge-small-en-v1.5"
embeddings = HuggingFaceEmbeddings(model_name=model_name)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key="PASTE YOUR API KEY")

# Initialize loader
loader = PyPDFLoader("D:\\Hamza Ali\\Internship Task\\hamza cv pdf.pdf")

# Load pages into document objects
pages = loader.load()

text_spitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100)
docs = text_spitter.split_documents(pages)


db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="chroma_db"
)


retriever = db.as_retriever(search_kwargs={"k": 3})
prompt = PromptTemplate.from_template("You are a RAG chatbot. You are given the following extracted parts of a long document and a question. Provide a conversational answer based on the context provided. If you can't find the answer in the context below, just say 'Hmm, I'm not sure.' Don't try to make up an answer. Context: {context} Question: {question}")

qf = itemgetter("question")

setup = {
    "question": qf,
    "context": qf | retriever 
}

chain = setup | prompt | llm 

# chain = retriever | prompt | llm
print(chain.invoke({"question": "What is the name of the person in the CV?"}).content)
print(chain.invoke({"question": "What is the email address of the person?"}).content)
print(chain.invoke({"question": "What are the main skills listed in the CV?"}).content)
print(chain.invoke({"question": "What is the work experience mentioned in the CV?"}).content)
print(chain.invoke({"question": "What educational qualifications does the person have?"}).content)
print(chain.invoke({"question": "What projects has the person worked on?"}).content)
