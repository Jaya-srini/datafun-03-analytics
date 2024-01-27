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
import io
import pandas as pd

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
    with file_path.open('wb') as file:
        file.write(data)
        print(f"Binary data saved to {file_path}")

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
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch json data:{response.status_code}")

# Function - Process text data  
def process_txt_file(folder_name, input_filename, output_filename):
    # Fetch the data
    txt_url = 'https://txt2html.sourceforge.net/sample.txt'
    response = requests.get(txt_url)
    
    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, input_filename, data)
        processed_data = data  
        write_txt_file(folder_name, output_filename, processed_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function - Process CSV data
def process_csv_file(csv_folder_name, input_filename, output_filename):
    # Fetch the data
    csv_url = 'https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/customers/customers-100.csv'
    response = requests.get(csv_url)
    
    if response.status_code == 200:
        data = response.text
        write_csv_file(csv_folder_name, input_filename, data)
        processed_data = data 
        write_csv_file(csv_folder_name, output_filename, processed_data)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function - Process Excel data
def process_excel_file(excel_folder_name, input_filename, output_filename):
    # Fetch the data
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    response = requests.get(excel_url)
    
    if response.status_code == 200:
        data = response.content
        write_excel_file(excel_folder_name, input_filename, data)

        # Use pandas to read Excel data directly from binary data
        excel_data = pd.read_excel(io.BytesIO(data), sheet_name='Sheet1')  # Update 'Sheet1' to the actual sheet name

        # Convert the read Excel data to CSV format
        processed_data = excel_data.to_csv(index=False)
        
        # Write the processed data to a CSV file
        csv_output_filename = output_filename.replace('.xls', '.csv')
        write_csv_file(excel_folder_name, csv_output_filename, processed_data)
        
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function - Process JSON data
def process_json_file(json_folder_name, input_filename, output_filename):
    # Fetch the data
    json_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'
    response = requests.get(json_url)
    
    if response.status_code == 200:
        data = response.content
        write_json_file(json_folder_name, input_filename, data)
        write_json_file(json_folder_name, output_filename, data)
       
    else:
        print(f"Failed to fetch data: {response.status_code}")

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
    url_json = "https://dog.ceo/api/breeds/image/random"
    
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

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')
    
# conditional execution
if __name__ == "__main__":
    main()