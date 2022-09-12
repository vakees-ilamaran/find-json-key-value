# find-json-key-value
Retrieves the value of the key passed in the nested json object

## Usage

$ python3 retrive_value_from_json.py --help  
```                                                                                    
Usage: retrive_value_from_json.py [OPTIONS]

Options:
  --obj TEXT  [required]
  --val TEXT  The value to find.  [required]
  --help      Show this message and exit. 
```


$ python3 retrive_value_from_json.py --obj '{"a":{"b":{"c":"d"}}}' --val 'a/b'
```
{'c': 'd'}
```

$ python3 retrive_value_from_json.py --obj '{"a":{"b":{"c":"d"}}}' --val 'a/b/c'
```
d
```