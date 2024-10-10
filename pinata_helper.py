import os
import requests
from dotenv import load_dotenv

load_dotenv()

PINATA_API_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"
PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")
print(PINATA_API_KEY,PINATA_SECRET_API_KEY)

def upload_pdf_to_pinata(file_path):
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }
    with open(file_path, 'rb') as file:
        response = requests.post(PINATA_API_URL, files={'file': file}, headers=headers)
        if response.status_code == 200:
            print("File uploaded successfully")
            return response.json()['IpfsHash']
        else:
            print(f"Error: {response.text}")
            return None
