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
# import pinecone
# from langchain.vectorstores import Pinecone
from langchain.vectorstores import Chroma
from dotenv import load_dotenv, find_dotenv





# def split_doc_to_chunk(document):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
#                                                    chunk_overlap=100
#                                                    )
#     return text_splitter.split_documents(document)


# def get_embedding_model():
#     _ = load_dotenv(find_dotenv()) # read local .env file
#     api_key=os.environ.get('GOOGLE_API_KEY')
#     palm.configure(api_key=api_key)

#     return GooglePalmEmbeddings()


# def get_template():
#     return """Combine the following Chat history and question into a Standalone Question:
#     Chat history:
#     {chat_history}
#     Question:
#     {question}  """


# def get_custom_question_prompt(custom_template):

#     return PromptTemplate.from_template(custom_template)




class chatbot():

    instances = {}

    def __init__(self, session_id, project_id) -> None:
        self.session_id = session_id
        self.project_id = project_id


        # configure palm
        _ = load_dotenv(find_dotenv()) # read local .env file
        api_key = os.environ.get('GOOGLE_API_KEY')
        palm.configure(api_key=api_key)


        # general variables
        self.embedding = None
        self.persist_directory = './chroma'
        self.llm = None
        self.vectordb = None
        self.chain = None
        self.retriever = None
        self.memory = None

    # loading project data
    def __load_project_data(self):

        directory = f"{self.persist_directory}/{self.project_id}"

        if os.path.exists(directory):

            self.vectordb = Chroma(
                persist_directory=f"{self.persist_directory}/{self.project_id}",
                embedding_function=self.embedding
            )

            return True

        return False

    
    def __load_llm(self):
        self.llm = GooglePalm()

    def __load_embedding_model(self):
        self.embedding = GooglePalmEmbeddings()

    def __load_retrevier(self):
        self.retriever = self.vectordb.as_retriever(search_kwargs=dict(k=5))

    def __load_memory(self):
        memory_key = f"chat_history_{self.session_id}"
        self.memory = VectorStoreRetrieverMemory(retriever=self.retriever, memory_key=memory_key,return_messages=True)

    # creating chain
    def __create_chain(self):
        self.__load_llm()
        self.__load_embedding_model()
        self.__load_retrevier()
        # self.__make_memory()
        self.chain=ConversationalRetrievalChain.from_llm(llm=self.llm,
                                                         retriever=self.retriever, 
                                                         # condense_question_prompt=prompt, 
                                                         # memory=self.memory,
                                                         # verbose=True, 
                                                         # get_chat_history=lambda h : h, 
                                                         # return_generated_question=True
                                                         )

        return True


    # loading project data, chat data and creating chain
    def load_bot(self):
        if not self.__load_project_data():
            return {'status': False, 'message': 'Project data not found'}
        if not self.__load_chat_data():
            return {'status': False, 'message': 'Chat data not found'}
        if not self.__create_chain():
            return {'status': False, 'message': 'Chain creation failed'}

        return {'status': True, 'message': 'Project data loaded successfully'}

    def get_response(self, question):
        result = self.chain({"question": question})
        return result['answer']

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


def bot_loader(session_id, project_id):
    instance = chatbot(session_id, project_id)
    load_msg = instance.load_bot()
    if load_msg['status']:
        # chatbot.instances[session_id] = instance
        # return {'status': True, 'message': load_msg['message']}
        chain_msg = instance.create_chain()
        if chain_msg:
            chatbot.instances[session_id] = instance
            return {'status': True, 'message': 'Ready for chat'}
        
    return {'status': False, 'message': load_msg['message']}


def get_response(session_id, question):
    print(chatbot.instances)
    if session_id in chatbot.instances:
        return {'status': True, 'message': chatbot.instances[session_id].get_response(question)} 
    else:
        return {'status': False, 'message': 'Session not found'}


# if __name__ == '__main__':
#     load_dotenv()
#     palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#     index_name = 'chat-history-trumio'
#     pinecone.init(
#         api_key=os.getenv("PINECONE_API_KEY"),
#         environment="gcp-starter"
#     )
#     pdf = 'Forza_Code.pdf'
#     data = doc_parse(pdf)
#     documents = split_doc_to_chunk(data)
#     embeddings = get_embedding_model()
#     index = pinecone.Index(index_name)
#     vectorstore = Pinecone(index, embeddings.embed_query, "text")
#     retriever = vectorstore.as_retriever(search_kwargs=dict(k=2))
#     memory = VectorStoreRetrieverMemory(retriever=retriever, memory_key="chat_history",return_messages=True)
#     vectordb = Chroma.from_documents(documents, embeddings)
#     template = get_template()
#     prompt = get_custom_question_prompt(template)
#     llm = GooglePalm()
#     chain=ConversationalRetrievalChain.from_llm(llm=llm,
#                                                 retriever=vectordb.as_retriever(), 
#                                                 condense_question_prompt=prompt, 
#                                                 memory=memory,verbose=True, 
#                                                 get_chat_history=lambda h : h, 
#                                                 return_generated_question=True)
#     question="my name is akhil"
#     result=chain({"question": question })
#     if result is not None:
#         print(result)
