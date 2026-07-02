# Make a copy of equipment_designs.txt, with create_design format
fileText = '###DESIGNS FOR AI AND CREATE_EQUIPMENT_VARIANT EFFECT\n'
variantName = ''

def reformat(line):
    global fileText
    global variantName
    # Sections
    if line.find('tank_designs={') != -1:
        fileText += '###TANK/AC/MECHANIZED/INFANTRY DESIGNS\n'
    elif line.find('ship_designs={') != -1:
        fileText += '###SHIP DESIGNS\n'
    elif line.find('plane_designs={') != -1:
        fileText += '###PLANE DESIGNS\n'

    # Equipment
    elif line.find('equipment={') != -1:
        line = line.replace('\n', '')
        fileText += line + '\t#Don\'t forget to rename this!\n'
    elif line.find('name=') != -1:
        line = line.replace('name=', '')
        line = line.replace('\"', '')
        line = line.replace('\t', '')
        variantName = line
    elif line.find('type=') != -1:
        line = line.replace('\"', '')
        fileText += line
    elif line.find('target_variant=') != -1:
        fileText += '\t\t#' + variantName + line
    elif line.find('match_value=') != -1:
        line = line.replace('\n', '')
        fileText += line + '\t#Delete for create_equipment_variant Effect\n'

    # Modules
    elif line.find('modules={') != -1:
        fileText += line
    elif line.find('_slot"="') != -1:
        line = line.replace('\"', '')
        fileText += line
    elif line.find('upgrades={') != -1:
        fileText += line
    elif line.find('_upgrade=') != -1:
        fileText += line
        
    elif line.find('}') != -1:
        fileText += line

with open('equipment_designs.txt', 'r') as f:
    for line in f:
        reformat(line)

with open('equipment_designs_reformatted.txt', 'w') as f:
    f.write(fileText)
