#Given a string, return a new string where "not " has been added to the front. However, 
# if the string already begins with "not", return the string unchanged.
#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

def not_string(str):
    if (str.find('not',0,4) != -1): # != -1 contém a string !
        return str
    else:
        return 'not '+str
    
def not_stringRes(str):
    if len(str)>=3 and str[:3] == "not":
        return str
    else:
        return "not "+str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print(not_string('is not'))
print(not_stringRes('candy'))
print(not_stringRes('x'))
print(not_stringRes('not bad'))
print(not_stringRes('is not'))