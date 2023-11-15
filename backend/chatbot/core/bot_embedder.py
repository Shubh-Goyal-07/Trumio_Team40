from langchain.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
import os
from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
import google.generativeai as palm

def parser(path):
    if '.pdf' in path:
        loader = PyPDFLoader(
                            file_path=path,
                            extract_images=False,
                        )
    # elif 'http' in path and '.pdf' in path:
    #     loader = OnlinePDFLoader(
    #                         file_path=path,
    #                         # extract_images=False,
    #                     )
    else:
        print("above directory loader")
        loader = DirectoryLoader(
                            path=path,
                            glob='**/*.*',
                        )
    print("loader: ", loader)
    data = loader.load()
    print("data: ", data)
    return data


def split_doc_to_chunk(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                   chunk_overlap=100
                                                   )
    splits = text_splitter.split_documents(data)
    return splits


def get_embedding_model():
    _ = load_dotenv(find_dotenv()) # read local .env file
    api_key = os.environ.get('GOOGLE_API_KEY')
    palm.configure(api_key=api_key)

    embedding = GooglePalmEmbeddings()
    return embedding


def make_vecdb(splits, projectid):
    embedding = get_embedding_model()
    print("Embedding model size: ", embedding.__sizeof__())
    persist_directory = './chroma'
    persist_directory = os.path.join(persist_directory, projectid)
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding,
        persist_directory=persist_directory
    )
    print("Vector DB size: ", vectordb.__sizeof__())
    return vectordb.__sizeof__()


def make_vecdb_for_project(projectid):
    
    path = './media/uploads/' + projectid +'/'
    print(path)
    data = parser(path)
    print("Data size: ", data.__sizeof__())
    splits = split_doc_to_chunk(data)
    print("Splits size: ", splits.__sizeof__())
    vecdeb_res = make_vecdb(splits, projectid)

    return vecdeb_res


# if __name__ == '__main__':
#     path = input('Enter the path of the file: ')
#     data = parser(path)
#     print(data)