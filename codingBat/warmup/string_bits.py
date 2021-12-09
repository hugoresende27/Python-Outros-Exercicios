#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    tam = len(str)
    nova = ""
    for i in range (tam):
        nova += str[i:2:2]
    return nova

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
