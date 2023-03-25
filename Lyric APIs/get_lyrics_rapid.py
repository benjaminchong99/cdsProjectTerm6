import requests

url = "https://theaudiodb.p.rapidapi.com/searchtrack.php"

querystring = {"s":"coldplay","t":"yellow"}

headers = {
	"X-RapidAPI-Key": "46e4fd53a4msh177fa2057a192d5p12feafjsn464b3cf84522",
	"X-RapidAPI-Host": "theaudiodb.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)