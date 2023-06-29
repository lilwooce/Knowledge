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
key = st.secrets["KG_API_KEY"]

def topicalEntities(query, to_csv=True):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload(kw_list=[query], cat=184, timeframe="today 12-m")
    relTop = pytrends.related_topics()
    topRelated = relTop.get(query).get('top')
    print("printing top related after this")
    print(topRelated)
    topTopics = topRelated['topic_title'].explode().to_list()
    g = knowledge_graph(key=key, query=f)
    e.append(g)
    e = []
    for f in topTopics:
        print("f is below this")
        print(f)
        g = knowledge_graph(key=key, query=f)
        e.append(g)
    ı = pd.concat(e)
    
    if to_csv == True:
        return ı.to_csv('ı.csv')
    else:
        return ı
    
def entity_article(kg_df):
    b = str(kg_df['result.detailedDescription.articleBody'].explode().to_list())
    doc = nlp(b)
    spacy.displacy.render(doc, style="ent")

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
