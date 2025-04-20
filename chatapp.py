import streamlit as st

# Title
st.title("💬 Simple Chat App")

# Initialize chat history in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input area
prompt = st.chat_input("Type your message here...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Simple bot response (you can make it smarter!)
    response = f"You said: '{prompt}' 🤖"

    # Show bot response
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
