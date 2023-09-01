import sqlite3
from random import random

from PIL import Image
import streamlit as st

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

st.set_page_config(
    page_title="Sentiment Analysis on Online Ecommerce Products", page_icon=":tada:", layout="wide"
)
# --- Load ASSETS ---
image_headphones = Image.open("images/headphones.jpeg")
image_liquidsauce = Image.open("images/liquid-sauce.jpeg")
image_liquidspray = Image.open("images/liquid-spray.jpg")
image_oreo = Image.open("images/oreo.jpeg")
img = ["images/headphones.jpeg", "images/liquid-sauce.jpeg", "images/liquid-spray.jpg"]


# def comments(key):
#     id = key
#     if st.button("comment"):
#         st.write("Write a comment on the product")
#         st.text_input("Review")
#         if st.button("Submit"):
#             st.success("Thank you for your feedback")
#
#
# # --Header Section ---
# st.title('Reviews about your various products you get online')
# with st.container():
#     st.write("----")
#     st.header("Products")
#     st.write("##")
#
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.image("images/headphones.jpeg")
#         st.write("this is a pair of headphones")
#         comments(key="1")
#     with col2:
#         st.image("images/liquid-sauce.jpeg")
#         st.write("food stuffs")
#         comments(key="2")
#     with col3:
#         st.image("images/liquid-spray.jpg")
#         st.write("a bottle of liquid spray")
#         comments(key="3")

# import sqlite3
# import streamlit as st
# from PIL import Image
#
# conn = sqlite3.connect('product_reviews.db', check_same_thread=False)
# cur = conn.cursor()
# st.title("Sign in")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
# with image_column:
#     user_profile = Image.open("images/user-profile.jpg")
#     st.image(user_profile)
#     with text_column:
#         st.subheader("User Login")
#         def loginUser():
#             st.write("Write a review about the product :pencil2:")
#             with st.form(key="product2"):
#                 usr_review = st.text_input("Enter username")
#                 usr_review = st.text_input("Enter password")
#                 submission = st.form_submit_button("submit")
#                 if submission == True:
#                     st.success("Successfully logged in")
#                     addData(review=usr_review)
#
#         def addData(review):
#             cur.execute(""" CREATE TABLE IF NOT EXISTS users(REVIEW BLOB(200));""")
#             cur.execute("INSERT INTO users VALUES(?)", (review,))
#             conn.commit()
#             conn.close()
#             st.success("Successfully saved")
#
#         loginUser()
import sqlite3

import streamlit as st
from PIL import Image
import pickle

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()


def create_usertable():
    cur.execute('CREATE TABLE IF NOT EXISTS users(username TEXT NOT NULL, password TEXT NOT NULL)')


def add_userdata(username, password):
    cur.execute('INSERT INTO users(username,password) VALUES (?, ?)', (username, password))
    conn.commit()


def login_user(username, password):
    cur.execute('SELECT * FROM users WHERE username =? AND password = ?', (username, password))
    data = cur.fetchall()
    return data


def view_all_users():
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    return data


def main():
    """Login user page"""
    st.title("Account Signup")
    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox("Account Authentication", menu)

    if choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            create_usertable()
            result = login_user(username, password)
            if result:
                st.success("Successfully logged in as {}".format(username))
                with st.container():
                    st.write("----")
                    st.header("Products")
                    st.write("##")
                    image_column, text_column = st.columns((1, 2))
                with image_column:
                    # insert an image
                    image_oreo = Image.open("images/oreo.jpeg")
                    st.image(image_oreo)
                    with text_column:
                        st.subheader("Review on, product")

                        def newForm():
                            with st.form(key="review"):
                                review = st.text_input("comment here")
                                submission = st.form_submit_button("Submit")
                                if submission == True:
                                    st.success("Thanks for the feedback")

                        newForm()
            else:
                st.warning("Incorrect Username or Password")



    if choice == "SignUp":
        st.subheader("Create a New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, new_password)
            st.success("You have successfully created an account")
            st.info("Go to login menu")



if __name__ == '__main__':
    main()
