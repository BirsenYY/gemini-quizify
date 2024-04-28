import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from document_processor import DocumentProcessor
from embedding_client import EmbeddingClient
from chroma_collection_creator import ChromaCollectionCreator

f"""
Task: Build a Quiz Builder with Streamlit and LangChain

Overview:
In this task, you will leverage your skills acquired from previous tasks to create a "Quiz Builder" application utilizing Streamlit. This interactive application enables users to upload documents, designate a quiz topic, select a number of questions, and subsequently generate a quiz based on the uploaded document contents.

Components to Integrate:
- DocumentProcessor: A class developed in Task 3 for processing uploaded PDF documents.
- EmbeddingClient: A class from Task 4 dedicated to embedding queries.
- ChromaCollectionCreator: A class from Task 5 responsible for creating a Chroma collection derived from the processed documents.

Step-by-Step Instructions:
1. Begin by initializing an instance of the `DocumentProcessor` and invoke the `ingest_documents()` method to process the uploaded PDF documents.

2. Configure and initialize the `EmbeddingClient` with the specified model, project, and location details as provided in the `embed_config`.

3. Instantiate the `ChromaCollectionCreator` using the previously initialized `DocumentProcessor` and `EmbeddingClient`.

4. Utilize Streamlit to construct a form. This form should prompt users to input the quiz's topic and select the desired number of questions via a slider component.

5. Following the form submission, employ the `ChromaCollectionCreator` to forge a Chroma collection from the documents processed earlier.

6. Enable users to input a query pertinent to the quiz topic. Utilize the generated Chroma collection to extract relevant information corresponding to the query, which aids in quiz question generation.

Implementation Guidance:
- Deploy Streamlit's widgets such as `st.header`, `st.subheader`, `st.text_input`, and `st.slider` to craft an engaging form. This form should accurately capture the user's inputs for both the quiz topic and the number of questions desired.

- Post form submission, verify that the documents have been processed and that a Chroma collection has been successfully created. The build-in methods will communicate the outcome of these operations to the user through appropriate feedback.

- Lastly, introduce a query input field post-Chroma collection creation. This field will gather user queries for generating quiz questions, showcasing the utility of the Chroma collection in sourcing information relevant to the quiz topic.

"""

if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",    
        "project": "your project ID",
        "location": "your location"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        #st.header("Quizzify")
        processor = DocumentProcessor()
        processor.ingest_documents()
        embedding_client = EmbeddingClient(**embed_config)
        chroma_creator = ChromaCollectionCreator(processor, embedding_client)
        

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
            
            topic_input = st.text_input("Enter Quiz Topic")
            num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=10)
            
            
            
            document = None
            
            submitted = st.form_submit_button("Generate a Quiz!")
            
            if submitted:
 
                chroma_creator.create_chroma_collection()
                   
                # Uncomment the following lines to test the query_chroma_collection() method
                #document = chroma_creator.query_chroma_collection(topic_input) 
                
    if document:
        #screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)