import requests

def main():
    res = requests.get("http://api.open-notify.org/iss-now.json")
    if res.status_code != 200:
        raise Exception("Error APi request not successful")
    data = res.json()
    longitude = data["iss_position"]["longitude"]
    print(f"Longitude is {longitude}")
    
    for key, value in data.items():
        print("Key:")
        print(key)


if __name__=="__main__":
    main()