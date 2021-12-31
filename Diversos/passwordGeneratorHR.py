import random

mins = "abcdefghijlmnopqkrstuvxywz"
maxs = "ABCDEFGHIJLMNOPQKRTSUVWYXZ"
nums = "0123456789"
#simbs = "@#*&%$"

todos = mins + maxs + nums #+ simbs #Elementos que vão compor a password

comps = 8       #comprimento da password

pw = "".join(random.sample(todos, comps))      #função join com string vazia "" + função random + função sample (elementos,legth)

print ("PASSWORD:::" ,pw)