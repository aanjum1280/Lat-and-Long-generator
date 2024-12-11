import requests

def get_lat_long(address, api_key):
    # Base URL for Google Maps Geocoding API
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Parameters to send with the request
    params = {
        "address": address,
        "key": api_key
    }

    # Making a GET request to the API
    response = requests.get(url, params=params)
    data = response.json()

    # Check if the API request was successful
    if data["status"] == "OK":
        # Extract latitude and longitude from the response
        location = data["results"][0]["geometry"]["location"]
        latitude = location["lat"]
        longitude = location["lng"]
        return latitude, longitude
    else:
        # Handle errors
        raise Exception(f"Error from Geocoding API: {data['status']}")

# Example Usage
if __name__ == "__main__":
    # Replace with your API key
    API_KEY = "YOUR_API_KEY"
    address = "house 12, kapasheda border, new delhi, 110037"
    
    try:
        lat, long = get_lat_long(address, API_KEY)
        print(f"Address: {address}")
        print(f"Latitude: {lat:.6f}, Longitude: {long:.6f}")
    except Exception as e:
        print(e)
