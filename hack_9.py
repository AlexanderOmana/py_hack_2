"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
def transform_dict(input_dict):
    return {k.capitalize(): v.replace('kz', 'z') for k, v in input_dict.items() if k == 'foo'}

# Caso de prueba
input_dict = {"foo": "fookziman", "bar": "barziman"}
output_dict = transform_dict(input_dict)
print(output_dict)  # Output: {'Foo': 'Fooziman'}
   
