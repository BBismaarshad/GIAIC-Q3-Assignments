import streamlit as st
import json
import os

USERS_FILE = "users.json"

# Load existing users from the file
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save new users to the file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

# Auth Section UI and Logic
def auth_section():
    st.sidebar.title("🔐 Login / Sign Up")
    users = load_users()

    # Already logged in
    if "auth_user" in st.session_state:
        st.sidebar.success(f"Logged in as {st.session_state['auth_user']}")
        if st.sidebar.button("🔓 Logout"):
            del st.session_state["auth_user"]
            st.sidebar.info("You have been logged out.")
        return

    # Login or Sign Up mode
    auth_mode = st.sidebar.radio("Select Action", ["Login", "Sign Up"])
    username = st.sidebar.text_input("Username")
    email = st.sidebar.text_input("Email") if auth_mode == "Sign Up" else ""
    password = st.sidebar.text_input("Password", type="password")

    if auth_mode == "Login":
        if st.sidebar.button("Login"):
            if username in users and users[username]["password"] == password:
                st.session_state["auth_user"] = username
                st.sidebar.success(f"Welcome back, {username}!")
            else:
                st.sidebar.error("Invalid username or password.")
    else:  # Sign Up
        if st.sidebar.button("Sign Up"):
            if username in users:
                st.sidebar.error("Username already exists.")
            elif username and email and password:
                users[username] = {"email": email, "password": password}
                save_users(users)
                st.session_state["auth_user"] = username
                st.sidebar.success(f"Account created for {username}!")
            else:
                st.sidebar.error("Please fill in all fields.")