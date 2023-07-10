import os
import streamlit as st
from advertools import knowledge_graph
import pytrends
import pandas as pd
import spacy
import pytrends
from pytrends.request import TrendReq
import streamlit as st
key = st.secrets["KG_API_KEY"]

def topicalEntities(query, to_csv=True):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[query], cat=184, timeframe="today 12-m")
    relTop = pytrends.related_topics()
    topRelated = relTop.get(query).get('top')
    topTopics = topRelated['topic_title'].explode().to_list()
    g = knowledge_graph(key=key, query=query)
    e = []
    e.append(g)
    for f in topTopics:
        g = knowledge_graph(key=key, query=f)
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
        key="query",
    )

    if qry:
        topicalEntities(str(qry), True)
        ı = pd.read_csv('ı.csv')

        st.title(f"{qry} Knowledge Graph")  # add a title
        st.write(ı)  # visualize my dataframe in the Streamlit app
    
main()
