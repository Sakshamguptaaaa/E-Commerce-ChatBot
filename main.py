import streamlit as st
from faq import faq_chain, ingest_faq_data
from sql import sql_chain
from smalltalk import small_talk_chain
from router import router
from pathlib import Path

faqs_path = Path(__file__).parent / "faq_data.csv"
ingest_faq_data(faqs_path)

def ask(query, history=[]):
    route_obj = router(query)
    route = route_obj.name if route_obj else None
    
    if route is None:
        if "last_route" in st.session_state:
            route = st.session_state["last_route"]
        else:
            route = 'small-talk'
    else:
        st.session_state["last_route"] = route

    if route == 'faq':
        return faq_chain(query, history)
    elif route == 'sql':
        return sql_chain(query, history)
    else:
        return small_talk_chain(query, history)

st.title("E-Commerce chatbot")


query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append({"role": "user", "content": query})
    recent_history = st.session_state.messages[-4:] 

    response = ask(query, recent_history)
    with st.chat_message("Assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "Assistant", "content": response})
