"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
   # Caso 1: ["a","b","c","d","e"] => ["1","-","3","-","5"]
text1 = ["a", "b", "c", "d", "e"]
output1 = []
for i, char in enumerate(text1):
    output1.append(str(i+1) if i % 2 == 0 else "-")
print("Caso 1:", output1)

# Caso 2: [] => ["0"]
text2 = []
output2 = ["0"] if not text2 else [str(i+1) if i % 2 == 0 else "-" for i, _ in enumerate(text2)]
print("Caso 2:", output2)


