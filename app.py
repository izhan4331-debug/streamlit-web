import streamlit as st
from pymongo import MongoClient

# ---------------- MONGODB CONNECTION ----------------
client = MongoClient("mongodb://localhost:27017/")

db = client["user_database"]

collection = db["users"]

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
}

.stButton button {
    width: 100%;
    background-color: blue;
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
with st.container():

    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    name = st.text_input("👤 Full Name")

    phone = st.text_input("📱 Phone Number")

    email = st.text_input("📧 Email")

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password"
    )

    submit = st.button("Register")

    if submit:

        if password != confirm_password:
            st.error("❌ Passwords do not match")

        else:

            user_data = {
                "name": name,
                "phone": phone,
                "email": email,
                "password": password
            }

            collection.insert_one(user_data)

            st.success("✅ Registration Successful")
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)