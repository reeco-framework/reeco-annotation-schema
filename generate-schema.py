import csv
import yaml
import io
import requests

# https://docs.google.com/spreadsheets/d/1PZ11esT6COK7Y0mMZEHifY9hQeREbNSlRbC6dkYtjNg/edit?usp=sharing
doc = "1PZ11esT6COK7Y0mMZEHifY9hQeREbNSlRbC6dkYtjNg"
terms_tab = "Terms"
types_tab = "Types"
licences_tab = "Licences"
terms_csv = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&sheet=%s' % (doc, terms_tab)
types_csv = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&sheet=%s' % (doc, types_tab)
licences_csv = 'https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&sheet=%s' % (doc, licences_tab)

output_yml = "./schema/schema.yml"

split_by = {
    'enum':',',
    'xsd-datatype':',',
    'domain':'|'
}

def dictify(input_csv):
    dictionary = {}
    r = requests.get(input_csv)
    buff = io.StringIO(r.text)
    cr = csv.DictReader(buff)
    position = 0
    for row in cr:
        position = position + 1
        ID = ''
        if 'Scope' in row.keys():
            ID = row['Scope'] + '/'
        if 'Super term' in row.keys() and row['Super term'] != '':
            ID = ID + row['Super term'] + '/'
        if 'Supertype Id' in row.keys() and row['Supertype Id'] != '':
            ID = ID + row['Supertype Id'] + '/'
        if 'Term' in row.keys(): # Terms
            ID = ID + row['Term'] 
        elif 'Type' in row.keys(): # Types
            ID = ID + row['Type']
        elif 'Code' in row.keys(): # Licences
            ID = ID + row['Code']
        else:
            raise ValueError('Bad row: ' + row)
        dictionary[ID] = {}
        dictionary[ID]['_position'] = position
        for key in row:
            k = key.lower().replace(' ','-')
            v = row[key]
            if k in split_by.keys():
                v = v.split(split_by[k])
            if row[key]:
                dictionary[ID][k] = v
    return dictionary

types = dictify(types_csv)
terms = dictify(terms_csv)
licences = dictify(licences_csv)
schema = {}
schema['types'] = types
schema['terms'] = terms
schema['licences'] = licences
yaml.dump(schema,open(output_yml,'w'))
