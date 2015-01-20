'''
A simple client for USDA statistics
    http://quickstats.nass.usda.gov/api

Found the data set in the data.gov catalog:
    http://catalog.data.gov/dataset/quick-stats-agricultural-database-api

Fun fact: This actually queries a database with 31 million records
'''

import requests


# You'll need to change this to the key from the email
#usda_key = ''

# Save the url
base = 'http://quickstats.nass.usda.gov/api/get_param_values/?key='

# If you save this publicly to Github then it's better to keep your key in
# a separate private plain text file called 'usda_key.txt'
try:
    with open('usda_api_key.txt') as f:
        usda_key = f.read().rstrip()
except FileNotFoundError:
    pass


def get_param_values(param, key = usda_key):
    url = 'http://quickstats.nass.usda.gov/api/get_param_values/?key='

    url_with_key = url + key + '&param=' + param

    response = requests.get(url_with_key)
    return response  
pass




def query(parameters, key=usda_key):
    url = 'http://quickstats.nass.usda.gov/api/api_GET/?key='
    query_str = '&'.join("{!s}={!s}".format(key,val) for (key,val) in parameters.items())
    url_with_key = url + key + '&' + query_str 
    response = requests.get(url_with_key)
    return response
pass



if __name__ == '__main__':
    # A few examples of usage

    # Possible values for 'commodity_desc'
    commodity_desc = get_param_values('commodity_desc')
    # Expect:
    # ['AG LAND', 'AG SERVICES', 'AG SERVICES & RENT',
    # 'ALMONDS', ...

    # Value of rice crops in Yolo (Davis) county since 2005
    riceparams = {'sector_desc': 'CROPS',
                  'commodity_desc': 'RICE',
                  'state_name': 'CALIFORNIA',
                  'county_name': 'YOLO',
                  'year__GE': '2005',
                  'unit_desc': '$',
                  }

    yolorice = query(riceparams)

    # Try using a dictionary comprehension to filter
    yearvalue = {x['year']: x['Value'] for x in yolorice}
    # Expect:
    # {'2007': '26,697,000', '2012': '51,148,000'}
