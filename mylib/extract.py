import requests

def extract(url="""https://raw.githubusercontent.com/fivethirtyeight
            /data/refs/heads/master/candy-power-ranking/candy-data.csv""", 
            file_path="data/candy-data.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



