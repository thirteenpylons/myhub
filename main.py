"""
Print out eng page and equipment

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
                print(f"Failed to extract...")

l = []
for k in contents:
    if contents[k] != "None":
        l.append(f"{k} {contents[k]}")

for x in l:
    with open("equipment.txt", "a") as jfile:
        jfile.write(f"{x}\n")