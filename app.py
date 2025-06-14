import streamlit as st
from rag_engine import load_docs, create_vector_store, get_qa_chain

st.set_page_config(page_title="StyleRecall AI", layout="wide")
st.title("📚🧵 StyleRecall AI – Fashion Knowledge Explorer")

uploaded_file = st.file_uploader("Upload a fashion document (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Loading and indexing document..."):
        docs = load_docs(uploaded_file.name)
        vectorstore = create_vector_store(docs)
        qa_chain = get_qa_chain(vectorstore)
    st.success("Document processed and ready!")

    query = st.text_input("Ask a question about the fashion content:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa_chain.run(query)
        st.markdown(f"**🧠 Answer:** {answer}")
