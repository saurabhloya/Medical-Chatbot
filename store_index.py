from src.helper import load_pdf,text_split,dowload_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("data\\")

text_chunks = text_split(extracted_data)

embeddings = dowload_hugging_face_embeddings()

index_name = "medical-chatbot"

PineconeVectorStore(index_name=index_name,embedding=embeddings)
docsearch = PineconeVectorStore.from_documents(text_chunks,index_name=index_name,embedding=embeddings)