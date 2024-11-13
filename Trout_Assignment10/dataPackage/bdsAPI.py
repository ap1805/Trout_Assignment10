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


