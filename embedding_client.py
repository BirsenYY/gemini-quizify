
from langchain_google_vertexai import VertexAIEmbeddings
import streamlit as st


class EmbeddingClient:
    """
    Task: Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.

    The EmbeddingClient class should be capable of initializing an embedding client with specific configurations
    for model name, project, and location. Your task is to implement the __init__ method based on the provided
    parameters. This setup will allow the class to utilize Google Cloud's VertexAIEmbeddings for processing text queries.

    Steps:
    1. Implement the __init__ method to accept 'model_name', 'project', and 'location' parameters.
       These parameters are crucial for setting up the connection to the VertexAIEmbeddings service.

    2. Within the __init__ method, initialize the 'self.client' attribute as an instance of VertexAIEmbeddings
       using the provided parameters. This attribute will be used to embed queries.

    Parameters:
    - model_name: A string representing the name of the model to use for embeddings.
    - project: The Google Cloud project ID where the embedding model is hosted.
    - location: The location of the Google Cloud project, such as 'us-central1'.

    Instructions:
    - Carefully initialize the 'self.client' with VertexAIEmbeddings in the __init__ method using the parameters.
    - Pay attention to how each parameter is used to configure the embedding client.

    Note: The 'embed_query' method has been provided for you. Focus on correctly initializing the class.
    """
    
    def __init__(self, model_name, project, location):
        """
        Initialize the embedding client with a specific model, project, and location for Google VertexAI.
        """
        self.client = VertexAIEmbeddings(
            model_name=model_name,
            project=project,
            location=location
        )
        
    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.

        :param query: The text query to embed.
        :return: The embeddings for the query or None if the operation fails.
        """
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.

        :param documents: A list of text documents to embed.
        :return: A list of embeddings for the given documents.
        """
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

# Streamlit interface
if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "your project ID"
    location = "your location"

    embedding_client = EmbeddingClient(model_name, project, location)
    
    st.title('Text Embedding Display')
    query = st.text_input("Enter text to embed:", "Hello World!")
    
    if st.button("Get Embedding"):
        vectors = embedding_client.embed_query(query)
        if vectors:
            st.write(vectors)
            st.success("Successfully retrieved and displayed the embeddings.")
        else:
            st.error("Failed to retrieve embeddings.")
