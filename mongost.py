# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:22:38 2021

@author: admin
"""

import streamlit as st
import pymongo

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")