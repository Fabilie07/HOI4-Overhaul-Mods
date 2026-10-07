The scripts in this folder are used to edit the effect of adding specific Platoons to the Battalion Designer.
To use them, Python 3 must be installed.
Here's how to use them:

1. Open platoonid.json
2. Enter the ID of the Platoon you want to edit
3. Execute techget.py
4. Open platoontech.json
5. Change the code to the one you want to implement
6. Execute techset.py
7. Manually change the Localisation and Scripted Effect to reflect the Stat changes in the Battalion Designer's GUI

IMPORTANT NOTICES
- The code you write into platoontech.json must be able to be correctly executed by Hoi4
- Avoid using the Unit's Name, any valid Platoon ID, unnecessary Brackets or other Syntax elements where they are not needed
- Hoi4-style comments in platoontech.json may be removed by the script
- Stick to the given formatting, e.g. spaces before and after each equation sign
- DO NOT change platoonid.json or any Technology File inbetween steps 3 and 6
- Always double-check that the script executed properly
- This script assumes that each instance of a Platoon has the same effect for all battalions. Any unit-specific changes must be added manually afterwards