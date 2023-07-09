from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings

import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def query_doc(query: str) -> str:
    """
    Predicts an answer for given question/query

    Parameters
    ----------
    query: str
           Question/query 
    
    Returns
    -------
    answer: str
            Answer predicted by the model
    """
    persist_dir = os.getenv('PERSIST_DIR')
    llm_name = os.getenv('LLM_NAME')

    embedding = HuggingFaceEmbeddings()
    vector_db = Chroma(persist_directory=persist_dir, 
                       embedding_function=embedding)

    # print("**************************************************")

    llm = ChatOpenAI(model_name=llm_name, temperature=0)

    # Create a prompt template to give more context 
    # and also to avoid hallucination
    # context is the metadata relating to each 
    # page content that we earlier created during 
    # doc vectorisation
    document_prompt = PromptTemplate(input_variables=["page_content","context"], 
                                     template="Answer the query with respect to the context and \
                                          avoid making up answers. Use the page content: \
                                            '{page_content}' and document context: '{context}'")
    
    # Use 'similarity' search type so that 
    # the result generated is not very different 
    # from the actual content provided in the 
    # knowledge doc
    retrieverqa = RetrievalQA.from_chain_type(
                                llm=llm,
                                chain_type="stuff",
                                retriever=vector_db.as_retriever(search_type='similarity'),
                                chain_type_kwargs={"document_prompt": document_prompt},
                                verbose=True
                            )

    result = retrieverqa({"query": query})
    answer = result["result"] 

    return  answer
