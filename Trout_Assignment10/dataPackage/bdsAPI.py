# Document here
import requests
import csv
import json

class BEAApi:          # Current-Cost Net Stock of Private Fixed Assets, Equipment, Structures, and Intellectual Property Products by Type, for all years
    def __init__(self, base_url="https://apps.bea.gov/api/data/?UserID=C66A4686-7616-452D-A62E-32BEE7520CA2&method=GetData&datasetname=FixedAssets&TableName=FAAt201&Year=ALL&ResultFormat=json"):
        self.base_url = base_url

    def get_request_url(self):
        response = requests.get(self.base_url)
        json_string = response.content
        parsed_json = json.loads(json_string)
        return parsed_json

    def print_computers_peripheral_equipment_2023(self, data):
        if 'BEAAPI' in data and 'Results' in data['BEAAPI'] and 'Data' in data['BEAAPI']['Results']:
            data_entries = data['BEAAPI']['Results']['Data']
            for entry in data_entries:
                if entry.get("LineDescription") == "Computers and peripheral equipment" and entry.get("TimePeriod") == "2023":
                    value = entry.get("DataValue", "N/A")
                    print(f"Value for 'Computers and Peripheral Equipment' fixed assets in 2023 (millions of $): {value}")
                    return

    def save_json_to_csv(self, data, filename='data/full_result.csv'):
        # Assuming 'Data' key contains relevant information
        if 'BEAAPI' in data and 'Results' in data['BEAAPI'] and 'Data' in data['BEAAPI']['Results']:
            data_entries = data['BEAAPI']['Results']['Data']
            if not data_entries:
                print("No data available to save.")
                return

            # Attempt to open the file directly without creating directories
            try:
                keys = data_entries[0].keys() if data_entries else []
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data_entries)
                print(f"Full JSON data saved to {filename}")
            except FileNotFoundError:
                print(f"Error: The directory for the file '{filename}' does not exist. Please create the directory manually.")
        else:
            print("No interesting data found in the response.")






