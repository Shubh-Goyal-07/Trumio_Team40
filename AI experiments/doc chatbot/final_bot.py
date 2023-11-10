import os
# import openai
import sys


# import panel as pn
# pn.extension()

# configure palm
import google.generativeai as palm


# READ OPENAI API KEY FROM .env FILE
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

api_key=os.environ.get('GOOGLE_API_KEY')
palm.configure(api_key=api_key)


# LOADING PDF
# from langchain.document_loaders import PyPDFLoader
# loader = PyPDFLoader('./pdfs/srs.pdf')

# pages = loader.load()

# page=pages[0]
# print(page.metadata)

#  SPLITTING THE DOCUMENT INTO CHUNKS

# from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTextSplitter

# text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=150, length_function=len)


# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)


# docs = text_splitter.split_documents(pages)

# text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=200)


# splits = text_splitter.split_documents(pages)


# print(docs[0].metadata)
# print(docs[0].page_content)
# print(len(splits))


from langchain.embeddings import GooglePalmEmbeddings

embedding = GooglePalmEmbeddings()

# sentence1 = "The opposite of hot is"
# sentence2 = "The opposite of cold is"
# sentence3 = "The weather is ugly today"

# embedding1 = embedding.embed_query(sentence1)
# embedding2 = embedding.embed_query(sentence2)
# embedding3 = embedding.embed_query(sentence3)

# import numpy as np
# print(np.dot(embedding1, embedding2))
# print(np.dot(embedding1, embedding3))
# print(np.dot(embedding2, embedding3))

from langchain.vectorstores import Chroma

persist_directory = './chroma'

# !rm -rf ./chroma

# vectordb = Chroma.from_documents(
#     documents=splits,
#     embedding=embedding,
#     persist_directory=persist_directory
# )


vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

# print(vectordb._collection.count())



# docs = vectordb.similarity_search(question, k=5)

# len(docs)

# for doc in docs:
    # print(doc.metadata)

# print(docs[0].page_content)


# docs = vectordb.max_marginal_relevance_search(question, k=2, fetch_k=5)

# print(docs)


from langchain.chat_models import ChatGooglePalm
llm = ChatGooglePalm(model_name='models/chat-bison-001', temperature=0)



from langchain.chains import RetrievalQA, ConversationalRetrievalChain

# qa_chain = RetrievalQA.from_chain_type(
    # llm, 
    # retriever = vectordb.as_retriever()
# )


# result = qa_chain({"query" : question})
# print(result["result"])


from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)



from langchain.prompts import PromptTemplate

# Build Prompt
template = """Use the following pieces of context to answer the question at  the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
{context}

Question: {question}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# qa_chain = RetrievalQA.from_chain_type(
#     llm, 
#     retriever = vectordb.as_retriever(),
#     return_source_documents=True,
#     chain_type_kwargs={"prompt" : QA_CHAIN_PROMPT}  
# )

retriever = vectordb.as_retriever()
qa_chain = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory,
)


next = True
while next:
    # question = "Describe the detectors being used in the Guardrails"
    question = input("Question: ")
    result = qa_chain({"question" : question})
    print(f"Answer: {result['answer']}")

    next = input("Next? (1/0): ")

    print("\n\n")
# print(f"Question: {question}")

# print(len(result["source_documents"]))







# DIFFERENT METHODS OF RETRIEVAL


# from langchain.llms import GooglePalm
# from langchain.retrievers.self_query.base import SelfQueryRetriever
# from langchain.chains.query_constructor.base import AttributeInfo

# metadata_field_info = [
#     AttributeInfo(
#         name="page",
#         description="The page from the document",
#         type="integer",
#     ),
# ]

# document_content_description = "LLM Guardrails and detectors"

# llm = GooglePalm(temperature=0)

# # retriever = SelfQueryRetriever.from_llm(
# #     llm,
# #     vectordb,
# #     document_content_description,
# #     metadata_field_info,
# #     verbose=True
# # )




# # docs = retriever.get_relevant_documents(question)
# # # print(docs)

# # for d in docs:
# #     print(d.metadata)




# from langchain.retrievers import ContextualCompressionRetriever
# from langchain.retrievers.document_compressors import LLMChainExtractor

# compressor = LLMChainExtractor.from_llm(llm)

# compression_retriever = ContextualCompressionRetriever(
#     base_compressor=compressor,
#     base_retriever=vectordb.as_retriever(search_type="mmr"),
# )


# compressed_docs = compression_retriever.get_relevant_documents(question)

# # for d in compressed_docs:
# #     print(d.metadata)