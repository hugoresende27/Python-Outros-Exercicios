#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both 
# strings.
#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

def string_match(a, b):
    curto = min(len(a),len(b))
    cont =0
    for i in range (curto-1):
        # aString= a[i:i+2]
        # bString= b[i:i+2]
        # if (aString == bString):
        if (a[i:i+2] ==b[i:i+2] ):
            cont+=1
    return cont



print (string_match('xxcaazz', 'xxbaaz'))
print (string_match('abc', 'abc'))
print (string_match('abc', 'axc'))
