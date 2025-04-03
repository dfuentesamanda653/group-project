import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully:", data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")

fetch_data("https://api.example.com/data")
