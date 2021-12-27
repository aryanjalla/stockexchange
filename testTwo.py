import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

querystring = {"symbol":"BURKIN","region":"IN"}

headers = {
    'x-rapidapi-key': "fd279a33acmsh89a6368dff33c87p1b1780jsnc664c297a9e4",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)