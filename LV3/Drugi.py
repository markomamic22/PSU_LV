import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('LV3')
mtcars = pd.read_csv('mtcars.csv')
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
mpg_4 = sum(mtcars.mpg[mtcars.cyl==4])
mpg_4 = mpg_4/ len(mtcars[mtcars.cyl==4])
mpg_6 = sum(mtcars.mpg[mtcars.cyl==6])
mpg_6 = mpg_6 / len(mtcars[mtcars.cyl==6])
mpg_8 = sum(mtcars.mpg[mtcars.cyl==8])
mpg_8 = mpg_4 / len(mtcars[mtcars.cyl==8])
values = [mpg_4,mpg_6,mpg_8]
ax.set_xlabel('Cilindri')
ax.set_ylabel('Srednja potrošnja')

ax.bar(['4','6','8'],values)
for i in ax.patches:
    ax.annotate(format(i.get_height(), '.2f') + ' mpg', 
                   (i.get_x() + i.get_width() / 2, 
                    i.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 5),
                   textcoords='offset points')
plt.show()

boxplot = mtcars.boxplot(by='cyl',column=['wt'])
plt.show()


automatic = mtcars[mtcars.am == 0]
manual = mtcars[mtcars.am == 1]
a = automatic.mpg.to_numpy()
m = manual.mpg.to_numpy()



fig2 = plt.figure()
ax2 = fig2.add_axes([0.1,0.1,0.8,0.8])
axa = ax2.plot(a, 'bs:')
axm = ax2.plot(m, 'ro-')
ax2.legend(labels = ['Automatski','Ručni'],loc='upper left')
ax2.set_title("Potrošnja s obzirom na vrstu mijenjača (mpg)")

plt.show()

automatic = mtcars[mtcars.am == 0]
manual = mtcars[mtcars.am == 1]
a_hp = automatic[['hp','qsec']].to_numpy()
m_hp= manual[['hp','qsec']].to_numpy()
print(a_hp)



fig3 = plt.figure()
ax3 = fig3.add_axes([0.1,0.1,0.8,0.8])
axa_hp = ax3.scatter(a_hp[:,1],a_hp[:,0])
axm_hp = ax3.scatter(m_hp[:,1],m_hp[:,0])
ax3.legend(labels = ['Automatski','Ručni'],loc='upper right')
ax3.set_title("Ubrzanje s obzirom na konjsku snagu")

plt.show()