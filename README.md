# Azure RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using Azure services and Streamlit. This application combines Azure AI Search for document retrieval and Azure OpenAI for intelligent response generation.

## 🚀 Overview

This project implements a RAG (Retrieval-Augmented Generation) system that:
- Retrieves relevant documents from an Azure AI Search index
- Uses Azure OpenAI GPT models to generate contextual responses
- Provides an interactive chat interface through Streamlit

## 🏗️ Architecture

The application follows a standard RAG architecture:

1. **Document Retrieval**: Azure AI Search retrieves relevant documents based on user queries
2. **Context Formation**: Retrieved documents provide context for the language model
3. **Response Generation**: Azure OpenAI generates responses based on the context and user question
4. **User Interface**: Streamlit provides an interactive chat interface

## 🛠️ Technologies Used

- **Azure AI Search**: Document indexing and retrieval
- **Azure OpenAI**: GPT-4 model for response generation
- **LangChain**: Framework for building LLM applications
- **Streamlit**: Web application framework
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8+
- Azure subscription with:
  - Azure AI Search service
  - Azure OpenAI service
- API keys for Azure services

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AzureQARAG
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root with the following variables:
   ```env
   # Azure AI Search Configuration
   AZURE_AI_SEARCH_SERVICE_NAME=your_search_service_name
   AZURE_AI_SEARCH_INDEX_NAME=your_index_name
   AZURE_AI_SEARCH_API_KEY=your_search_api_key

   # Azure OpenAI Configuration
   AZURE_OPENAI_ENDPOINT=your_openai_endpoint
   AZURE_OPENAI_API_KEY=your_openai_api_key
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   AZURE_OPENAI_MODEL=gpt-4.1-mini

   # Azure Storage Configuration
   AZURE_STORAGE_CONNECTION_STRING=your_storage_connection_string
   AZURE_TABLE_NAME=data
   ```

## 🚀 Usage

1. **Prepare your data**
   - Use `datainsert.py` to insert your data into Azure AI Search index
   - Ensure your CSV data file (`azurelib2.csv`) is properly formatted

2. **Run the application**
   ```bash
   streamlit run azurechatbotdemo.py
   ```

3. **Access the chatbot**
   - Open your browser and navigate to `http://localhost:8501`
   - Start chatting with the RAG-powered assistant

## 📁 Project Structure

```
AzurelibQAProject/
├── azurechatbotdemo.py      # Main Streamlit application
├── datainsert.py            # Script to insert data into Azure Search
├── azurelib2.csv           # Sample data file
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🔒 Security Best Practices

- **Never commit API keys** to version control
- Store sensitive credentials in `.env` file
- Use different API keys for different environments
- Consider using Azure Key Vault for production deployments

## ⚙️ Configuration

### Azure AI Search Setup
- Content key: `Answer` (modify in code if your data structure differs)
- Top-k results: 3 documents per query
- Index name: configurable via environment variables

### Azure OpenAI Setup
- Model: GPT-4.1-mini (configurable)
- API version: 2024-12-01-preview
- Temperature and other parameters can be adjusted in the code

## 🔄 Data Flow

1. User enters a question in the Streamlit chat interface
2. Azure AI Search retriever finds relevant documents
3. Retrieved documents provide context for the prompt
4. Azure OpenAI generates a response based on context and question
5. Response is displayed in the chat interface

## 🛠️ Customization

### Modifying the Prompt Template
Edit the prompt template in `azurechatbotdemo.py`:
```python
prompt = ChatPromptTemplate.from_template(
    """Your custom prompt template here
    
    Context: {context}
    Question: {question}"""
)
```

### Adjusting Retrieval Parameters
Modify the retriever configuration:
```python
retriever = AzureAISearchRetriever(
    content_key="your_content_field",
    top_k=5,  # Adjust number of results
    index_name="your_index_name"
)
```

## 🐛 Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify API keys are correct
   - Check endpoint URLs
   - Ensure services are properly configured in Azure

2. **Search Index Issues**
   - Verify index name matches your Azure Search index
   - Check if data was properly inserted using `datainsert.py`
   - Ensure content_key matches your data schema

3. **Model Errors**
   - Verify model name and API version
   - Check Azure OpenAI service deployment status

## 📊 Performance Optimization

- Adjust `top_k` parameter for retrieval quality vs. speed trade-off
- Implement caching for frequently asked questions
- Consider using semantic search capabilities in Azure AI Search

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
