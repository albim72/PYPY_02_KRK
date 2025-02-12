import requests

def get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("GET Response:", response.json())
    else:
        print(f"GET Error: {response.status_code}")

def post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Mój post",
        "body": "Treść posta",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print("POST Response:", response.json())
    else:
        print(f"POST Error: {response.status_code}")

def download_file():
    url = "https://via.placeholder.com/150"
    response = requests.get(url)
    if response.status_code == 200:
        with open("obrazek.png", "wb") as file:
            file.write(response.content)
        print("Obraz zapisany jako 'obrazek.png'")
    else:
        print(f"Download Error: {response.status_code}")

if __name__ == "__main__":
    get_request()
    post_request()
    download_file()
