from pprint import pprint
import json
import csv

def Dataparser(srcfile,destinationfile):
    data={}
    with open (srcfile) as file:
        var=csv.DictReader(file)
        for row in var:
            if row["Base URL"] != "":
                if 'Base URL' not in data:
                    data['Base URL'] = row['Base URL']
                    data["Level 1 - Name"]=row["Level 1 - Name"]
                    data["Level 1 - ID"]=row["Level 1 - ID"]
                    data["Level 1 - URL"]=row["Level 1 - URL"]
                    data["children"]=[]
                    if row["Level 2 - Name"] !='':
                        data["children"].append({"Level 2 - Name":row["Level 2 - Name"],"Level 2 - ID":row["Level 2 - ID"],"Level 2 URL":row["Level 2 URL"],"children":[]})
                        if row["Level 3 - Name"] != '':
                            data["children"][-1]["children"] = [{"Level 3 - Name":row["Level 3 - Name"],"Level 3 - ID":row["Level 3 - ID"],"Level 3 URL":row["Level 3 URL"],"children":[]}]
                        else:
                            data["children"][-1]["children"] = []
                    else:
                        data["children"] = []
                else:
                    if data["Level 1 - Name"] == row["Level 1 - Name"]:
                        if data["children"] and data["children"][-1]["Level 2 - Name"] == row["Level 2 - Name"]:
                            if row["Level 3 - Name"] != '':
                                data["children"][-1]["children"].append({"Level 3 - Name":row["Level 3 - Name"],"Level 3 - ID":row["Level 3 - ID"],"Level 3 URL":row["Level 3 URL"],"children":[]})
                            else:
                                pass
                        else:
                            data["children"].append({"Level 2 - Name":row["Level 2 - Name"],"Level 2 - ID":row["Level 2 - ID"],"Level 2 URL":row["Level 2 URL"],"children":[]})
                            if row["Level 3 - Name"] != '':
                                data["children"][-1]["children"] = [{"Level 3 - Name":row["Level 3 - Name"],"Level 3 - ID":row["Level 3 - ID"],"Level 3 URL":row["Level 3 URL"],"children":[]}]
                            else:
                                pass
        with open(destinationfile,'w') as jsonfile:
            json_data = json.dumps(data)
            jsonfile.write(json_data)
        print(f'CSV data parsed to json file and stored in {destinationfile}')
        return data