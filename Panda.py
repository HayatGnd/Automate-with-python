import pandas as pd
#recuperer les tableau dans un site web :
simpsons=pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")
sum=len(simpsons)
print(sum)
print(simpsons[0])
#telecharger des fichier automatiquement selct all:

 