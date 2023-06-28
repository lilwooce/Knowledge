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
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox("Disable text input widget", key="disabled")
        st.radio(
            "Set text input label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
        )
        st.text_input(
            "Placeholder for the other text input widget",
            "This is a placeholder",
            key="placeholder",
        )

    with col2:
        text_input = st.text_input(
            "Enter some text 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder,
        )

        if text_input:
            st.write("You entered: ", text_input)
    
main()
