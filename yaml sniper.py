from ast import parse
import yaml

#Setting up the file to be parsed.
with open('yaml-file.yaml', 'r') as file:
    sniper = yaml.safe_load(file)

#This will filter and extract the values out of the file. You can add as many steps as you need. Values will be a list object.
values=sniper['dictionary']['key']

#Making the list a string. In case you need it.
strtarget=' '.join([str(elem) for elem in values])