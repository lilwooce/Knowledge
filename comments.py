
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

'''headers = {
    'authority': 'trends.google.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'S=billing-ui-v3=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9:billing-ui-v3-efe=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9; SEARCH_SAMESITE=CgQI95cB; HSID=AgPfyHQuf2mpbP77X; SSID=AUisvhCqrudaKPKkm; APISID=dB7h4s41TqZQkkvn/AfpigwCHLIP0MuBlt; SAPISID=r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f; __Secure-1PAPISID=r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f; __Secure-3PAPISID=r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f; SID=YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdglYY99p7yd0TxAz-Ez345cw.; __Secure-1PSID=YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdg72eQZCX3Pxlmd2UoS1yW6g.; __Secure-3PSID=YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdg_HnVbbZkKYgTK_1KuEHG9A.; AEC=Ad49MVH7gqncLvk6plDE3CxCnTdEYv0sfi2UevfuNDCe_A6TaLIUSJnYJQ; NID=511=BGsUTReOPBxvWhjc5k0vHVZCp5RZifUc4LHWfvO6OdonmTXQz7UF0JX2xmZHQUXT56r1jARvWXG7F1x9Po-xM5Xe-9yY3LqGmtAHFxzn7NKEPgeAjrbsqMNZAs_qDWN2EgRcv694f5-q1Da1jZqWcR0D8ybptz3NP2qco6qO1ij_8LYpD6uajVtM5S1XiIVo0FbXCzLLsltpbkCDset0wO75IWx0hSOmAebBAmXvJennLD3LmaPxGoEVQA93B2dEdpgqExdV3qqqGZPIz25k6xY0XwJtCWt4l4h8ZXvRoZOkl7bTG7WBtgAqffcDfPAZnnG4QzGFkMjEVQqxlARHRzkUM-is5cwqwD4KUJfQOPcfQf0XTYRBKM7qh6Qv98CjO3lqD8OLJDslcTQNuabFBSQU8MzV7njvKL0vttW60n-Oi1hRrOQyFF-RJUyEnbHp0un1YXebgsHyonL-trOmfSririmThA4pRwDV8MR27dPZ5wxJf6oghyHI6_pdDJ4CDJcotuXq_0ua6ZSlJcwSKZdYuKnrXQUKGAmDL1TaUxABOFkFtC4AYAj0FntBf8GU6l-Znhwd8ed0dcKKQIqMU-4ruI_XrcgG; 1P_JAR=2023-07-10-15; OTZ=7111660_72_76_104100_72_446760; __Secure-1PSIDTS=sidts-CjEBPu3jIZ0XQMu8DNKyiB9LkC4sP67hIp2Go-bhEK0QB9PDDx6Q7vgjCZZAj7SZduf_EAA; __Secure-3PSIDTS=sidts-CjEBPu3jIZ0XQMu8DNKyiB9LkC4sP67hIp2Go-bhEK0QB9PDDx6Q7vgjCZZAj7SZduf_EAA; SIDCC=APoG2W83fSJwx3ucYKgGU52TupNcnMQNkxtw76X3-8juwczMyDonHtAMr4YDOuys-NVBqBVArg; __Secure-1PSIDCC=APoG2W-Zya3Q9ZFFFJhhYua-HKg9UR04hQ5lHOIqaXQ7BoRjyiMPjs2i83-wxN2bO-lx8UZgt_s; __Secure-3PSIDCC=APoG2W96DIGLE0wzEUOJBhHm3v4I1hWQGsfzrIDZ08qfxV-P5iJJclWi6G9d3MOfIJ0PERnKawk',
    'origin': 'https://trends.google.com',
    'referer': 'https://trends.google.com/trends/explore?date=now%201-d&geo=US&q=Apple&hl=en',
    'sec-ch-ua': '"Opera GX";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"99.0.4788.86"',
    'sec-ch-ua-full-version-list': '"Opera GX";v="99.0.4788.86", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
}'''