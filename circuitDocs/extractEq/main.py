"""
Crawl circuit documentation and return core data from circuit.

This is a script that I used to find the SN of the equipment to match
the account for balancing.

Author: Christian M. Fulton
Date: 26.Nov.2021
"""

import os
from openpyxl import load_workbook as LW


d = input("Enter the directory to crawl: ")
contents = {}
for subdir, dirs, files in os.walk():
    for f in files:
        if f.endswith(".xlsx"):
            try:
                doc = LW(filename=os.path.join(subdir, f))
                WS = doc.active
                name = WS["B6"].value
                eng = WS["D6"].value
                equipment = WS["B19"].value
                acc = WS["B10"].value
                print(name, eng, acc, equipment)
                contents[str(name)] = str(eng), str(acc), str(equipment)
                print("Successfully extracted...")
            except:
                print('Failed to extract...')

l = [f'{k} {v}' for k, v in contents.items() if contents[k] != "None"]
for x in l:
    with open("equipment.txt", "a") as jfile:
        jfile.write(f"{x}\n")