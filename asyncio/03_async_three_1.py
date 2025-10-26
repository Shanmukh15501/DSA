import requests
import time
def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} with status {response.status_code}")

def main():
    start = time.time()
    
    urls = ["https://httpbin.org/delay/2"] * 3
    for url in urls:
        fetch_url(url)
    end =  time.time() - start
    
    print("enddddddddddd",end)

main()
