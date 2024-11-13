

# File: main.py
from dataPackage.bdsAPI import BEAApi

if __name__ == "__main__":

    # Instantiate the BEAApi class
    api = BEAApi()

    # Get the data from the API
    data = api.get_request_url()

    # Print the value for 'Computers and Peripheral Equipment' fixed assets in 2023
    api.print_computers_peripheral_equipment_2023(data)
    
    #save the JSON file to a CSV file
    api.save_json_to_csv(data)
