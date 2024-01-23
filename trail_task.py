import requests

# Making a GET requests to the API  to fetch the data
response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Saving the infromation to a list with json or dictionaries (Python)
data = response.json()

# Extract the titles from the data
# Check if this title have the string 'qui' in the value
titles = [dic['title'] for dic in data 
          if isinstance(dic, dict) and 'title' in dic and isinstance(dic['title'], str) and  'qui' in dic['title']]


# Printing esach title using f-strings
for title  in titles:
    print(f'Title: {title}')

# Checking if any title is of type (int)
is_int_title = any(isinstance(title, int) for title in titles)

# Printing the result of the type check
if is_int_title:
    print('At least one of the titles is of type int')
else:
    print('None of the titles is of type int')