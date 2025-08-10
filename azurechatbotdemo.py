import streamlit as st
#from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.title("Azurelib Chatbot")







# Step 2: Set the environment variables for Azure AI Search
# These variables configure the search service and index for retrieving documents

# Set the Azure AI Search service name from environment variables
os.environ["AZURE_AI_SEARCH_SERVICE_NAME"] = os.getenv("AZURE_AI_SEARCH_SERVICE_NAME")

# Set the Azure AI Search index name to query from environment variables
os.environ["AZURE_AI_SEARCH_INDEX_NAME"] = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")

# Set the Azure AI Search API key for authentication from environment variables
os.environ["AZURE_AI_SEARCH_API_KEY"] = os.getenv("AZURE_AI_SEARCH_API_KEY")


# Import necessary libraries and modules from Langchain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import AzureChatOpenAI
from langchain_community.retrievers import AzureAISearchRetriever

# Step 1: Initialize the AzureAI Search Retriever
# This retrieves relevant documents based on the user query from the Azure Search index
retriever = AzureAISearchRetriever(
    content_key="Answer",  # The key for the content field in the search results change it accordingly as per your data
    top_k=3,              # Number of top results to retrieve
    index_name="azuretable-index"  # Name of the Azure Search index to query
)

# Step 2: Define the prompt template for the language model
# This sets up how the context and question will be formatted for the model
prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the context provided. Think intelligently

Context: {context}  # Placeholder for the context from the retriever

Question: {question}  # Placeholder for the user question"""
)


# Step 3: Initialize the Azure Chat OpenAI model
# This sets up the model to be used for generating responses

llm = AzureChatOpenAI(
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),  
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),          # Fetch the API key for Azure OpenAI from environment variables
    model=os.getenv("AZURE_OPENAI_MODEL")               # Specify the model to use
)





# Step 4: Create a processing chain
# This chain will process the retrieved context and the user question
chain = (
    {"context": retriever , "question": RunnablePassthrough()}  # Set context using the retriever and format it
    | prompt                                                               # Pass the formatted context and question to the prompt
    | llm                                                                  # Generate a response using the language model
    | StrOutputParser()                                                   # Parse the output to a string format
)


# Set OpenAI API key from Streamlit secrets
#client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_question := st.chat_input("How Can I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_question)
# Display assistant response in chat message container
    with st.chat_message("assistant"):
   
        
        response = chain.invoke(user_question)
      
        st.write(response)


        st.session_state.messages.append({"role": "assistant", "content": response})