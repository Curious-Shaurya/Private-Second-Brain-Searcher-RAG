# Private-Retrieval-Augmented-Generation-Searching
A local, AI-powered search and summarization engine for your educational documents. This tool uses vector embeddings to find relevant content in your PDFs and Docx files and Llama 3 to answer your questions.


### Key Features
Semantic Search: Finds relevant content based on context and concepts, not just exact word matches.

Multi-Format Support: Seamlessly ingests and parses both .pdf and .docx files.

Local-First Privacy: All processing, embedding, and storage happen on your local machine. No data is sent to the cloud.

Clean UI: A minimalistic Streamlit interface designed for quick navigation during tutoring sessions.

### The Tech Stack
Frontend: Streamlit

Vector Database: ChromaDB

Embeddings: all-MiniLM-L6-v2 (Sentence-Transformers)

Document Processing: pypdf and python-docx


### Prerequisites
Before you begin, ensure you have the following installed:

Python 3.14+: Download from python.org. During installation, make sure to check the box "Add Python to PATH".

Ollama: Download from ollama.com. After installing, open your terminal or command prompt and run the command: ollama pull llama3

### Installation
Download the Project: Extract the project files into your folder of choice.

Open Terminal: Navigate to that folder, click the address bar at the top, type cmd, and press Enter.

Create a Virtual Environment: Type "python -m venv venv" and press Enter.

Activate the Environment: Type "venv\Scripts\activate" and press Enter. You should now see (venv) at the start of your command line.

Install Libraries: Type "pip install -r requirements.txt" and press Enter to download the necessary tools.

### How to Use
Start the App: Ensure your virtual environment is active and run the command: "streamlit run app.py".

Upload: Use the sidebar in the browser window to upload your worksheets.

Search: Type your question in the text box. The AI will search your local database and provide a summarized answer based only on your documents.

### Dependencies
The project uses the following libraries: streamlit, ollama, chromadb, sentence-transformers, pypdf, and python-docx.
