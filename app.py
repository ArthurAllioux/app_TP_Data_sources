import streamlit as st
import logging
import requests

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
if st.button('Make a Google Analytics request'):
  req = requests.get("https://www.google.com/")
  req2 = requests.get('https://analytics.google.com/analytics/web/#/p273040931/reports/defaulthome?params=_u..nav%3Ddefault')
  st.text(req2.status_code)
  st.markdown(req2.text)
  st.write('\n Request Done  ' + str(req))
  st.markdown(req.cookies._cookies)
else:
  st.write('Request not Done')
