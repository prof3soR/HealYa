import streamlit as st
from PIL import Image
img = Image.open('mind.png')
st.set_page_config(
    page_title="HealYa",
    page_icon=img
    )
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v960-ning-28.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=bd5ed782336be6fe2881d76eb1de6788");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.title('WELCOME TO HealYa login page')
st.write("")
st.write("")
st.write("")
def login():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="healya.c1wddsheroly.ap-northeast-1.rds.amazonaws.com",
      user="rohit",
      password="healyaro",
      database="bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select password from login where user_id={};".format(uid))
    myresult = mycursor.fetchall()
    valid=myresult
    
    if len(valid)==0:
        st.write("Invalid login")
    else:
        if pas==valid[0][-1]:
            st.write("Success!")

            
        else:
            st.write("Wrong password!")
    mydb.close()

col1, col2 = st.columns(2)

with col1:
    uid=st.text_input("User Id",placeholder="Enter Your user id (Ex:1)")
    pas=st.text_input("Password",placeholder="Enter your password")
    if st.button("Log in"):
        login()
with col2:
    st.image("login-page.jpeg")

    
