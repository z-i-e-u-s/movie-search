#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from omdbapi.movie_search import GetMovie
import pandas as pd
from tabulate import tabulate as td
#"Library Imported"




search=input("Enter the movie you want to search for :")





movie=GetMovie(title=search,api_key='723686e0',plot='full')




result=movie.get_data('Title','Year','Genre','Director','Actors','Rated','imdbRating','imdbVotes')
result_data=pd.DataFrame.from_dict(result,orient='index')
"Your Returned Result : "







print(td(result_data,tablefmt="rst"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




