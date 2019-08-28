import json

j = json.dumps([
    "foo",
    {
        'bar': ('baz', None, 1.4, 2)
    }
])

print(j)   #see output data format compared to above