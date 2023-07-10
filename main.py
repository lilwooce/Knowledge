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

cookies = {
    'S': 'billing-ui-v3=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9:billing-ui-v3-efe=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9',
    'SEARCH_SAMESITE': 'CgQI95cB',
    'HSID': 'AgPfyHQuf2mpbP77X',
    'SSID': 'AUisvhCqrudaKPKkm',
    'APISID': 'dB7h4s41TqZQkkvn/AfpigwCHLIP0MuBlt',
    'SAPISID': 'r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f',
    '__Secure-1PAPISID': 'r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f',
    '__Secure-3PAPISID': 'r1mfG0zXPJrOgPH8/ARMT0G-SOicT3Di-f',
    'SID': 'YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdglYY99p7yd0TxAz-Ez345cw.',
    '__Secure-1PSID': 'YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdg72eQZCX3Pxlmd2UoS1yW6g.',
    '__Secure-3PSID': 'YgjnfqPbgulFW50B5FmEIOmFBxJ_zaARw8WUq1XK7eLQUBdg_HnVbbZkKYgTK_1KuEHG9A.',
    'AEC': 'Ad49MVH7gqncLvk6plDE3CxCnTdEYv0sfi2UevfuNDCe_A6TaLIUSJnYJQ',
    'NID': '511=BGsUTReOPBxvWhjc5k0vHVZCp5RZifUc4LHWfvO6OdonmTXQz7UF0JX2xmZHQUXT56r1jARvWXG7F1x9Po-xM5Xe-9yY3LqGmtAHFxzn7NKEPgeAjrbsqMNZAs_qDWN2EgRcv694f5-q1Da1jZqWcR0D8ybptz3NP2qco6qO1ij_8LYpD6uajVtM5S1XiIVo0FbXCzLLsltpbkCDset0wO75IWx0hSOmAebBAmXvJennLD3LmaPxGoEVQA93B2dEdpgqExdV3qqqGZPIz25k6xY0XwJtCWt4l4h8ZXvRoZOkl7bTG7WBtgAqffcDfPAZnnG4QzGFkMjEVQqxlARHRzkUM-is5cwqwD4KUJfQOPcfQf0XTYRBKM7qh6Qv98CjO3lqD8OLJDslcTQNuabFBSQU8MzV7njvKL0vttW60n-Oi1hRrOQyFF-RJUyEnbHp0un1YXebgsHyonL-trOmfSririmThA4pRwDV8MR27dPZ5wxJf6oghyHI6_pdDJ4CDJcotuXq_0ua6ZSlJcwSKZdYuKnrXQUKGAmDL1TaUxABOFkFtC4AYAj0FntBf8GU6l-Znhwd8ed0dcKKQIqMU-4ruI_XrcgG',
    '1P_JAR': '2023-07-10-15',
    'OTZ': '7111660_72_76_104100_72_446760',
    '__Secure-1PSIDTS': 'sidts-CjEBPu3jIZ0XQMu8DNKyiB9LkC4sP67hIp2Go-bhEK0QB9PDDx6Q7vgjCZZAj7SZduf_EAA',
    '__Secure-3PSIDTS': 'sidts-CjEBPu3jIZ0XQMu8DNKyiB9LkC4sP67hIp2Go-bhEK0QB9PDDx6Q7vgjCZZAj7SZduf_EAA',
    'SIDCC': 'APoG2W83fSJwx3ucYKgGU52TupNcnMQNkxtw76X3-8juwczMyDonHtAMr4YDOuys-NVBqBVArg',
    '__Secure-1PSIDCC': 'APoG2W-Zya3Q9ZFFFJhhYua-HKg9UR04hQ5lHOIqaXQ7BoRjyiMPjs2i83-wxN2bO-lx8UZgt_s',
    '__Secure-3PSIDCC': 'APoG2W96DIGLE0wzEUOJBhHm3v4I1hWQGsfzrIDZ08qfxV-P5iJJclWi6G9d3MOfIJ0PERnKawk',
}

class CookieTrendReq(TrendReq):
    def GetGoogleCookie(self):
        return dict(filter(lambda i: i[0] == 'NID', cookies.items()))

def topicalEntities(query, to_csv=True):
    pytrends = TrendReq(hl='en-US', tz=360)
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




