"""
Project 3 emphasizes skills in using Git for version control, 
creating and managing Python virtual environments, and handling different types of data. 
The project involves fetching data from the web, 
processing it using appropriate Python collections, 
and writing the processed data to files.
"""

# Standard library imports
import csv
from pathlib import Path 

# External library imports (requires virtual environment)
import requests
import json

# Local module imports
import jaya_projsetup      
import JayaTries_utils as utils

#Function - Process Text Data
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

#Function - Process CSV Data
def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w', newline='', encoding='utf-8') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

#Function - Process Excel Data
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

#Function - Process JSON Data
def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name, filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON data saved to {file_path}")

#Function - Fetch and write excel file
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

#Function - Fetch and write txt data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text) #call function saves content
    else:
        print(f"Failed to fetch data: {response.status_code}")

#Function - Fetch and save csv data
def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.content.decode('utf-8'))
    except requests.RequestException as e:
        print(f"Error fetching CSV data: {e}")

#Function - Fetch and save JSON data
def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.RequestException as e:
        print(f"Error fetching JSON data: {e}")

#Function - main
def main():
    '''
    Main function
    Fetching data from web sources and processing them for statistical analysis.
    Writes the statistical analysis to a txt file.
    '''
    print(f"Name:  {utils.company_name}")
    
    # URLs with differnt data types
    url_text = "https://storage.googleapis.com/kagglesdsdata/datasets/463494/941394/Shakespeare_01.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240124%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240124T015418Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5d0da122a3e4c7a356b8d4940847e96cc92e695cbd330044d29cc7a752d7810001753662bacdf25b21bfe4d0d3ff633a4b8f3f1ef23bd68afbdbecaa210e4b5f6c6a4614b940fcdc0beded8079a2829c3c38d860b46080222d9262db2f0f1954678287bcbafdf881e757ac9c106c1f271e63859ee5a790d3efa4a678933f11905932e44d61107699118e2bec17cdc8126c8437d422e7239000b9a32c66ee2ad253122c4be55e0ad73265a4fc55b6a3d453ab4bf1e2b82a55b1379bf33818a2cea0acf439669257e3058c7193047714e74a196efeb2eff7fddbed73a14dd22ba99f029f0dca5f55db2796fec7b6e67f33786af37d1781769f75946bc9f791323e"
    url_excel = "https://github.com/mikeygman11/Baseball-Statistics/raw/master/2019mlb.xlsx"
    url_csv = "https://query.data.world/s/352fjx2iiw5427wzmelxeky6fql6uh?dws=00000"
    url_json = "https://storage.googleapis.com/kagglesdsdata/datasets/496274/945103/StadiumsFull.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240124%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240124T021508Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71e775d54b626f4f795aeebb70198e1dad862cb099ea8401a2c8657c507a3040d847a2288ba19b9d37adc9183e978c993c7cf4f7c355ca633c08dcd0d8fa655dc37b8b82a3cf06c23aee21e0452af773f2b2d0fcf19465f682b63d3bb664c88a9ef121685bf163b8291150848dace19a7aa2ecc2507e401d18e81c316a7c7acd61a7ceecbfd3162058bdf3f6065bfc6154e59e7059e38da497d0e638398a34544eff4b32f3255cea82868fa9b3f5fe394abe6ba914489329451dafc667db827161905aa497fc971544cb2b4bf283c9c6e86c7c05bbdb02d00a4be86c127da101aad3a01c1ae6772a1d2518774a284b2b1da3dc3c8398770d749b3a000a348ba0"
    
    # folder names to write data to
    txt_folder_name = "data-txt"
    excel_folder_name = "data-excel"
    csv_folder_name = "data-csv"
    json_folder_name = "data-json"
    
    # file names to write data to
    txt_filename = 'data.txt'
    excel_filename = 'data.xls'
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    
    # fetch data and write to files
    fetch_and_write_txt_data(txt_folder_name, txt_filename, url_text)
    fetch_and_write_excel_data(excel_folder_name, excel_filename, url_excel)
    fetch_and_write_csv_data(csv_folder_name, csv_filename, url_csv)
    fetch_and_write_json_data(json_folder_name, json_filename, url_json)
    
# conditional execution
if __name__ == "__main__":
    main()