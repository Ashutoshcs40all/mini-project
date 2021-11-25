import streamlit as st
from database import MedicineDetails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
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
     
     CustomerN_v = st.sidebar.text_input("Customer Name ")
     MedicineN_v = st.sidebar.text_input("Medicine Name ")
     ManufeDate_v = st.sidebar.date_input("Manufector Date ")
     PuraDate_v = st.sidebar.date_input("Puraching Date ")
     MedicineStock_v = st.sidebar.text_input("Medicine Stock ")
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
   
    st.bar_chart(MedicineDetails.set_index('MedicineN')['MedicineStock'])


    col1, col2, col3, col4, col5, col6, col7  = st.columns(7)

    col1.subheader("Id")
    col2.subheader("Customer Name")
    col3.subheader("Medicine Name")
    col4.subheader("Manufector Date")
    col5.subheader('Puraching Date')
    col6.subheader('Medicine Stock')  
    col7.subheader('Return Date')  

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
        col8, col9, col10, col11, col12, col13, col14 = st.columns(7)
        if res:
            col8.text(res.id) 
            col9.text(res.CustomerN)
            col10.text(res.MedicineN)
            col11.text(res.ManufeDate)
            col12.text(res.PuraDate)
            col13.text(res.MedicineStock)
            col14.text(res.ReturnDate)

#def get_input():
    # col15.subheader("Medicine Name")  
     #col16.subheader("Medicine Stock")    



if selOption == options[0]:
    showDetails()
elif selOption == options[1]:
    searchMedicine()

del_id= st.number_input("Enter id to delete")
del_btn = st.button("Delete")

if del_id and del_btn:
          to_delete = session.query(MedicineDetails).filter_by(id=del_id).first()
          session.delete(to_delete)
          session.commit()
          st.success('Data Deleted')    




