import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


os.chdir("LV3")
mtcars = pd.read_csv('mtcars.csv')

print("Ispis prvih 5 s najvećom portošnjom\n")
print(mtcars.sort_values(by='mpg',ascending=True).head(5),'\n')
print("Ispis 3 s najmanjom potrošnjom od 8 cilindara\n")
print(mtcars.loc[mtcars['cyl']==8].sort_values(by='mpg',ascending=False).head(3),'\n')
six_average = mtcars.loc[mtcars['cyl']==6]
print("Srednja potrošnja za 6 cilindara je: ",six_average['mpg'].mean(),"\n")
four_cylinder = mtcars[(mtcars['cyl']==4)&(mtcars['wt']>=2.00)&(mtcars['wt']<=2.20)]
print("Srednja potrošnja za 4 cilindra između 2000 i 2200 lbs je: ",four_cylinder['mpg'].mean(),"\n")
automatic = mtcars[mtcars['am']==0]
manual = mtcars[mtcars['am']==1]
print("Auti s automatskim mijenjačem: ", len(automatic),"\nAuti s ručnim mijenjačem: ", len(manual),"\n")
print("Auti s automatskim mijenjačem i konjskom snagom preko 100:\n",automatic[automatic['hp']>100])
print(mtcars['wt']*1000*0.4549) 

print(mtcars.wt)
new_wt = mtcars.wt * 1000
mtcars.wt = new_wt
print(mtcars.wt)