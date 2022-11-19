import streamlit as st
from PIL import Image
img = Image.open('mind.png')
st.set_page_config(
    page_title="HealYa Signup page",
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
             background-image: url("https://wallpaperaccess.com/full/449895.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.title('WELCOME TO HealYa sing up page')
import mysql.connector
mydb = mysql.connector.connect(
host="healya.c1wddsheroly.ap-northeast-1.rds.amazonaws.com",
user="rohit",
password="healyaro",
database="bd")

mycursor = mydb.cursor()
mycursor.execute("select user_id from login;")
myresult = mycursor.fetchall()
new_id=myresult[-1][0]+1

col1,col2=st.columns(2)
with col1:
    st.write("User id:",new_id)
    pas=st.text_input("Create Password",placeholder="Enter your password")
    pas_con=st.text_input("Confirm your Password",placeholder="Enter your password")
    if st.button("Create account"):
        if pas!=pas_con:
            st.write("Password did not match ")
        else:
            try:
                sql= "INSERT INTO login(user_id,password) VALUES (%s,%s);"
                val=(new_id,pas)
                mycursor.execute(sql, val)
                mydb.commit()
                st.write("Account created successfully!")
            except:
                mydb.rollback()
                st.write("Failed!")
        
with col2:
    st.write("")
    
    st.image("sp.jpeg")

mydb.close()

st.subheader("Click here to login !", anchor="http://18.181.181.113:8501/")


