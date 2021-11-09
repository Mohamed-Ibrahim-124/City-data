import pandas as pd
import json
import csv
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with open("countries.csv", 'r') as j:
        countries = json.loads(j.read())
        result = []
        longest_city_name = ''
        number_of_countries = 0
        for key in countries:
            longest_city_name = max(max(countries[key]),(longest_city_name))
            number_of_countries +=len(countries[key])
            result.append([key , len(countries[key]) , max(countries[key])])
        print("longest City Name =",longest_city_name,"Number of Cities=",number_of_countries)
        header = ["Country Name","Number of cities","City with max length"]
        with open('result.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            # write the data
            writer.writerow(result)
