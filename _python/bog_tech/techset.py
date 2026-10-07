import techhandlerbog as bog


if __name__ == '__main__':
    bog.get_all_techs()
    platoonId = bog.get_platoon_id_json()
    filesToEdit = bog.list_files_with_platoon(platoonId)
    genericCode = bog.load_generic_platoon_tech()
    genericUnit = bog.techUnitName[filesToEdit[0].name]
    print(f'Edited Unit Name: {genericUnit}')
    print(f'Edited Platoon ID: {platoonId}')

    for file in filesToEdit:
        print('')
        print(f'Editing {file.fileName}')
        startLines = bog.get_technology_lines(file, platoonId)
        print(f'Matching Techs found at: {startLines}')
        newUnit = bog.techUnitName[file.name]
        print(newUnit)
        newCode = bog.convert_generic_tech(genericCode, newUnit, genericUnit)
        if file.fileName.find('reset') != -1:
            newCode = bog.convert_to_reset(newUnit, newCode)
        newCodeRev = newCode.copy()
        newCodeRev.reverse()

        while len(startLines) != 0:
            line = startLines.pop()
            file.currentLine = line
            code = file.get_partition(False)
            file.currentLine = line + 1

            for oldLine in code.text:
                file.remove_line()

            for newLine in newCodeRev:
                file.add_line(newLine)

        bog.change_file(file.fileName, bog.techPath, file)
        print(f'Successfully changed {file.fileName}')
