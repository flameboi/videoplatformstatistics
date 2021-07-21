import numpy as np
import math
views=input("Enter views: ")
ls=float(input("Enter Likes: "))
ds=float(input("Enter dislikes "))
vote = (float(ls) + float(ds))
per = float
per = 100*float(vote)/float(views)
print(str(vote) + " viewrs voted, which are " + str(per) + "% from all viewers" )
