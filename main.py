import os
import streamlit as st
from advertools import knowledge_graph
import pandas as pd
import spacy
import pytrends
from pytrends.request import TrendReq as UTrendReq
GET_METHOD='get'
key = st.secrets["KG_API_KEY"]

class TrendReq(UTrendReq):
    def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
        return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

headers = {
    'authority': 'trends.google.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'S=billing-ui-v3=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9:billing-ui-v3-efe=grQmoRiI50g8IVgg5iDCxdLbRDvXYnz9; SEARCH_SAMESITE=CgQI95cB; OTZ=7111660_72_76_104100_72_446760; SID=YwjnfmbLrKheYvabw3fC90EzIX2DA0Fh-rkG9HuoR81JDFYeImEYHOMqsYQ4dmZIw2R5VQ.; __Secure-1PSID=YwjnfmbLrKheYvabw3fC90EzIX2DA0Fh-rkG9HuoR81JDFYeWyZMQVzB_nsWrLm-fYz9RA.; __Secure-3PSID=YwjnfmbLrKheYvabw3fC90EzIX2DA0Fh-rkG9HuoR81JDFYeUsYuQbDjpfO4Cwn5C-x38g.; HSID=A4mZvl3mulzudMnI7; SSID=ARergqdrmtLt0FEst; APISID=hTBTpg5Ol-xMJAba/Aizi4hnL8IhTvm6Tb; SAPISID=TSyThzzc7l-42ZW2/AvgsX2_YYEyE61Wlb; __Secure-1PAPISID=TSyThzzc7l-42ZW2/AvgsX2_YYEyE61Wlb; __Secure-3PAPISID=TSyThzzc7l-42ZW2/AvgsX2_YYEyE61Wlb; AEC=Ad49MVE9bdQ84x_10caHtLmjVC4zttyJEYjbNIVtZk4JySBMXRyLdqBjLg; NID=511=FE1YGW_koU4GIPlukp_FMPIk40e_dDbwCpJ9b8_4LeemV3VwUBkD4VuzI51M_GXWicYLQN255B80_15DnMJgCByKccaXIE2cEiCQ2hQbr96XC7KtF2NIaiQsw9HklbC_2R4Dx4OdtGuszEl3Ctx8b7UXiHHraXCpysRiDHx-wt8EyHRfhzDOcN0fT0jB0IcigK8buqKa9SRHgsj4RB7ZOOoCy0SAt3nvIG4kU__SCN_FinAtZLkjfHeM2_XfmgkN8eS7-NhwYeis1q0j76FwWGJtpntZ7HKh3J2zqm7NVXvPsAubwhkDNEJoplDYR2lQZpRIaGgqR0XbUJtGMspwnUwRjtQuXmj2tCF64_K9VN0Fcm66z6zdzRjfuDaqydf3rBQ3EU3aSVzS_T9OphI0SaFpOI5Ur-QKk_p-9F4GApIdtoIwjB1HmGXLe2Lw_hSo_vdwf6nlu6b1gc8WxtCDPdAzkWrPPTp13ABZyn_IMPaTrNFiTlHJsJqZefvieskyJPmQzH2WVi1FmXRgcqSZ0nHcphUK-tpz_Wr0RriExZIuLpOoj7WPeP2uBs8JzOJRLys8TgIvsiAF00FHZNggSs_-wbWDULvR38xCrv8SSmiK_43ai8CYIiQz1bIawRT7TWYef6eoZA; __Secure-1PSIDTS=sidts-CjEBPu3jIerAjzmXteZx-B-ifgdiDfKzUo_KMbRqQb2D6hlaZud3BsLKyF2PrCPB6eVREAA; __Secure-3PSIDTS=sidts-CjEBPu3jIerAjzmXteZx-B-ifgdiDfKzUo_KMbRqQb2D6hlaZud3BsLKyF2PrCPB6eVREAA; 1P_JAR=2023-07-19-23; SIDCC=APoG2W9C1S7vC4vn9-gIiqzzUsZbVHxkJbUVqdl6q94txNISnBF08Fxc5UXndR2Lmz50HOB-QH8; __Secure-1PSIDCC=APoG2W-5BYdgYooyeE6tiqBA-jQy4BMUueGniCjEvBwaOe2r4GUKWML8_YTLfZLbMgSjvi7rlOKw; __Secure-3PSIDCC=APoG2W_9TBiFaAJRCo8IjB90AxuVy7hFn327S2DB_jIclaWka4iWK9E7CnmhX8C77IzOH2ovGgDN',
    'referer': 'https://trends.google.com/trends/explore?date=now%201-d&geo=US&q=Cars&hl=en',
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
}

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

def relEntities(qry, to_csv=True):
    g = knowledge_graph(key=key, query=qry)
    e=[]
    e.append(g)
    ı = pd.concat(e)

    if to_csv == True:
        return ı.to_csv('ı.csv')
    else:
        return ı

def relQueries(query):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=[query], cat=184, timeframe="today 12-m")
    relTop = pytrends.related_topics()
    topRelated = relTop.get(query).get('top')
    topTopics = topRelated['topic_title'].explode().to_list()
    return topTopics

def main():
    # Store the initial value of widgets in session state

    qry = st.text_input(
        "What do you want to find the top related entities and queries for?\n",
        key="query",
    )
    relQry = st.text_input(
        "What do you want to find the top related queries for?\n",
        key="relQuery",
    )

    if qry:
        relEntities(str(qry), True)
        ı = pd.read_csv('ı.csv')

        st.title(f"{qry} Knowledge Graph")  # add a title
        st.write(ı)  # visualize my dataframe in the Streamlit app
    
    if relQry:
        relQ = relQueries(relQry)

        st.title(f"Related Queries for {relQry}")  # add a title
        st.write(relQ)  # visualize my dataframe in the Streamlit app
    
main()




