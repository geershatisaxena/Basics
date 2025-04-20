import streamlit as st

# Set page config
st.set_page_config(page_title="Pro Calculator", page_icon="🧮", layout="centered")

# Title and Description
st.title("🧮 Professional Calculator")
st.write("A clean, simple calculator app built with Streamlit.")

st.divider()

# Input fields in two columns
col1, col2 = st.columns(2)
with col1:
    fnum = st.number_input("First Number", format="%.2f", step=1.0)
with col2:
    snum = st.number_input("Second Number", format="%.2f", step=1.0)

# Operation buttons
st.subheader("Select Operation")
col3, col4, col5, col6 = st.columns(4)
operation = None

if col3.button("➕ Add"):
    operation = "add"
elif col4.button("➖ Subtract"):
    operation = "subtract"
elif col5.button("✖️ Multiply"):
    operation = "multiply"
elif col6.button("➗ Divide"):
    operation = "divide"

# Perform calculation
if operation:
    try:
        if operation == "add":
            result = fnum + snum
            symbol = "+"
        elif operation == "subtract":
            result = fnum - snum
            symbol = "-"
        elif operation == "multiply":
            result = fnum * snum
            symbol = "×"
        elif operation == "divide":
            if snum == 0:
                raise ZeroDivisionError
            result = fnum / snum
            symbol = "÷"

        # Show result
        st.success(f"✅ Result: {fnum} {symbol} {snum} = **{round(result, 4)}**")

    except ZeroDivisionError:
        st.error("❌ Error: Division by zero is not allowed.")

# Footer
st.divider()
st.caption("Created with ❤️ using Streamlit")
