"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
  result = s
 

# Caso 1: "fooziman" => "oozima"
text1 = "fooziman"
output1 = text1[1:-1]
print("Caso 1:", output1)

# Caso 2: "barziman" => "arzima"
text2 = "barziman"
output2 = text2[1:-1]
print("Caso 2:", output2)

# Caso 3: "qux" => "qux"
text3 = "qux"
output3 = text3
print("Caso 3:", output3)

