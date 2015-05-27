#!/usr/local/bin/python3
"""Accept format strings from the user and format fixed data."""
i = 42
r = 31.97
c = 2.2 + 3.3j
s = "String"
lst = ["zero", "two", "three", "four", "five"]
dct = {"Jim": "Dady",
    "Stella": "DoBois",
    1: "integer"}
while True:
    fmt = input("Format string: ")
    if not fmt:
        break
    fms = "{" + fmt + "}"
    print("Format:", fm