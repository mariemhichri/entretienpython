import pandas
import json

excel_data_df = pandas.read_excel('test.xlsx')

json_str = excel_data_df.to_json(orient='records')

json_array = json.loads(json_str)


def exportJSON():
    list = []
    i=0
    j=0
    for item in json_array:
        if i>2 and i<32 and  item['Unnamed: 1'] :
            if item["N°"] == None :
                details = {
                    "order": j,
                    "type": "CELL",
                    "description": item['Unnamed: 1'],
                    "unity": item['Unnamed: 2'],
                    "quantity": item['Unnamed: 3']
                }
                list.append(details)
            else :
                x = item["N°"].split(".")
                level = len(x)-1
                title = {
                    "order": j,
                    "type": "SECTION",
                    "reference": item["N°"],
                    "level": level,
                    "description": item['Unnamed: 1']
                }
                list.append(title)
            j=j+1
        i=i+1
    data = {"items":list}
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

exportJSON()

