# Name: Aryan Patel, Jacob Shulte
# email: patel7aj@mail.uc.edu, schul2jt@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010/001
# Semester/Year: Fall/2024
# Brief Description of the assignment: submit a request to an API and store the results in a dictionary. Access some data from the 
#                                      dictionary to print to the console. Also store the results of the api in a csv file.
# Brief Description of what this module does: instantiates the class of the api request url and calls the method to get the data. then calls 
#                                              the method to print the message to the console and the method to save the csv file
# Citations:
# Anything else that's relevant: 

from dataPackage.bdsAPI import BEAApi

if __name__ == "__main__":

    # Instantiate the BEAApi class
    api = BEAApi()

    # Get the data from the API
    data = api.get_request_url()

    # Print the value for 'Computers and Peripheral Equipment' fixed assets in 2023
    api.print_computers_peripheral_equipment_2023(data)
    
    #save the endpoint by converting the json data to a CSV file
    api.save_json_to_csv(data)
