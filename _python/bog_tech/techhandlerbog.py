import os
import json
import re
from pathlib import Path

dirPath = Path(__file__).parents[2]
jsonPath = dirPath / '_python' / 'bog_tech'
techPath = dirPath / 'land overhaul bog' / 'common' / 'technologies'

techNames = [
    'infantry',
    'motorized',
    'mechanized',
    'cavalry',
    'mountaineer',
    'paratrooper',
    'marine',
    'marine_commando',
    'ranger',
    'mountaineers_mechanized',
    'amphibious_mechanized',
    'rangers_mechanized'
]

techId = {
    'infantry': '01',
    'motorized': '02',
    'mechanized': '03',
    'cavalry': '04',
    'mountaineer': '10',
    'paratrooper': '11',
    'marine': '12',
    'marine_commando': '13',
    'ranger': '14',
    'mountaineers_mechanized': '20',
    'amphibious_mechanized': '22',
    'rangers_mechanized': '24'
}

techUnitName = {
    'infantry': 'infantry',
    'motorized': 'motorized',
    'mechanized': 'mechanized',
    'cavalry': 'cavalry',
    'mountaineer': 'mountaineers',
    'paratrooper': 'paratrooper',
    'marine': 'marine',
    'marine_commando': 'marine_commando',
    'ranger': 'ranger_battalion',
    'mountaineers_mechanized': 'mountaineers_mechanized',
    'amphibious_mechanized': 'amphibious_mechanized',
    'rangers_mechanized': 'rangers_mechanized'
}

fileRepo = []


class FileText():
    def __init__(self, text, fileName='', path=dirPath, currentLine=0, name=''):
        self.text = text
        self.currentLine = currentLine
        self.name = name
        self.fileName = fileName

    def convert_text_to_str(self):
        textStr = ''
        for line in self.text:
            textStr += line

        return textStr

    def find_lines(self, token):
        self.currentLine = 0
        lineIds = []
        while self.currentLine != len(self.text):
            if self.text[self.currentLine].find(token) != -1:
                lineIds.append(self.currentLine)
            self.currentLine += 1
        return lineIds

    def remove_line(self):
        self.text.pop(self.currentLine)
        
    def add_line(self, line: str):
        self.text.insert(self.currentLine, line)

    def get_partition(self, edges=True):
        parentheses = 0
        partition = []
        while True:
            line = self.remove_comment()
                    
            parentheses += line.count('{')
            parentheses -= line.count('}')

            partition.append(line)
            self.currentLine += 1
            if parentheses == 0: break

        if not edges:
            partition.pop(0)
            partition.pop()
        return FileText(partition)

    def remove_comment(self):
        line = self.text[self.currentLine]
        if line.find('#') != -1:
            line = line.split('#')[0] + '\n'
        return line
           


def load_file(fileName: str, path=None):
    lines = []
    if path:
        filePath = path / fileName
    else:
        filePath = fileName
    with open(filePath, 'r') as f:
        for line in f:
            lines.append(line)
    fileText = FileText(lines, fileName)
    return fileText

def change_file(fileName: str, path, fileText: FileText):
    targetPath = path / fileName
    if targetPath.exists():
        os.remove(targetPath)
    fileTextStr = fileText.convert_text_to_str()
    with open(targetPath, 'w') as f:
        f.write(fileTextStr)

def get_platoon_tech(platoonFile, platoonId):
    name = platoonFile.name
    techToken = f'tom_inf_bat_{name}_{platoonId}_tech'
    line = platoonFile.find_lines(techToken)[0]
    platoonFile.currentLine = line
    technology = platoonFile.get_partition(False)
    length = len(technology.text)
    print(f'Extracted tom_inf_bat_{name}_{platoonId}_tech')
    print(f'Lines: {line+2}-{line+length+1}')
    return technology

def get_technology_lines(platoonFile, platoonId):
    name = platoonFile.name
    techToken = f'tom_inf_bat_{name}_{platoonId}_tech'
    return platoonFile.find_lines(techToken)

def list_files_with_platoon(platoonId):
    files = []
    for file in fileRepo:
        if file.find_lines(f'{platoonId}_tech') != []:
            files.append(file)
    return files

def convert_generic_tech(lines, newUnit, unit):
    newLines = []
    for line in lines:
        if line.find(unit + ' = {') != -1:
            newLine = line.replace(unit, newUnit)
        else:
            newLine = line
        newLines.append(newLine)
    return newLines

def convert_to_reset(unit, code):
    textObject = FileText(code)
    line = textObject.find_lines(unit + ' = {')[0]

    textObject.currentLine = line
    textPartition = textObject.get_partition()
    i = 0

    for partLine in textPartition.text:
        modifier = re.search(' = [0-9]', partLine)
        modifierNeg = re.search(' = -[0-9]', partLine)
        if modifier:
            newLine = partLine.replace(' = ', ' = -')
        elif modifierNeg:
            newLine = partLine.replace(' = -', ' = ')
        else:
            newLine = partLine
        code[line+i] = newLine
        i += 1

    return code

def create_tech_names():
    techFileNames = dict()
    for name in techNames:
        fileId = techId[name]
        filename = f'tom_inf_hidden_techs_{fileId}_{name}.txt'
        filenameReset = f'tom_inf_hidden_techs_{fileId}_{name}_reset.txt'
        techFileNames.update({name: [filename, filenameReset]})

    return techFileNames

def get_platoon_id_json():
    with open('platoonid.json') as f:
        data = json.load(f)
        return data['id']

def load_generic_platoon_tech():
    lines = []
    with open('platoontech.json') as f:
        for line in f:
            lines.append(line)
    return lines
    
def get_all_techs():
    global fileRepo
    names = create_tech_names().values()
    files = []
    i = 0
    
    for name in names:
        files.append(load_file(name[0], techPath))
        files[-1].name = techNames[i]
        files.append(load_file(name[1], techPath))
        files[-1].name = techNames[i]
        i += 1

    fileRepo = files
