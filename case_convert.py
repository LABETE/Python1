#
# case_convert.py
#
s = "this Is a Simple string"
slower = s.lower() # s converted to lower case <--
supper = s.upper() # s converted to UPPER CASE <--
stitle = s.title() # s converted to Title Case <--
scapitalize = s.capitalize() # s converted to Capitalize case <--
sislower = s.islower()
sisupper = s.isupper()
sjoin = s.join("-")
stranslate = s.translate("Este es un simple string")
srsplit = s.split("-") 
sstartswith = s.startswith("I")

print(s, slower, supper, stitle, sc