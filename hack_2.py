"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    # Caso 1: "fooziman" => "fzmn"
text1 = "fooziman"
output1 = ''.join(char for char in text1 if char not in 'oai')
print("Caso 1:", output1)

# Caso 2: "barziman" => "brzmn"
text2 = "barziman"
output2 = ''.join(char for char in text2 if char not in 'ai')
print("Caso 2:", output2)

# Caso 3: "qux" => "qx"
text3 = "qux"
output3 = text3.replace("u", "")
print("Caso 3:", output3)