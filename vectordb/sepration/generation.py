import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from retrival import get_context


load_dotenv()

st.title("Naive RAG Chatbot")


client_groq = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("What would you like to know?"):

    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)


    retrieved_docs = get_context(user_query)

    system_prompt = f"""You are a helpful assistant with memory of the full conversation.
You also have access to a relevant document chunk below.

Use the DOCUMENT CONTEXT to answer questions about the topic.
Use the CONVERSATION HISTORY to answer follow-up questions like:
- "what was my last question?"
- "explain that again"
- "summarize what we talked about"

DOCUMENT CONTEXT:
{retrieved_docs}

If neither the context nor the conversation history has the answer, say: 'I don't have this information yet.'"""

   
    llm_messages = [{"role": "system", "content": system_prompt}]
    llm_messages += st.session_state.messages

  
    with st.chat_message("assistant"):
        response = client_groq.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=llm_messages
        )
        answer = response.choices[0].message.content
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})