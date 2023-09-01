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


if __name__ == '__main__':
    main()
