from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import google.generativeai as palm
import os
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import GooglePalm
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import VectorStoreRetrieverMemory
import pinecone
from langchain.vectorstores import Pinecone


def doc_parse(pdf):
    loader = PyPDFLoader(pdf)
    data = loader.load()
    return data

def split_doc_to_chunk(document):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0,)
    return text_splitter.split_documents(document)

def get_embedding_model():
    return GooglePalmEmbeddings()

def get_template():
    return """Combine the following Chat history and question into a Standalone Question:
    Chat history:
    {chat_history}
    Question:
    {question}  """

def get_custom_question_prompt(custom_template):
    return PromptTemplate.from_template(custom_template)



if __name__ == '__main__':
    load_dotenv()
    palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    index_name = 'chat-history-trumio'
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment="gcp-starter"
    )
    pdf = 'Forza_Code.pdf'
    data = doc_parse(pdf)
    documents = split_doc_to_chunk(data)
    embeddings = get_embedding_model()
    index = pinecone.Index(index_name)
    vectorstore = Pinecone(index, embeddings.embed_query, "text")
    retriever = vectorstore.as_retriever(search_kwargs=dict(k=2))
    memory = VectorStoreRetrieverMemory(retriever=retriever, memory_key="chat_history",return_messages=True)
    vectordb = Chroma.from_documents(documents, embeddings)
    template = get_template()
    prompt = get_custom_question_prompt(template)
    llm = GooglePalm()
    chain=ConversationalRetrievalChain.from_llm(llm=llm,
                                                retriever=vectordb.as_retriever(), 
                                                condense_question_prompt=prompt, 
                                                memory=memory,verbose=True, 
                                                get_chat_history=lambda h : h, 
                                                return_generated_question=True)
    question="my name is akhil"
    result=chain({"question": question })
    if result is not None:
        print(result)
