# Name: Aryan Patel, Jacob Shulte
# email: patel7aj@mail.uc.edu, schul2jt@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010/001
# Semester/Year: Fall/2024
# Brief Description of the assignment: submit a request to an API and store the results in a dictionary. Access some data from the 
#                                      dictionary to print to the console. Also store the results of the api in a csv file.
# Creates a class to send an api request and has a method to get the data of the api and put it into a dictionary, 
#                                               extract and print some interesting data to the console, and a method to save the endpoint data to a csv file.
# Citations: Bill, https://www.geeksforgeeks.org/convert-json-to-csv-in-python/, https://www.geeksforgeeks.org/python-api-tutorial-getting-started-with-apis/,
#            https://www.geeksforgeeks.org/python-dictionary/, https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
# Anything else that's relevant:

import requests
import csv
import json

class BEAApi:  # This API is data of "Current-Cost Net Stock of Private Fixed Assets, Equipment, Structures, and Intellectual Property Products by Type, for all years"
    def __init__(self, base_url="https://apps.bea.gov/api/data/?UserID=C66A4686-7616-452D-A62E-32BEE7520CA2&method=GetData&datasetname=FixedAssets&TableName=FAAt201&Year=ALL&ResultFormat=json"):
        self.base_url = base_url

    def get_request_url(self):
        '''
        @param self: the current object
        @return: dictionary with the api endpoint data
        '''
        response = requests.get(self.base_url)
        json_string = response.content
        parsed_json = json.loads(json_string)
        return parsed_json


    # Since the endpoint is information related to fixed assets by the type of asset, I thought it would be cool to see the most recent value of computer equipment, so i used that type and got the
    # value for computers and peripheral equipment in 2023
    def print_computers_peripheral_equipment_2023(self, data):
        '''
        @param self: the current object, data: the api request
        '''
        if 'BEAAPI' in data and 'Results' in data['BEAAPI'] and 'Data' in data['BEAAPI']['Results']:
            data_entries = data['BEAAPI']['Results']['Data']
            for entry in data_entries:
                if entry.get("LineDescription") == "Computers and peripheral equipment" and entry.get("TimePeriod") == "2023":
                    value = entry.get("DataValue", "N/A")
                    print(f"Value for 'Computers and Peripheral Equipment' fixed assets in 2023 (millions of $): {value}")
                   

    def save_json_to_csv(self, data, filename='dataPackage/full_result.csv'):
        '''
        @param self: the current object, data: the api request, filename: the path for the csv to save to
        '''
        if 'BEAAPI' in data and 'Results' in data['BEAAPI'] and 'Data' in data['BEAAPI']['Results']:
            data_entries = data['BEAAPI']['Results']['Data']
            if not data_entries:
                print("No data available to save.")               
            try:
                keys = data_entries[0].keys() if data_entries else []
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data_entries)
                print(f"Full JSON data saved to {filename}")
            except:
                print("Error saving file")
        else:
            print("No interesting data found in the response.")






