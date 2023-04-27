import yaml

# Reading dynamic yaml file and store here
import os

dir = os.getcwd()

class read_yml:
    def read_file(f):
        with open(f,'r') as file:
            data = yaml.safe_load(file)
        return data
        # print(data['Db_conn']['Password'])
