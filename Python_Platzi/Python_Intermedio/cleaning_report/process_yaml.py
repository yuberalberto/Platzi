import yaml

tipo = int(input("What type of sector are you looking for?"))

file = open("sectors.yaml")
dict_sectors = yaml.safe_load(file)

# dict_sectors is now a list of dicts - 
print(dict_sectors)

def yaml_count(dict_sectors, s):
    c = 0
    if isinstance(dict_sectors, dict):
        for k, v in dict_sectors.items:
            if k == s and v ==tipo: 
                c += 1
            c += yaml_count(v, s)
          #  print(k,v)
    elif isinstance(dict_sectors, list):
        for l in dict_sectors:
            c += yaml_count(l, s) 
    return c

print(yaml_count(dict_sectors, "type")) # returns 2
































