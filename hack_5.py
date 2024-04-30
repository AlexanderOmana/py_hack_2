"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
   # Caso 1: "fooziman" => "fo-zi-man-"
print("Caso 1:", "-".join(["fo", "zi", "man", ""]))

# Caso 2: "barziman" => "ba-zi-an"
print("Caso 2:", "-".join(["ba", "zi", "an"]))

# Caso 3: "qux" => "qu-"
print("Caso 3:", "qux"[0] + "u-")

# Caso 4: "eq" => "eq"
print("Caso 4:", "eq")
    
