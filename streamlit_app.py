import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="MarkItDown Converter",
    page_icon="📝",
    layout="centered"
)

st.title("📝 MarkItDown Converter")
st.write("Convert various file formats to Markdown")

# List of supported extensions
supported_extensions = ('.txt', '.doc', '.docx', '.pdf', '.mp3', '.pptx', '.jpg', '.jpeg', '.png', 
                      '.xlsx', '.xls', '.csv', '.json')

st.write(f"Supported formats: {', '.join(supported_extensions)}")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=[ext[1:] for ext in supported_extensions])

# Get API configuration from environment variables
api_port = os.getenv('API_PORT', '8001')
api_host = os.getenv('API_HOST', 'localhost')
API_URL = f"http://{api_host}:{api_port}/convert"

if uploaded_file is not None:
    # Show file info
    st.write("File details:")
    st.write(f"- Name: {uploaded_file.name}")
    st.write(f"- Type: {uploaded_file.type}")
    st.write(f"- Size: {uploaded_file.size} bytes")

    # Convert button
    if st.button("Convert to Markdown"):
        with st.spinner("Converting..."):
            try:
                # Prepare the file for upload
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                
                # Make the API request
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Display the markdown content
                    st.subheader("Markdown Output:")
                    st.text_area("", value=result["result"], height=300)
                    
                    # Add download button for markdown
                    st.download_button(
                        label="Download Markdown",
                        data=result["result"],
                        file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                        mime="text/markdown"
                    )
                else:
                    st.error(f"Error: {response.json()['detail']}")
            
            except Exception as e:
                st.error(f"Error occurred: {str(e)}")

# Add some helpful information
with st.sidebar:
    st.subheader("How to use")
    st.write("""
    1. Upload a supported file using the file uploader
    2. Click 'Convert to Markdown' to start conversion
    3. View the converted markdown in the text area
    4. Download the markdown file using the download button
    """)
    
    st.subheader("About")
    st.write("""
    This tool uses MarkItDown to convert various file formats to Markdown.
    The conversion is powered by GPT-4 for high-quality results.
    """)
