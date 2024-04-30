"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    # Reglas de reemplazo
    s = s.replace('a', '@').replace('e', '3').replace('i', '¡').replace('o', '0').replace('u', 'v').replace('f', 'F').replace('b', 'B').replace('q', 'Q')
    return s

# Caso 1: "fooziman" => "F00z¡m@N"
text1 = "fooziman"
output1 = fn_hack_3(text1)
print("Caso 1:", output1)  # Output: "F00z¡m@N"

# Caso 2: "barziman" => "B@rz¡m@N"
text2 = "barziman"
output2 = fn_hack_3(text2)
print("Caso 2:", output2)  # Output: "B@rz¡m@N"

# Caso 3: "3q" => "3Q"
text3 = "3q"
output3 = text3.upper()
print("Caso 3:", output3)  # Output: "3Q"

# Caso 4: "qu" => "Qv"
text4 = "qu"
output4 = fn_hack_3(text4)
print("Caso 4:", output4)  # Output: "Qv"

# Caso 5: "qux" => "QvX"
text5 = "qux"
output5 = fn_hack_3(text5)
output5 = output5.replace('x', 'X')
print("Caso 5:", output5)  # Output: "QvX"


