from abc import ABC, abstractmethod
import pandas as pd
import json
import xmltodict

class JsonParser(ABC):
    """Abstract JsonParser Class"""

    @abstractmethod
    def parse_to_json(self, path_input, path_output):
        pass

class CSVParser(JsonParser):
    """CSVParser that inherts from JsonParser"""

    # overriding abstract method
    def parse_to_json(self, path_input, path_output):
        df = pd.read_csv(path_input, index_col = 0)
        df.to_json(path_output)

class XMLParser(JsonParser):
    """CSVParser that inherts from JsonParser"""

    # overriding abstract method
    def parse_to_json(self, path_input, path_output):
        """Parse XML to json file"""
        with open(path_input) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            xml_file.close()
            json_data = json.dumps(data_dict)
            with open(path_output, "w") as json_file:
                json_file.write(json_data)
                json_file.close()

class CSVParser(JsonParser):
    """CSVParser that inherts from JsonParser"""

    # overriding abstract method
    def parse_to_json(self, path_input, path_output):
        df = pd.read_csv(path_input, index_col = 0)
        df.to_json(path_output)

class XLSXParser(JsonParser):
    """CSVParser that inherts from JsonParser"""

    # overriding abstract method
    def parse_to_json(self, path_input, path_output):
        df = pd.read_excel(path_input)
        df.to_json(path_output)
