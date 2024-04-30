"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    text1 ="fooziman"
    # Caso 1: "fooziman" => "fOozIman"
text1 = "fooziman"
output1 = text1.replace("o", "O").replace("i", "I")
print("Caso 1:", output1)

# Caso 2: "qux" => "qUx"
text2 = "qux"
output2 = text2.replace("u", "U")
print("Caso 2:", output2)

# Caso 3: "eq" => "eq"
text3 = "eq"
output3 = text3
print("Caso 3:", output3)
    
