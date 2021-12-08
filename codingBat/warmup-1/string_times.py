#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
    if (n>0):
        return n*str
    else:
        return ""
    
def string_times2(str, n):
    res = ""
    for i in range (n):
        res += str
    return res
    
    
print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))
print(string_times('Hi', 0))
print("##########################")
print(string_times2('Hi', 2))
print(string_times2('Hi', 3))
print(string_times2('Hi', 1))
print(string_times2('Hi', 0))