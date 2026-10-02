import streamlit as st
from chatbot_engine import FAQBot

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬")
st.title("💬 FAQ Chatbot")

@st.cache_resource
def load_bot():
    return FAQBot("faqs.csv")

bot = load_bot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    result = bot.get_answer(prompt)
    with st.chat_message("assistant"):
        st.write(result["answer"])
        st.caption(f"Confidence: {result['confidence']}")

    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})