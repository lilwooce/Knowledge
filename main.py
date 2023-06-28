import os
import streamlit as st
from advertools import knowledge_graph
import pytrends
import pandas as pd
import spacy
import pytrends
from pytrends.request import TrendReq
import streamlit as st
nlp = spacy.load("en_core_web_sm")
key = os.getenv("KG_API_KEY")

def topicalEntities(query, to_csv=True):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload(kw_list=[query], cat=184, timeframe="today 12-m")
    relTop = pytrends.related_topics()
    topRelated = relTop.get(query).get('top')
    topTopics = topRelated['topic_title'].explode().to_list()
    e = []
    for f in topTopics:
        g = knowledge_graph(key=key, query=query)
        e.append(g)
    ı = pd.concat(e)
    if to_csv == True:
        return ı.to_csv('ı.csv')
    else:
        return ı

def main():
    # Store the initial value of widgets in session state

    qry = st.text_input(
        "What do you want to find the top related queries for?\n",
        "type here",
        key="query",
    )
    
    if qry:
        topicalEntities(qry, to_csv=True)
    
main()
