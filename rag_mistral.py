import pandas as pd

# RAG Components
from langchain_community.document_loaders import PyPDFLoader           # Load Docs
from langchain_text_splitters import RecursiveCharacterTextSplitter     # Chunking
from langchain_huggingface import HuggingFaceEmbeddings                 # Embeddings (Updated Import)
from langchain_community.vectorstores import FAISS                      # Vector Store (FAISS)
from langchain_ollama import OllamaLLM                                  # Local LLM

# RAG Chain Construction
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# ============================================================
# 1) LOAD DOCUMENTS
# ============================================================
loader = PyPDFLoader("/Users/anantwagh/Downloads/Anant Wagh Resume - AI and Automation QA.pdf")
documents = loader.load()


# ============================================================
# 2) SPLIT DOCUMENTS INTO CHUNKS
# ============================================================
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(documents)


# ============================================================
# 3) CREATE EMBEDDINGS (HUGGINGFACE)
# ============================================================
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# ============================================================
# 4) STORE EMBEDDINGS IN VECTOR DATABASE (FAISS)
# ============================================================
vectordb = FAISS.from_documents(chunks, embeddings)


# ============================================================
# 5) CREATE RETRIEVER
# ============================================================
retriever = vectordb.as_retriever(search_kwargs={"k": 4})


# ============================================================
# 6) DEFINE THE LLM (OLLAMA - LOCAL, NO API KEY REQUIRED)
# ============================================================
#llm = OllamaLLM(model="mistral")    # You can replace with llama3 / gemma / phi3 etc.
llm = OllamaLLM(model="mistral", temperature=0)


# ============================================================
# 7) BUILD THE RAG PIPELINE (LLM + RETRIEVAL)
# ============================================================
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant. Use ONLY the context below to answer.

<context>
{context}
</context>

Question: {question}

Give a clear and concise answer.
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# ============================================================
# 8) ASK QUESTION + RUN PIPELINE
# ============================================================
query = "Summarize the document in 2 bullet points."
answer = rag_chain.invoke(query)

print("\n✅ FINAL ANSWER:\n")
print(answer)


# ============================================================
# 9) VIEW CHUNKS THAT WERE USED TO FORM THE ANSWER (EVALUATION)
# ============================================================
retrieved_docs = retriever.get_relevant_documents(query)

df = pd.DataFrame([
    {"Used Text Snippet": d.page_content[:200] + "..."}
    for d in retrieved_docs
])

print("\n📄 CONTEXT SOURCES USED:\n")
print(df)
