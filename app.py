import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

#create engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database
Base = automap_base()

#reflect cont
Base.prepare(engine, reflect=True)

#Check reflection
#print(Base.classes.keys())

#Create references to SQL tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#create databse session
session = Session(engine)

#create flask app
app = Flask(__name__)

#create route
@app.route('/')
def welcome():
    return(

        '''
        
        Welcome to the climate analysis API
        
        Available Routes

        /api/v1.0/precipitation

        /api/v1.0/stations

        /api/v1.0/tobs

        /api/v1.0/temp/start/end
        
        
        '''
    )

if __name__ == '__main__':
    app.run(debug=True)