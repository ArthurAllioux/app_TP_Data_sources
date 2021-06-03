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
import functools
import time
import collections

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        logging.warning(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


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

@timer
def read_with_counter():
  words = re.findall(r'\w+', open('t8.shakespeare.txt').read().lower())
  return words

@timer
def read_with_counter_100times():
  tps_counter = {}
  for i in range(10):
    start_time = time.perf_counter() 
    words = read_with_counter()  
    end_time = time.perf_counter()   
    run_time = end_time - start_time 
    tps_counter[i]= run_time
  return (words,tps_counter)

if st.button('Read shakespeare with counter'):
  words,tps_counter = read_with_counter_100times()
  st.write(collections.Counter(words).most_common(10))

@timer
def read_with_dico():
  book = open('t8.shakespeare.txt', "r")
  d = dict()
  for line in book:
      line = line.strip()
      line = line.lower()
      words = line.split(" ")
      for word in words:
          if word in d:
              d[word] = d[word] + 1
          else:
              d[word] = 1
  return d

@timer
def read_with_dico_100times():
  for i in range(100):
    start_time = time.perf_counter() 
    dico = read_with_dico()
    end_time = time.perf_counter()   
    run_time = end_time - start_time 
    tps_counter[i]= run_time
  return dico

if st.button('Read shakespeare with dico'):
  dico = read_with_dico_100times()
  st.write(collections.Counter(dico).most_common(10))
  