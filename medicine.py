import streamlit as st
from database import MedicineDetails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from PIL import Image
import datetime


engine = create_engine('sqlite:///mydatabase.sqlite3')
                      
Session = sessionmaker(engine)
session = Session()


st.write("""
# Medicine Inventory Application
**Visually** show data on a Medicine! 
""")

image = Image.open("OIP.jpg")
st.image(image, use_column_width= True)

sidebar = st.sidebar

sidebar.header('Dashboard Home')

options = ['Add Data', 'View Data']
selOption = sidebar.selectbox('Select any option', options)

def get_input():
     
     CustomerN_v = st.sidebar.text_input("CustomerN ")
     MedicineN_v = st.sidebar.text_input("MedicineN ")
     ManufeDate_v = st.sidebar.date_input("ManufeDate ")
     PuraDate_v = st.sidebar.date_input("PuraDate ")
     MedicineStock_v = st.sidebar.text_input("MedicineStock ")
     ReturnDate_v= st.sidebar.date_input("ReturnDate ")

     
     btn = sidebar.button("Save Data!!")   

     if btn:
          try:
               Medicine = MedicineDetails( CustomerN = CustomerN_v, MedicineN = MedicineN_v, ManufeDate = ManufeDate_v, PuraDate = PuraDate_v, MedicineStock = MedicineStock_v, ReturnDate = ReturnDate_v)
               
                                   
               session.add(Medicine)
               session.commit()

               st.success('Data Saved!!')
          except Exception as e:
               print(e)
               st.error('Error in saving data')

def viewData():
     st.header('View Data Header')

if selOption == options[0]:
     get_input()
elif selOption == options[1]:
     viewData()


def showDetails():
    st.header('Medicine Data')
    st.markdown('---')

    data = session.query(MedicineDetails).all()

    df = pd.read_sql_table(table_name="Medicine Data",
                           con=session.connection(), index_col="IdNo")

    Medicine = df['MedicineN'].unique()

    selMedicine = st.selectbox('Select Medicine', Medicine)

    Medicine = df[df['MedicineN'] == selMedicine]
   

    col1, col2, col3, col4, col5, col6, col7  = st.columns(7)

    col1.subheader("Id")
    col2.subheader("CustomerN")
    col3.subheader("MedicineN")
    col4.subheader("ManufeDate")
    col5.subheader('PuraDate')
    col6.subheader('MedicineStock')  
    col7.subheader('ReturnDate')  

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
        res = session.query(MedicineDetails).filter_by(id=search_Medicine).first()
        col8, col9, col10, col11, col12, col13, col14 = st.columns(6)
        if res:
            col8.text(res.id) 
            col9.text(res.CustomreN)
            col10.text(res.MedicineN)
            col11.text(res.ManufeDate)
            col12.text(res.PuraDate)
            col13.text(res.MedicineStock)
            col14.text(res.ReturnDate)


if selOption == options[0]:
    showDetails()
elif selOption == options[1]:
    searchMedicine()


