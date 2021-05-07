import pandas as pd
import numpy as np
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from geopy.geocoders import Nominatim
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier


def maps():
    df = pd.read_csv("dataset.csv")
    geolocator = Nominatim(user_agent="analysisapp")
    lat_long = []
    cities=df["City"].unique().tolist()
    for i in cities:
        print(i)
        location = geolocator.geocode(i,timeout=2000)  # "California")
        print(location)
        if location != None:
            latitude = location.latitude
            longitude = location.longitude
            latLong = [latitude, longitude]
            values = {
                "latLng": latLong,
                "name": i
            }

            lat_long.append(values)
    return lat_long

