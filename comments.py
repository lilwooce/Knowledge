
'''love_entities = knowledge_graph(key=key, query='Love')
""" You can call these two lines in the function if you want but since these two lines are not necessary for repeated usage, we have pu thtem outside of the function. """

def entity_article(kg_df):
    b = str(kg_df['result.detailedDescription.articleBody'].explode().to_list())
    doc = nlp(b)
    spacy.displacy.serve(doc, style="ent")

entity_article(love_entities)'''



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