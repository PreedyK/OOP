import streamlit as st
from PIL import Image

col1, col2 = st.columns((4, 5))

with col1:
    st.title("My Resume")
    st.header("Kiryn Preedy")

with col2:
    image = Image.open('Kiryn-115.jpg')
    st.image(image, width=200)

st.markdown("**About Me**")
st.text("I am an Artist, Musician, and Academic Weapon")
st.text("I am Studying Computer Science at JBU")
st.divider()

st.markdown("**Education**")
st.text("I have a Highschool Diploma from Spero Academy and am studying for my BA in Computer Science")

st.markdown("**Work Experience**")
st.text("I worked at an HTeaO in my hometown and worked for my Dad's business as a data analyst")

st.markdown("**Hobbies & Interests**")
st.text("My hobbies are painting, singing, playing viola, guitar, and piano, crocheting, speending time with friends, or any other creative outlet.")

st.markdown("**Contact Me**")
st.text_input("Your Name: ")
st.text_input("Email: ")
message = st.text_area("Your Message: ")
st.button("Send Message")