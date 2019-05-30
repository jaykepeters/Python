try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "atomizer"
  
for j in search(query, tld="com", stop=1000): 
    domain=j.split("//")[-1].split("/")[0]
    print(domain)

