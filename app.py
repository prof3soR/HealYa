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
             background-image: url("https://weareluminate.co/wp-content/uploads/2022/05/Blank-1250-x-800.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


col1, col2 = st.columns([1,4])

with col1:
    st.image('mind.png',width=100)

with col2:
    st.title("Thank you for joining HealYa",anchor=None)


st.write("This is HealYa's confession page")
st.write("This is a safe and secure place for to take a mental heath status test and talk about it and help us help you get the best mental health care you deserve!")
st.subheader("Take the test below to know you mental health status")
st.write("Please answer the question keeping past two weeks of activity of your life to patiently answer the qustions so that we can give you a better assesment")
st.write("On scale of 1 to 5 please select what you felt based on the question...")
Q1= st.radio("Being so restless that it is hard to sit still",(1,2,3,4,5),horizontal=True)
Q2= st.radio("Becoming easily annoyed or irritable",(1,2,3,4,5),horizontal=True)
Q3= st.radio("Feeling bad about yourself - or that you are a failure or have let yourself or your family down",(1,2,3,4,5),horizontal=True)
Q4= st.radio("Thoughts that you would be better off dead, or of hurting yourself and Little interest or pleasure in doing things ",(1,2,3,4,5),horizontal=True)
Q5= st.radio("I find it difficult to get a hold of my thoughts",(1,2,3,4,5),horizontal=True)
Q6= st.radio("Felt guilty or unable to stop blaming yourself or others for the event(s) or any problems the event(s) may have caused?",(1,2,3,4,5),horizontal=True)
Q7= st.radio("Tried hard not to think about the event(s) or went out of your way to avoid situations that reminded you of the event(s)?",(1,2,3,4,5),horizontal=True)
Q8= st.radio("Felt numb or detached from people, activities, or your surroundings?",(1,2,3,4,5),horizontal=True)
Q9= st.radio("Can't stop overthinking and ruining even good things happening",(1,2,3,4,5),horizontal=True)
Q10= st.radio("Others don't believe me when I tell them the things I see or hear",(1,2,3,4,5),horizontal=True)
            

def get_score(x):
    if x<=10:
        st.write("You have a Excellent state of mental health")
    elif x<=15:
        st.write("You have a Good state of mental health")
    elif x<=30:
        st.write("Your Mental health state is Average please let us help you!")
    elif x<=40:
        st.write("Your Mental health state is Below Average please let us help you!")
    else:
        st.write("You have a bad state of mental health please let us help you!")

score=0
score=Q1+Q2+Q3+Q4+Q5+Q6+Q7+Q8+Q9+Q10
        
if st.button("Get score",type="primary"):
    get_score(score)
 
sym=[]
st.subheader("If you're struggling with mental health, we've got you covered.Now that you know your state of mental health, take a moment and pick your symptoms and check the boxes that are relevant to you. ")
s1=st.checkbox("Feeling sad or down")
s2=st.checkbox("Confused thinking or reduced ability to concentrate")
s3=st.checkbox("Excessive fears or worries")
s4=st.checkbox("Extreme mood changes of highs and lows")
s5=st.checkbox("Withdrawal from friends and activities")
s6=st.checkbox("Loneliness")

sym=[]

if s1:
    sym.append('sad')
if s2:
    sym.append('confusion')
if s3:
    sym.append('fears')
if s4:
    sym.append('mood_changes')
if s5:
    sym.append('withdrawal')
if s6:
    sym.append('loneliness')
    
sym=','.join(sym)

st.text("We want you to know that we care about you and your well-being, and we want to help you get through whatever is bothering you right now. If there's anything we can do, just let us know.")
st.text("You don't have to tell us what's wrong; we just need to know how much it's affecting your life and how much of an impact it has on your moods.")
st.text("You can tell us anything about yourself or any personal life at all, and we will not reveal anything about you.We want to help!")
confession=st.text_area("Confession box",placeholder="You can confess your feeling here (completely anonymous)",height=1)


#score
#sym
#confession

def insert():
    import mysql.connector
    from datetime import datetime
    now = datetime.now()
    mydb = mysql.connector.connect(
      host="healya.c1wddsheroly.ap-northeast-1.rds.amazonaws.com",
      user="rohit",
      password="healyaro",
      database="bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT user_id FROM user;")
    myresult = mycursor.fetchall()
    id=myresult[-1][0]
    new_id=id+1
    mycursor = mydb.cursor()
    mycursor.execute("SELECT con_id FROM confessions;")
    myresult = mycursor.fetchall()
    con_id=myresult[-1][0]
    new_con_id=con_id+1
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    now=formatted_date.split()[0]
    sql = "INSERT INTO user(user_id,doj,test_score,feelings) VALUES (%s,%s,%s,%s);"
    val=(new_id,now,score,sym)
    sql1 = "INSERT INTO confessions(con_id,user_id,confession) VALUES (%s,%s,%s);"
    val1=(new_con_id,new_id,confession)
    try:
        mycursor.execute(sql, val)
        mycursor.execute(sql1,val1)
        mydb.commit()
        st.write("SUCCESS!")
    except:
        mydb.rollback()
        st.write("Failed!")
    
    mydb.close()
    

if st.button("Submit",type="primary"):
    insert()




    
    
