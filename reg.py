import streamlit as st
import sqlite3
import subprocess

conn = sqlite3.connect('symtable.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS table1 (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

background_image = "https://img.freepik.com/free-photo/frame-medical-equipment-desk_23-2148519742.jpg?size=626&ext=jpg&ga=GA1.2.734836280.1694843058&semt=ais"

custom_css = f"""
<style>
    .stApp {{
        background-image: url('{background_image}');
        background-size: 100% 100%;
        background-attachment: scroll;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)



selected_option = st.sidebar.radio("Select an option", ("Sign Up", "Login"))

if selected_option == "Sign Up":
    st.title("SYMPTOMS CHECKER")
    st.title("Sign Up")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    signup_button = st.button("Sign Up")

    if signup_button:
        cursor.execute("SELECT username FROM table1 WHERE username=?", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user is None:
            cursor.execute("INSERT INTO table1 (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            st.success("User registered successfully!")
        else:
            st.error("Username already exists. Please choose another username.")

if selected_option == "Login":
    st.title("SYMPTOMS CHECKER")
    st.title("Login")

    username = st.text_input("New Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        cursor.execute("SELECT * FROM table1 WHERE username=?", (username,))
        user = cursor.fetchone()

        if user is not None:
            stored_password = user[1]
            if password == stored_password:
                st.success("Logged in as " + username)
                subprocess.run(["streamlit", "run", "app0.py"])
            else:
                st.error("Incorrect username or password")
        else:
            st.error("User not found")


conn.close()
