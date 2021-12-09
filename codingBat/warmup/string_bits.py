#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    tam = len(str)
    nova = ""
    for i in range (0,tam,2):
        nova += str[i:i+1]
    return nova

def string_bits2(str):
    tam = len(str)
    nova = ""
    for i in range(tam):
        if (i % 2 == 0):        #outra solução, fazer os indexs pares apenas
            nova += str[i]
    return nova

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))

print(string_bits2('Hello'))
print(string_bits2('Hi'))
print(string_bits2('Heeololeo'))
