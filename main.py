
import pandas as pd
from datetime import datetime
movie=pd.read_csv('movies.csv')

movie['YEAR']=movie['YEAR'].str.replace("[()]","",regex=True).str.replace("I","").str.replace("II","").str.replace("V","").str.strip()
movie['YEAR']=movie['YEAR'].str[0:4]
movie['VOTES']=movie['VOTES'].str.replace(",","").fillna(0).astype(int)
movie['Gross'].dropna()
movie['RunTime']=movie['RunTime'].fillna(0).astype(int)
movie['RATING']=movie['RATING'].fillna(0)
movie['GENRE']=movie['GENRE'].fillna("")
movie.info()

import matplotlib.pyplot as plt
#plt.bar(movie['MOVIES'],movie['RATING'],color='red')
#plt.show()

voted = movie.sort_values(by='VOTES',ascending=False).reset_index()
voted=voted.head(10)
plt.bar(voted['MOVIES'],voted['VOTES'],color='red')
plt.xticks(fontsize=4)
plt.show()


long = movie.sort_values(by=movie['RunTime'],ascending=False).reset_index()
long=long.head(10)
plt.bar(long['MOVIES'],long['RunTime'],color='red')
plt.xticks(fontsize=4)
plt.show()


# the item slicing not working because of string available
# cant remove hypen why dont knpw