from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as palm
import os
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.llms import GooglePalm
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import Chroma
import environ
env = environ.Env()
environ.Env.read_env()


# from langchain.output_parsers.

api_key = env('GOOGLE_API_KEY')

# _ = load_dotenv(find_dotenv()) # read local .env file
# api_key = os.environ.get('GOOGLE_API_KEY')
palm.configure(api_key=api_key)


def make_chain(prompt: PromptTemplate, llm: GooglePalm) -> ConversationalRetrievalChain:
    """
    Makes a ConversationalRetrievalChain from a prompt and a language model.
    """

    chain = prompt | llm

    return chain


def make_prompt(title: str, pointers: list) -> str:
    """
    Generates a prompt from a list of pointers and a title.
    """
    
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a an instructor at a university. You are teaching a course on {title}. You will be given some pointers to help you create content a one hour lecture for the course. Do bifurcate in different topics only, not in slides. While you provide "),
    ("human", "Here are the pointers: {pointers}"),])

    return prompt



def generate_lecture(title: str, pointers: list) -> str:
    """
    Generates a lecture from a list of pointers and a title.
    """

    # pointers = "\n\n-".join(pointers)
    
    prompt = make_prompt(title, pointers)
    llm = GooglePalm()
    chain = make_chain(prompt, llm)

    response = chain.invoke({"title": title, "pointers": pointers})

    return response