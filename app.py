import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()
# Inject Google AdSense script into the page

# Configure the page
st.set_page_config(
    page_title="Prompt Enhancer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

adsense_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3575681239429167"
     crossorigin="anonymous"></script>
"""

st.markdown("""
    <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-3575681239429167"
        data-ad-slot="YOUR_AD_SLOT"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
""", unsafe_allow_html=True)

# Custom CSS with modern styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Title styling */
    .title-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(45deg, #FF4B4B, #FF6B6B);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #FF4B4B, #FF6B6B);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #FF6B6B, #FF8B8B);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }
    
    /* Card styling */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    /* Info box styling */
    .info-box {
        background-color: #e3f2fd;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        background-color: #f8f9fa;
        border-top: 1px solid #e0e0e0;
        margin-top: 2rem;
    }
    
    /* Premium box styling */
    .premium-box {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description with enhanced styling
st.markdown("""
    <div class="title-container">
        <h1 style="color: white; margin: 0;">✨ Prompt Enhancer</h1>
        <p style="color: white; margin: 0.5rem 0 0;">Transform your prompts into powerful, well-structured versions</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state for tracking API calls and last usage
if 'api_called' not in st.session_state:
    st.session_state.api_called = False
if 'last_usage_date' not in st.session_state:
    st.session_state.last_usage_date = None

def can_use_enhancer():
    """Check if user can use the enhancer based on daily limit"""
    if st.session_state.last_usage_date is None:
        return True
    
    last_usage = datetime.strptime(st.session_state.last_usage_date, '%Y-%m-%d')
    today = datetime.now().date()
    
    return last_usage.date() < today

def update_usage_date():
    """Update the last usage date"""
    st.session_state.last_usage_date = datetime.now().strftime('%Y-%m-%d')

def enhance_prompt(prompt):
    """Enhance the prompt using Gemini API"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return "Error: API key not found. Please set GEMINI_API_KEY in your .env file."
    
    try:
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Create the model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        system_prompt = """You are an expert prompt engineer. Enhance the given prompt by:
        1. Adding clear context and constraints
        2. Including specific examples where relevant
        3. Breaking down complex tasks into steps
        4. Adding output format specifications
        5. Including quality criteria
        6. Making it more specific and actionable
        Return only the enhanced prompt without any explanations."""
        
        full_prompt = f"{system_prompt}\n\nUser Prompt: {prompt}\n\nEnhanced Prompt:"
        
        # Generate response
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar with information
with st.sidebar:
    st.markdown("""
        <div class="card">
            <h3>About Prompt Enhancer</h3>
            <p>This tool helps you create better prompts by:</p>
            <ul>
                <li>Adding clear context and constraints</li>
                <li>Including specific examples</li>
                <li>Breaking down complex tasks</li>
                <li>Specifying output formats</li>
                <li>Adding quality criteria</li>
                <li>Making prompts more actionable</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card">
            <h3>Usage Tips</h3>
            <p>For best results:</p>
            <ul>
                <li>Be specific in your original prompt</li>
                <li>Include any relevant context</li>
                <li>Mention desired output format</li>
                <li>Specify any constraints</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Premium section in sidebar
    st.markdown("""
        <div class="premium-box">
            <h3>Want More Enhancements?</h3>
            <p>Get unlimited daily enhancements by supporting the project!</p>
            <a href="https://www.buymeacoffee.com/yourusername" target="_blank" style="color: white; text-decoration: none; font-weight: bold;">
                ☕DM here
            </a>
        </div>
    """, unsafe_allow_html=True)

# Main content area
st.markdown("""
    <div class="info-box">
        <p style="margin: 0;">💡 <strong>Pro Tip:</strong> The enhanced prompt will be optimized for better results with AI models.</p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for input and output
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card">
            <h3>Your Prompt</h3>
            <p>Enter the prompt you want to enhance below:</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_prompt = st.text_area("", height=200, placeholder="Enter your prompt here...")
    
    if st.button("✨ Enhance Prompt"):
        if not user_prompt:
            st.warning("Please enter a prompt first!")
        elif not can_use_enhancer():
            st.error("You've already used your free enhancement today. Please try again tomorrow or support the project for unlimited enhancements!")
            st.markdown("""
                <div class="premium-box">
                    <p>Get unlimited daily enhancements by supporting the project!</p>
                    <a href="https://www.instagram.com/rethinkgenai/" target="_blank" style="color: white; text-decoration: none; font-weight: bold;">
                        ☕ DM here
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Enhancing your prompt... This may take a few seconds."):
                enhanced_prompt = enhance_prompt(user_prompt)
                st.session_state.api_called = True
                st.session_state.enhanced_prompt = enhanced_prompt
                update_usage_date()

with col2:
    st.markdown("""
        <div class="card">
            <h3>Enhanced Prompt</h3>
            <p>Your optimized prompt will appear here:</p>
        </div>
    """, unsafe_allow_html=True)
    
    if 'enhanced_prompt' in st.session_state:
        st.text_area("", value=st.session_state.enhanced_prompt, height=200)
        st.success("✨ Your prompt has been enhanced successfully!")
        
        # Add copy button
        if st.button("📋 Copy to Clipboard"):
            st.code(st.session_state.enhanced_prompt, language="text")
            st.success("Copied to clipboard!")
    else:
        st.info("Your enhanced prompt will appear here after clicking the 'Enhance Prompt' button.")

# Footer with enhanced styling
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ for the community</p>
        <p>Free users are limited to one enhancement per day.</p>
        <p>Want more? Drop a DM at <a href="https://www.instagram.com/rethinkgenai/" target="_blank">@rethinkgenai</a> for unlimited enhancements!</p>
        <p style="font-size: 0.8rem; color: #666;">Version 1.0.0</p>
    </div>
""", unsafe_allow_html=True) 
