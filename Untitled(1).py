#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from omdbapi.movie_search import GetMovie
import pandas as pd
from tabulate import tabulate as td
"Library Imported"


# In[ ]:


search=input("Enter the movie you want to search for :")


# In[ ]:


movie=GetMovie(title=search,api_key='723686e0',plot='full')


# In[ ]:


result=movie.get_data('Title','Year','Genre','Director','Actors','Rated','imdbRating','imdbVotes')
result_data=pd.DataFrame.from_dict(result,orient='index')
"Your Returned Result : "




# In[ ]:


print(td(result_data,tablefmt="rst"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




