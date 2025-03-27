import streamlit as st
import time
import requests
import random
import base64

st.set_page_config(page_title="Money making machine", page_icon="💰", layout="centered")
st.title("Money Making Machine💴💲")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
# Add background image using st.image and CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{get_base64_of_image("image.png")});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



def generate_money():
    return random.randint(1, 1000)

st.subheader("**Instant cash generator**")
if st.button("**💰Generate Money💴**"):
    st.write("Counting your money...")
    time.sleep(1)                    # sleep def use for delay time
    amount = generate_money()
    st.success(f"**You made ${amount}**")       #dollar $ is use to show $ symbol with amount

def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustle?apikey=12345')
        if response.status_code == 200:
            hustle = response.json()
            return hustle["side_hustle"]
        else: 
            return ("Freelancing")
    except:
        return ("Something went wrong!")

st.subheader("**Side Hustle Ideas**")
if st.button("**💲📈Generate Profitable Hustles**"):
    idea = fetch_side_hustle()
    st.success(f"**{idea}**")

# money making motivation

def fetch_money_quotes():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?apikey=1234')
        if response.status_code == 200:
            quoets = response.json()
            return quoets["money_quotes"]
        else:
            return ("Money is the root of all evils")
    except:
        return ("Something went wrong!")
    
if st.button("**💸Hustle for Money Motivation**"):
    quotes = fetch_money_quotes()
    st.info(f"**{quotes}**")
    

