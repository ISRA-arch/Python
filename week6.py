import os
import requests
from urllib.parse import urlparse
import uuid

def download_image():
    print("!")
    image_url = input().strip()

    
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)


        
        print(" Fetching image...")
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  

        parsed = urlparse()
        filename = os.path.basename(parsed.path)

        
        if not filename or "." not in filename:
            filename = f"ubuntu_image_{uuid.uuid4().hex[:8]}.jpg"

        file_path = os.path.join(folder_name, filename)

        

if __name__ == "__main__":
    download_image()
