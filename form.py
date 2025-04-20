import streamlit as st

# Title of the app
st.title("🎈 Welcome to My Streamlit App!")

# Subheader
st.subheader("Let's collect some information from you")

# Create a form
with st.form("user_form"):
    name = st.text_input("What's your name?")
    color = st.selectbox("Pick your favorite color", ["Red", "Green", "Blue", "Yellow", "Other"])
    date = st.date_input("Pick a date")
    message = st.text_area("Say something...")
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# Show the results after submission
if submitted:
    st.success("✅ Form submitted successfully!")
    st.write("Here's what you told us:")
    st.write(f"**Name:** {name}")
    st.write(f"**Favorite Color:** {color}")
    st.write(f"**Selected Date:** {date}")
    st.write(f"**Message:** {message}")
