import requests
import json

def fetch_subdomain_data(domain):
    url = f"https://api.subdomain.center/?domain={domain}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    domain = "acehprov.go.id"
    result = fetch_subdomain_data(domain)
    
    if result:
        print(json.dumps(result, indent=2))
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
