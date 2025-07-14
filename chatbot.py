import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
API_KEY = "Actual API_KEY"  
genai.configure(api_key=API_KEY)

# Initialize the model
try:
    model = genai.GenerativeModel("gemini-1.5-pro")  
except Exception as e:
    st.error(f"Model initialization failed: {e}")

def generate_response(prompt):
    """Generate a response using the Gemini API."""
    try:
        response = model.generate_content(prompt)
        return response.text if response else "No response generated."
    except Exception as e:
        return f"Error generating response: {e}"

# Theme toggle for light/dark mode
theme = st.sidebar.radio("🌗 Select Theme", ["Light Mode", "Dark Mode"])
if theme == "Dark Mode":
    st.markdown("""
        <style>
            body { background-color: #1E1E1E; color: white; }
            .response-box { background-color: #333; color: white; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background-color: #f5f5f5; color: black; }
            .response-box { background-color: #ffffff; padding: 10px; border-radius: 8px; margin-bottom: 10px; box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1); }
        </style>
    """, unsafe_allow_html=True)

# Sidebar Branding and About Section
st.sidebar.image("image.png", width=150)  # Replace with your logo
st.sidebar.title("About WriteWise AI")
st.sidebar.write("WriteWise AI is your ultimate writing assistant, helping you craft professional and flawless content with ease.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_area("Enter your text or query:", height=80)

# Generate response button
if st.button("Generate Response"):
    if user_input.strip():  
        response = generate_response(user_input)
        
        # Store the conversation in chat history
        st.session_state.chat_history.append({"user": user_input, "bot": response})

        # Display chat history
        for chat in reversed(st.session_state.chat_history):
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.write(f"**You:** {chat['user']}")
            st.write(f"**WriteWise AI:** {chat['bot']}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a query before generating a response.")
