import streamlit as st
from pymongo import MongoClient

# ---------------- CONFIG & THEME ----------------
st.set_page_config(page_title="Pro Registration", page_icon="👤", layout="wide")

# Custom CSS for a modern look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .st-emotion-cache-1r6slb0 { border-radius: 15px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #0056b3; border: none; }
    </style>
    """, unsafe_allow_html=True)

# ---------------- APP LOGIC ----------------
def registration_form():
    # Sidebar for extra info
    with st.sidebar:
        st.title("Assistance")
        st.info("Need help? Contact support@example.com")
        st.write("---")
        st.caption("Version 2.0.1")

    # Main Center Column
    _, col2, _ = st.columns([1, 2, 1])

    with col2:
        st.header("🚀 Create Your Account")
        st.subheader("Join our professional network today.")
        
        with st.form("reg_form", clear_on_submit=True):
            # Using columns inside the form for better spacing
            name_col, phone_col = st.columns(2)
            name = name_col.text_input("Full Name", placeholder="John Doe")
            phone = phone_col.text_input("Phone Number", placeholder="+92 XXX XXXXXXX")
            
            email = st.text_input("Email Address", placeholder="name@company.com")
            
            pass_col, confirm_col = st.columns(2)
            password = pass_col.text_input("Password", type="password")
            confirm = confirm_col.text_input("Confirm Password", type="password")
            
            # Terms and Conditions
            agree = st.checkbox("I agree to the Terms of Service")
            
            submit = st.form_submit_button("Register Now")

            if submit:
                if not agree:
                    st.warning("⚠️ Please agree to the terms.")
                elif password != confirm:
                    st.error("❌ Passwords do not match.")
                elif not name or not email:
                    st.error("❌ Name and Email are required.")
                else:
                    # Database Logic
                    # collection.insert_one({"name": name, "email": email...})
                    st.success(f"🎉 Welcome aboard, {name}! Your account is ready.")
                    st.balloons()

if __name__ == "__main__":
    registration_form()

            collection.insert_one(user_data)

            st.success("✅ Registration Successful")
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)
