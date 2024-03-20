import requests

API_KEY = "b5f3c3575b4d350213badab79f50c2e2"

def get_data(place,days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url) # gets the content
    data = response.json() # turns the content into json
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",days=3,kind="Temperature"))