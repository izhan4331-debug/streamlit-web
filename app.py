import streamlit as st
from pymongo import MongoClient

# ---------------- MONGODB CONNECTION ----------------
# Note: Agar aap Streamlit Cloud par hain to localhost kaam nahi karega.
# Local testing ke liye ye sahi hai.
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["user_database"]
    collection = db["users"]
except Exception as e:
    st.error(f"Database Connection Error: {e}")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Registration Form",
    page_icon="📝",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.form-container {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    color: black;
}
.stButton button {
    width: 100%;
    background-color: #0000FF;
    color: white;
    height: 45px;
    border-radius: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📝 Registration Form")

# ---------------- FORM ----------------
# st.form use karne se indentation ke masle kam ho jate hain
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    with st.form("my_form"):
        name = st.text_input("👤 Full Name")
        phone = st.text_input("📱 Phone Number")
        email = st.text_input("📧 Email")
        password = st.text_input("🔑 Password", type="password")
        confirm_password = st.text_input("🔒 Confirm Password", type="password")
        
        submit = st.form_submit_button("Register")

        if submit:
            if not name or not email or not password:
                st.error("❌ Please fill all required fields")
            elif password != confirm_password:
                st.error("❌ Passwords do not match")
            else:
                user_data = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "password": password
                }
                # Data insertion
                collection.insert_one(user_data)
                st.success("✅ Registration Successful")
                st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
