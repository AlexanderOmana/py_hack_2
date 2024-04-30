"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    # Caso 1: ["a","b","c","d","e"] => ["1",2,"3",4,"5"]
text1 = ["a", "b", "c", "d", "e"]
output1 = []
i = 0
while i < len(text1):
    output1.append(str(i+1) if i % 2 == 0 else i+1)
    i += 1
print("Caso 1:", output1)

# Caso 2: [] => [0]
text2 = []
output2 = [0] if not text2 else output1
print("Caso 2:", output2)
    
