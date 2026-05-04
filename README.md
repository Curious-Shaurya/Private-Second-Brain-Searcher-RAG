# Private-Retrieval-Augmented-Generation-Searching

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

### Installation
Download Repository:
- Simply click the code dropdown button, click download zip and unzip the files. 
install dependencies:
Run the following command in your terminal if you have pip installed already. If not install pip first. 
- pip install -r requirement.txt

### Usage
To run the app: 
- Open the folder in termal and run the following command and a new screen should open. 
- streamlit run app.py
