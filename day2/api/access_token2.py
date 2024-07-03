import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=crIgZdonnwjF0gReGweLspKR&client_secret=G6RVAUrfT34YHRpwnLANls5yISCpU0r5"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()