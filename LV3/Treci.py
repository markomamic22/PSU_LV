import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

os.chdir('LV3')
# url koji sadrzi xml datoteku s mjerenjima:
url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=5&vrijemeOd=01.01.2017&vrijemeDo=01.01.2018'

resp = ur.urlopen(url).read()

root = ET.fromstring(resp)



df = pd.DataFrame(columns=('vrijednost', 'vrijeme'))

i = 0
while True:
    
    try:
        obj = root.getchildren()[i].getchildren()
    except:
        break
    
    row = dict(zip(['vrijednost', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
    df.vrijednost[i] = float(df.vrijednost[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)
df.plot(y='vrijednost', x='vrijeme')
plt.show()

# add date month and day designator
df['month'] = df['vrijeme'].dt.month
df['dayOfweek'] = df['vrijeme'].dt.dayofweek
