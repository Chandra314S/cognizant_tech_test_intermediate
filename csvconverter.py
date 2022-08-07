import csv, json

output = []
class LevelNode():
    def __init__(self, l_name,l_id,l_url):
        self.l_name = l_name
        self.l_id = l_id
        self.l_url = l_url
        self.child =[]

class BaseNode():
    def __init__(self, base_url):
        self.base_url = base_url
        self.child =[]

class JsonDataParser():
    def __init__(self):
        self.headers = []
        self.totalNodes = []
        pass

    def getBaseNode(self, baseUrl):
        resultNode = None
        if baseUrl == "":
            return None
        for baseNode in self.totalNodes:
            if baseNode.base_url == baseUrl:
                resultNode = baseNode
                break
        if resultNode is None:
            resultNode = BaseNode(baseUrl)
            self.totalNodes.append(resultNode)
        return resultNode

    def loadChildLevel(self, childNode, ind):
        result = []
        for childrenNode in childNode:
            child_output = {
                self.headers[int(ind)] : childrenNode.l_name,
                self.headers[int(ind+1)] : childrenNode.l_id,
                self.headers[int(ind+2)] : childrenNode.l_url,
                "children": self.loadChildLevel(childrenNode.child, ind+3)
            }
            result.append(child_output)
        return result

    def DataParser(self, datafilepth='Data/data1.csv', parsedfilepth='Results/parsed_json.json'):
        with open(datafilepth) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                if len(self.headers) == 0 :
                    self.headers = row
                    continue
                baseNode = self.getBaseNode(row[0])
                if baseNode is None or row[1] == "":
                    continue
                currentNode = None
                for baseParent in baseNode.child:
                    if baseParent.l_id == row[2]:
                        currentNode = baseParent
                        break
                if currentNode is None:
                    currentNode = LevelNode(row[1], row[2], row[3])
                    baseNode.child.append(currentNode)
                for x in range(0, len(row) - 4, 3):
                    childNode = None
                    if row[4+x+1] == "":
                        continue
                    for child in currentNode.child:
                        if child.l_id == row[4+x+1]:
                            childNode = child
                            break
                    if childNode is None:
                        # childNode = LevelNode(row[4+x], row[4+x+1], row[4+x+2],row[4+x+3])
                        childNode = LevelNode(row[4+x], row[4+x+1], row[4+x+2])
                        currentNode.child.append(childNode)
                    currentNode = childNode
        #import pdb;pdb.set_trace()
        result = []
        for resultNode in self.totalNodes:
            baseResult = {
                self.headers[0]: resultNode.base_url,
                "levels": self.loadChildLevel(resultNode.child, 1)
            }
            result.append(baseResult)

        json.dump(parsedfilepth,
                  open(parsedfilepth, 'w'),
                  indent=4,
                  sort_keys=False)
        # with open(parsedfilepth,'w') as jsonfile:
        #     json_data = json.dumps(result)
        #     jsonfile.write(json_data)
        jsonstr = json.dumps(result)
        print(f'CSV data parsed to json file and stored in {parsedfilepth}')
        return jsonstr