"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
input_data = [{"a":"b"},{"c":"d"},{"e":"f"}]
output_data = []

for item in input_data:
    new_item = {}
    for key, value in item.items():
        new_key = str(len(output_data)*2 + 1)
        new_value = str(len(output_data)*2 + 2)
        new_item[new_key] = new_value
    output_data.append(new_item)

print(output_data)


