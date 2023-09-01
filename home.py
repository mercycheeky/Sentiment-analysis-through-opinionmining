import sqlite3

import streamlit as st
from PIL import Image
import pickle
import mysql.connector
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Sentiment Model", "About", "Register", "Login"],
    icons=["house", "book", "eye-fill", "person-plus", "person"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white"},
    "icon": {"color": "orange", "font-size": "25px"},
    "nav-link": {
        "font-size": "25px",
        "text-align": "left",
        "margin": "0px",
        "--hover-color": "#eee",
    },
    "nav-link-selected": {"background-color": "green"},
}
)
if selected == "Home":
    def main():
        image_headphones = Image.open("images/headphones.jpeg")
        image_liquidsauce = Image.open("images/liquid-sauce.jpeg")
        image_liquidspray = Image.open("images/liquid-spray.jpg")
        image_oreo = Image.open("images/oreo.jpeg")

    # --Header Section ---
        st.title('Reviews about your various products you get online')
        with st.container():
            st.write("----")
            st.header("Products")
            st.write("##")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("images/headphones.jpeg")
                st.write("this is a pair of headphones")
                if st.button("comment", key="count"):
                    st.write("Write a comment on the product")
                    st.text_input("Review")
                    if st.button("Submit"):
                        st.success("Thank you for your feedback")
                # comments()
            with col2:
                st.image("images/liquid-sauce.jpeg")
                st.write("food stuffs")
                if st.button("comment", key="count2"):
                    st.write("Write a comment on the product")
                    st.text_input("Review")
                    if st.button("Submit"):
                        st.success("Thank you for your feedback")

            with col3:
                st.image("images/liquid-spray.jpg")
                st.write("a bottle of liquid spray")
                if st.button("comment", key="count3"):
                    st.write("Write a comment on the product")
                    st.text_input("Review")
                    if st.button("Submit"):
                        st.success("Thank you for your feedback")

if selected == "Sentiment Model":
    import writefile as writefile
    import pickle
    import streamlit as st

    from train import vectorizer

    # loading the trained model
    pickle_in = open('classifier.pkl', 'rb')
    classifier = pickle.load(pickle_in)


    @st.cache()
    # defining the function which will make the prediction using the data which the user inputs
    def prediction(Review):
        # Making predictions
        data = vectorizer.transform([Review]).toarray()
        predictions = classifier.predict(data)

        if predictions == 0:
            pred = "Negative Review"
        else:
            pred = "Positive Review"
        return pred


    # this is the main function in which we define our webpage
    def main():
        # front end elements of the web page
        html_temp = """ 
        <div style ="background-color:grey;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Sentiment Analysis For Product Reviews</h1> 
        </div> 
        """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)

        # following lines create boxes in which user can enter data required to make prediction
        Review = st.text_input('Enter Review')
        # strength = st.selectbox('Password strength',(0, 1, 2))
        result = ""

        # when 'Predict' is clicked, make the prediction and store it
        if st.button("Predict"):
            result = prediction(Review)
            st.success('Your review is a  {}'.format(result))
            print(result)

    #
    # if __name__ == '__main__':
    #     main()
if selected == "About":
    st.title("About page")
    st.write(
        "Everyone can freely express his/her views and opinions anonymously and without the fear of consequences. Social media and online posting have made it even easier to post confidently and openly. These opinions have both pros and cons while providing the right feedback to reach the right person which can help fix the issue and sometimes a con when these get manipulated These opinions are regarded as valuable. This allows people with malicious intentions to easily make the system to give people the impression of genuineness and post opinions to promote their own product or to discredit the competitor products and services, without revealing identity of themselves or the organization they work for.The use of Opinion Mining, a type of language processing to track the emotion and thought process of the people or users about a product which can in turn help research work.2 Opinion mining, which is also called sentiment analysis, involves building a system to collect and examine opinions about the product made in social media posts, comments, online product and service reviews or even tweets. Automated opinion mining uses machine learning, a component of artificial intelligence. An opinion mining system can be built using a software that can extract knowledge from dataset and incorporate some other data to improve its performance. One of the biggest applications of opinion mining is in the online and e-commerce reviews of consumer products, feedback and services. As these opinions are so helpful for both the user as well as the seller the e-commerce web sites suggest their customers to leave a feedback and review about their product or service they purchased. These reviews provide valuable information that is used by potential customers to know the opinions of previous or current users before they decide to purchase that product from that seller. Similarly, the seller or service providers use this information to identify any defects or problems users face with their products and to understand the competitive information to know the difference about their similar competitors’ products. There is a lot of scope of using opinion mining and many applications for different usages: Individual consumers: A consumer can also compare the summaries with competing products before taking a decision without missing out on any other better products available in the market. Businesses/Sellers: Opinion mining helps the sellers to reach their audience and understand their perception about the product as well as the competitors. Such reviews3 also help the sellers to understand the issues or defects so that they can improve later versions of their product. In today’s generation this way of encouraging the consumers to write a review about a product has become a good strategy for marketing their product through real audience’s voice. Such precious information has been spammed and manipulated. Out of many researches one fascinating research was done to identify the deceptive opinion spam [3].")

if selected == "Register":
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
        st.subheader("Create a New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, new_password)
            st.success("You have successfully created an account")
            st.info("Go to login menu")
if selected == "Login":
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
if __name__ == '__main__':
    main()
