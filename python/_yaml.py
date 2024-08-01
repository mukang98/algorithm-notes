# %%
# ================================================================= #
#                        1.Yaml                                     #
# ================================================================= #
### Usage1 : Convert a Python object to a YAML-formatted string ###
import yaml

raw_data = {
    "Type": "animal", 
    "Location": "land",  
    "Name": ["dog", "cat", "rabbit"]}

yaml_data = yaml.dump(raw_data, sort_keys=False) 
#Parameter "sort_keys=False" prevents automatic sorting of dictionary keys in the output.
print(yaml_data)
with open("./tmp/yaml_test.txt", "w") as f:
    yaml.dump(raw_data, f, sort_keys=False) #Write to txt
# %%
### Usage2 : Convert a YAML-formatted string to a Python object ###
import yaml

yaml_data = """
Type: animal
Location: land
Name:
- dog
- cat
- rabbit
"""
data = yaml.safe_load(yaml_data)
print("data from variable: ", data)
with open("./tmp/yaml_test.txt", "r") as f:
    data_txt = yaml.safe_load(f) # Read from txt
    print("data from txt: ", data_txt)
# %%
