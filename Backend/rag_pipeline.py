from langchain.vectorstores import Pinecone
from langchain_pinecone import Pinecone as PineconeVectorStore
from langchain_ollama.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
def get_qa():
    llm = ChatOllama(model="llama3.2")


    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    vectorstore = PineconeVectorStore(
    index_name="nutrition-index",
    embedding=embedding_model
)


    retriever = vectorstore.as_retriever(search_type="similarity")
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)


    return qa
