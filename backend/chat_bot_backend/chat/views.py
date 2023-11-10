from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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


from . import bot


# Create your views here.


class ChatView(APIView):


    def get(self, request, *args, **kwargs):

        load_dotenv()
        palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        index_name = 'chat-history-trumio'
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment="gcp-starter"
        )
        pdf = 'chat/ibm.pdf'
        data = bot.doc_parse(pdf)
        documents = bot.split_doc_to_chunk(data)
        embeddings = bot.get_embedding_model()
        index = pinecone.Index(index_name)
        vectorstore = Pinecone(index, embeddings.embed_query, "text")
        retriever = vectorstore.as_retriever(search_kwargs=dict(k=2))
        memory = VectorStoreRetrieverMemory(retriever=retriever, memory_key="chat_history",return_messages=True)
        vectordb = Chroma.from_documents(documents, embeddings)
        template = bot.get_template()
        prompt = bot.get_custom_question_prompt(template)
        llm = GooglePalm()
        chain=ConversationalRetrievalChain.from_llm(llm=llm,
                                                    retriever=vectordb.as_retriever(), 
                                                    condense_question_prompt=prompt, 
                                                    memory=memory,verbose=True, 
                                                    get_chat_history=lambda h : h, 
                                                    return_generated_question=True)
        # question="my name is akhil"
        # result=chain({"question": question })
        # if result is not None:
        #     print(result)


        next = True
        # while next:
            # question = "Describe the detectors being used in the Guardrails"
        question = input("Question: ")
        result=chain({"question": question })
        print(f"Answer: {result['answer']}")

        next = input("Next? (1/0): ")

        print("\n\n")

        
        return Response({"message": result})