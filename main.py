import streamlit as st
import sqlite3
import os
from datetime import datetime
from prompt_enhancer import enhance_prompt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (ip_address TEXT PRIMARY KEY, 
                  usage_count INTEGER DEFAULT 0,
                  last_used TIMESTAMP)''')
    conn.commit()
    conn.close()

# Check user usage
def check_user_usage(ip_address):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT usage_count FROM users WHERE ip_address = ?', (ip_address,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

# Update user usage
def update_user_usage(ip_address):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO users (ip_address, usage_count, last_used)
                 VALUES (?, COALESCE((SELECT usage_count + 1 FROM users WHERE ip_address = ?), 1), ?)''',
              (ip_address, ip_address, datetime.now()))
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Set page config
st.set_page_config(
    page_title="Prompt Enhancer Pro",
    page_icon="✨",
    layout="wide"
)

# Add Google Ads
st.markdown("""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=YOUR-ADS-CLIENT-ID" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

# Main title
st.title("✨ Prompt Enhancer Pro")
st.markdown("Transform your prompts into powerful, effective instructions using AI!")

# Get user's IP address (in production, use proper IP detection)
ip_address = "127.0.0.1"  # This should be replaced with actual IP detection

# Check if user has usage remaining
usage_count = check_user_usage(ip_address)
remaining_uses = 2 - usage_count

# Input section
st.subheader("Enter Your Prompt")
user_prompt = st.text_area("Your prompt:", height=150)

if st.button("Enhance Prompt"):
    if not user_prompt:
        st.error("Please enter a prompt to enhance!")
    else:
        if remaining_uses > 0:
            # Process the prompt
            enhanced_prompt = enhance_prompt(user_prompt)
            
            # Display results
            st.subheader("Enhanced Prompt")
            st.write(enhanced_prompt)
            
            # Update usage
            update_user_usage(ip_address)
            
            # Show remaining uses
            st.info(f"You have {remaining_uses - 1} enhancement(s) remaining.")
        else:
            st.error("You have reached the maximum number of enhancements (2). Please try again later!")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using AI</p>
        <p>© 2024 Prompt Enhancer Pro. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True) 