import streamlit as st
import logging
import requests
import pytrends
import pandas as pd
import lxml
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os
import re

code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G8LLP1NRE9"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-G8LLP1NRE9');
</script>"""

a=os.path.dirname(st.__file__) + '/static/index.html'
with open(a, 'r') as f:
    data=f.read()
    if len(re.findall('G-', data)) == 0:
        with open(a, 'w') as f:
            newdata=re.sub('<head>','<head>' + code, data)
            f.write(newdata)

st.title("Hello worl   d ! It's Arthur ALLIOUX")
input = st.text_input('Variable', 'exemple')
logging.warning('La variable est ' + input)
st.write('The value is', input)
pytrends = TrendReq(hl='en-US', tz=360)
input1 = st.text_input('Recherche 1 ')
input2 = st.text_input('Recherche 2 ')
input3 = st.text_input('Recherche 3 ')
if st.button('Search trend'):
  keywords = [input1, input2, input3]
  pytrends.build_payload(keywords, timeframe = 'today 3-m')
  data = pytrends.interest_over_time()
  st.line_chart(data)

if st.button('Make a Google Analytics request'):
  req = requests.get("https://www.google.com/")
  req2 = requests.get('https://analytics.google.com/analytics/web/#/p273040931/reports/defaulthome?params=_u..nav%3Ddefault&key=AIzaSyCFZp_DJbQUHGrvvnktRejZ5REge7Rli9c')
  st.text(req2.status_code)
  st.markdown(req2.text)
  st.write('\n Request Done  ' + str(req))
  st.markdown(req.cookies._cookies)
else:
  st.write('Request not Done')