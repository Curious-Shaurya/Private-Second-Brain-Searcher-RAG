import streamlit as st
import os
from main import SecondBrain

# 1. PAGE CONFIGURATION
# Sets the browser tab title and creates a wide, professional layout.
st.set_page_config(page_title="Second Brain | Tuition Assistant", layout="wide")

# 2. CACHING THE ENGINE
# This ensures the AI model only loads once.
@st.cache_resource
def load_brain():
    return SecondBrain()

brain = load_brain()

# 3. SIDEBAR: UPLOAD CENTER
with st.sidebar:
    st.header("📂 Document Vault")
    st.write("Upload your worksheets (PDFs) here.")
    
    # Drag and Drop widget
    uploaded_files = st.file_uploader(
        "Drop PDFs here", 
        type="pdf", 
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    
    # Ingest Button
    if st.button("Learn Documents", use_container_width=True):
        if uploaded_files:
            progress_bar = st.progress(0)
            for i, uploaded_file in enumerate(uploaded_files):
                # Temporary path in current folder
                temp_path = uploaded_file.name
                
                # Write to disk temporarily so our processor can read it
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Ingest into the brain
                brain.add_document(temp_path)
                
                # STORAGE CLEANUP: Delete the file from local folder immediately
                os.remove(temp_path)
                
                # Update progress
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            st.success(f"Successfully learned {len(uploaded_files)} files!")
        else:
            st.warning("Please select files first.")

    # Status Metric
    count = brain.database.collection.count()
    st.divider()
    st.metric("Total Knowledge Chunks", count)

# 4. MAIN UI: SEARCH
st.title("🧠 My Second Brain")
st.write("Search through your tuition materials using natural language.")

query = st.text_input("", placeholder="Ask a question (e.g., What is the past perfect continuous tense?)")

if query:
    # Use a spinner for a professional 'loading' feel
    with st.spinner("Searching the vault..."):
        info = brain.read_question(query, n_results=3)
    
    # DEFENSIVE PROGRAMMING: Check if results exist to avoid IndexError
    if info and info.get('documents') and len(info['documents'][0]) > 0:
        all_docs = info['documents'][0]
        all_metas = info['metadatas'][0]

        st.subheader(f"Top results for: '{query}'")
        
        # Iterate through results using zip (parallel iteration)
        for text, meta in zip(all_docs, all_metas):
            # Extract filename from metadata
            full_path = meta.get("source", "Unknown Source")
            filename = os.path.basename(full_path)
            
            # Use an 'expander' or 'container' for a clean card look
            with st.container(border=True):
                st.write(f"**📄 File:** `{filename}`")
                # Preview first 300 characters
                st.write(f"**Preview:** {text.strip()[:300]}...")
    else:
        st.info("No relevant matches found in your current vault.")

# Footer
st.caption("Built for high-performance learning.")