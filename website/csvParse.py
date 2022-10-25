from flask import render_template, request, redirect, url_for
import pandas as pd
from sqlalchemy import create_engine


from . import db


def parseCSV(file_path):
    #get the data from the csv
    csvData=pd.read_csv(file_path, header=1)
    #loop through the rows
    for i, row in csvData.iterrrows():
        
        value = (row['email'], row['password'],['role']) 
        mycursor = db.cursor()
        mycursor.execute(sql,value,if_exsists='append')
        db.commit()


