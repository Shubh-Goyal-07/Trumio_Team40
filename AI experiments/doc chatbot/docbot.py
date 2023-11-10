import os 
from dotenv import load_dotenv, find_dotenv

# configure palm
import google.generativeai as palm

load_dotenv(find_dotenv()) # read local .env file

api_key=os.environ.get('GOOGLE_API_KEY')
palm.configure(api_key=api_key)

# models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
# model=models[0].name


# generate text
# prompt = 'Why is palestine and Israel fighting?'
# text = palm.generate_text(
#     prompt=prompt,
#     model=model,
#     temperature=0.1,
#     max_output_tokens=1024,
#     top_p=0.9,
#     top_k=40,
#     # stop_sequences=['\n\n']
# )
# print(text.result)




from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter


llm = GooglePalm()
llm.temperature = 0.1


# prompts = ["The opposite of hot is",'The opposite of cold is'] # according to the class prmpts must be in list
# llm_result = llm._generate(prompts)

# print(llm_result.generations[0][0].text)
# print(llm_result.generations[1][0].text)


pdf_folder_path = './pdfs'
pdf_loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]
pdf_index = VectorstoreIndexCreator(
        embedding=GooglePalmEmbeddings(),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)).from_loaders(pdf_loaders)

# print(pdf_index)

pdf_chain = RetrievalQA.from_chain_type(llm=llm,
                            chain_type="stuff",
                            retriever=pdf_index.vectorstore.as_retriever(kwargs={'k':4}),
                            input_key="question")

# print(pdf_chain)

pdf_answer = pdf_chain.run('Summarize the resume of the candidate as a list of bullet points.')

# print('\n\n')
print(pdf_answer)