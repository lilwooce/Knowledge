import os
from advertools import knowledge_graph
import pytrends
import pandas as pd
import spacy
import pytrends
from pytrends.request import TrendReq
nlp = spacy.load("en_core_web_sm")
key = os.getenv("KG_API_KEY")

'''love_entities = knowledge_graph(key=key, query='Love')
""" You can call these two lines in the function if you want but since these two lines are not necessary for repeated usage, we have pu thtem outside of the function. """

def entity_article(kg_df):
    b = str(kg_df['result.detailedDescription.articleBody'].explode().to_list())
    doc = nlp(b)
    spacy.displacy.serve(doc, style="ent")

entity_article(love_entities)'''

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
    qry = input("What do you want to find the top related queries for?\n")
    topicalEntities(qry, to_csv=True)

main()

'''jhlTrends = TrendReq(hl="en-US", tz=360)
jhlTrends.build_payload('Jennifer Love Hewitt', cat=0, timeframe="today 5-y")
jlh_queries = pytrends.related_queries()
#jlh_queries.get('Jennifer Love Hewitt').get('top')
jlh_entities = knowledge_graph(key=key, query="Jennifer Love Hewitt")
jlh_graph_list = jlh_entities['topic_title'].explode().to_list()

a = []
for x in jlh_graph_list:
    b = knowledge_graph(key=key, query=x)
    a.append(b)

jlh_graph_list_ = pd.concat(a)
jlh_graph_list_.head(50)'''