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
        print(e)
    df = pd.concat(e)
    if to_csv == True:
        return df.to_csv('df.csv')
    else:
        return df
    
def entity_article(kg_df):
    b = str(kg_df['result.detailedDescription.articleBody'].explode().to_list())
    doc = nlp(b)
    spacy.displacy.render(doc, style="ent")

def main():
    # Store the initial value of widgets in session state

    qry = st.text_input(
        "What do you want to find the top related queries for?\n",
        "type here",
        key="query",
    )

    if qry:
        topicalEntities(qry, to_csv=True)
        df = pd.read_csv('df.csv')
        df[['resultScore','result.description','result.name','result.detailedDescription.articleBody']]

        print("visualizing")
        st.title(f"{qry} Knowledge Graph")  # add a title
        st.write(df)  # visualize my dataframe in the Streamlit app
        print("done visualizing")
    
main()
