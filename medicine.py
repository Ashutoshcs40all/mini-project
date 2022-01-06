from sqlalchemy.sql.functions import current_date, current_user, user
import streamlit as st

from database import MedicineDetails
from database import userDeatails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from PIL import Image
import datetime

engine = create_engine('sqlite:///mydatabase.sqlite3')
                      
Session = sessionmaker(engine)
session = Session()
Logged_IN = False
current_user = {}

#st.write("""
# Medicine Inventory Application
#**Visually** show data on a Medicine! 
#""")



sidebar = st.sidebar


sidebar.header('Dashboard Home')

def intro():
     
     st.title('Medicine Inventory Application')
   
     st.markdown('- Simple Web Page Using Python With Streamlit library. ')
     st.caption('- Medical inventory Application is used to track medical supplies and prescription drugs within a single practice or an entire hospital system.')
     st.markdown('- We can easily understand the data using graph(via plotly and matplotlib library used).')
     st.markdown('------ ')  



def get_input():

     if not Logged_IN: 
          return

def Register():
    # if Logged_IN: 
         # return
     Names_v = st.sidebar.text_input(" Name")
     Username_v = st.sidebar.text_input("Username")
     Email_id_v = st.sidebar.text_input("Email Id")
     Password_v = st.sidebar.text_input("Password")

     btn = sidebar.button("Save UserDetails!!") 

     if btn:
          try:
               Register = userDeatails( Names = Names_v , Username = Username_v, Email_id = Email_id_v, Password = Password_v)
               
                                   
               session.add(Register)
               session.commit()

               st.success('Data Saved')
          except Exception as e:
               print(e)
               st.error('Error in saving data')         
     
     CustomerN_v = st.sidebar.text_input("Customer Name")
     MedicineN_v = st.sidebar.text_input("Medicine Name")
     ManufeDate_v = st.sidebar.date_input("Manufector Date")
     PuraDate_v = st.sidebar.date_input("Puraching Date ")
     MedicineStock_v = st.sidebar.text_input("Medicine Stock")
     ReturnDate_v= st.sidebar.date_input("Return Date ")


   
        
     btn = sidebar.button("Save Data!!")   

     if btn:
          try:
               Medicine = MedicineDetails( CustomerN = CustomerN_v, MedicineN = MedicineN_v, ManufeDate = ManufeDate_v, PuraDate = PuraDate_v, MedicineStock = MedicineStock_v, ReturnDate = ReturnDate_v)
               
                                   
               session.add(Medicine)
               session.commit()

               st.success('Data Saved')
          except Exception as e:
               print(e)
               st.error('Error in saving data')

options = ['Introduction','Add Data', 'View Data']
selOption = sidebar.selectbox('Select any option', options)               

def viewData():
     st.header('View Data Header')


if selOption == options[0]:
    intro()
elif selOption == options[1]:
     get_input()
elif selOption == options[2]:
     viewData()

    # """Medicine Inventory Application"""

    # st.title("Medicine Inventory Application")

    # menu = ["Home", "Login", "Signup"]
     #choice = st.sidebar.selectbox("Menu", menu)

     #if choice =="Home":
        #  st.sidebar("Home")

     #elif choice == "Login":
      #    st.subheader("Login Section")

        #  username = st.sidebar.text_input("User Name")    
         # password = st.sidebar.text_input("Password",type='')
         # if st.button("Login"):
            #   st.success("Logged In as{}" .format(username)) 

def showDetails():
    st.header('Medicine Data')
    st.markdown('---')

    data = session.query(MedicineDetails).all()

    df = pd.read_sql_table(table_name="Medicine Data",
                           con=session.connection(), index_col="IdNo")

    Medicine = df['MedicineN'].unique()

    selMedicine = st.selectbox('Select Medicine', Medicine)

    Medicine = df[df['MedicineN'] == selMedicine]

    Medicine_Details = df[df['MedicineN']== selMedicine]
    st.subheader("Bar chart for Medicine Stock") 
    st.bar_chart(Medicine_Details.set_index('MedicineN')['MedicineStock'])
    

    col1, col2, col3, col4, col5, col6, col7  = st.columns(7)

    col1.subheader("Id")
    col2.subheader("Customer Name")
    col3.subheader("Medicine Name")
    col4.subheader("Manufector Date")
    col5.subheader('Puraching Date')
    col6.subheader('Medicine Stock')  
    col7.subheader('Expiration    Date')  

    for entry in data:
         col1.text(entry.id)
         col2.text(entry.CustomerN) 
         col3.text(entry.MedicineN) 
         col4.text(entry.ManufeDate)
         col5.text(entry.PuraDate) 
         col6.text(entry.MedicineStock) 
         col7.text(entry.ReturnDate)

def searchMedicine():
    st.header("Search Medicine")
    st.markdown("---")

    search_Medicine = st.text_input("Enter Medicine to search")
    search_btn = st.button("Search")

    if search_Medicine and search_btn:
        res = session.query(MedicineDetails).filter_by(MedicineN=search_Medicine).first()
        col8, col9, col10, col11, col12, col13, col14 = st.columns(7)
        if res:
            col8.text(res.id)
            col9.text(res.CustomerN)
            col10.text(res.MedicineN)
            col11.text(res.ManufeDate)
            col12.text(res.PuraDate)
            col13.text(res.MedicineStock)
            col14.text(res.ReturnDate)    


def searchuser():
    st.header("Search user")
    st.markdown("---")

    search_user = st.text_input("Enter username to search")
    search_btn = st.button("Search")

     
    if search_user and search_btn:
          res = session.query(userDeatails).filter_by(Username=search_user).first()
       
          if res:(True)
                            

#if selOption == options[0]:
  #  intro()

if selOption == options[1]:
    showDetails()
elif selOption == options[2]:
   searchMedicine()

del_id= st.number_input("Enter id to delete")
del_btn = st.button("Delete")

if del_id and del_btn:
          to_delete = session.query(MedicineDetails).filter_by(id=del_id).first()
          session.delete(to_delete)
          session.commit()
          st.success('Data Deleted')       