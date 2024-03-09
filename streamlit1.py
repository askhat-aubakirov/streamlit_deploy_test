import streamlit as st

# Title and header
st.title("Hello, Streamlit World!")
st.header("This is my first Streamlit app!")

# Text and code display
st.write("This is some text content.")
st.code("""
def hello_world():
  print("Hello, World!")

hello_world()
""")

# Input widget (text box)
name = st.text_input("Enter your name:")

# Display entered name
if name:
  st.write("Hello, " + name + "!")

# Button and action
if st.button("Click me!"):
  st.balloons()  # Fun animation

# Run the app
if __name__ == "__main__":
  st.sidebar.title("Sidebar Menu")
  st.sidebar.text("This is content in the sidebar.")
  st.sidebar.button("Sidebar Button")
  st.balloons()  # Show balloons on app start
