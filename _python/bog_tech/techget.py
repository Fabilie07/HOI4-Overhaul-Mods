import techhandlerbog as bog


bog.get_all_techs()

platoonId = bog.get_platoon_id_json()
fileText = bog.list_files_with_platoon(platoonId)[0]
technology = bog.get_platoon_tech(fileText, platoonId)
bog.change_file('platoontech.json', bog.jsonPath, technology)
