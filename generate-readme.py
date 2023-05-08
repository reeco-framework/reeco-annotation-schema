import yaml
import sys
from reeco import Schema

output_readme = 'schema/README.md'

# def terms(s):
#     return sorted(s['terms'], key=lambda d: d['_position'])

TXT = """# Annotation schema

**Do not edit: this file is automatically generated**

## Introduction
"""

SCHEMA = Schema()

TXT = TXT + """

## Containers and Components
"""

TXT = TXT + """

### List of types

Container types:
"""
# List of container types
for component in SCHEMA.containers():
    TXT = TXT + "\n - " + component['type']
    for sub1 in SCHEMA.subtypes(component['type']):
        TXT = TXT + "\n. - " + sub1['type']
        for sub2 in SCHEMA.subtypes(sub1['type']):
            TXT = TXT + "\n   - " + sub2['type']
            for sub3 in SCHEMA.subtypes(sub2['type']):
                TXT = TXT + "\n    - " + sub3['type']
                for sub4 in SCHEMA.subtypes(sub3['type']):
                    TXT = TXT + "\n     - " + sub4['type']
TXT = TXT + """

Component types:
"""
# List of component types
for component in SCHEMA.components():
    TXT = TXT + "\n - " + component['type']
    for sub1 in SCHEMA.subtypes(component['type']):
        TXT = TXT + "\n  - " + sub1['type']
        for sub2 in SCHEMA.subtypes(sub1['type']):
            TXT = TXT + "\n   - " + sub2['type']
            for sub3 in SCHEMA.subtypes(sub2['type']):
                TXT = TXT + "\n    - " + sub3['type']
                for sub4 in SCHEMA.subtypes(sub3['type']):
                    TXT = TXT + "\n      - " + sub4['type']
 
# List of terms to annotate containers
TXT = TXT + """

### Terms for Containers
"""
for term in SCHEMA.termsFor('Container'):
    TXT = TXT + "\n - " + term['term']
    for sub1 in SCHEMA.subterms(term['term']):
        TXT = TXT + "\n  - " + sub1['term']
        for sub2 in SCHEMA.subterms(sub1['term']):
            TXT = TXT + "\n   - " + sub2['term']
    


TXT = TXT + """

### Terms for Components

"""
for term in SCHEMA.termsFor('Component'):
    TXT = TXT + "\n - " + term['term']
    for sub1 in SCHEMA.subterms(term['term']):
        TXT = TXT + "\n  - " + sub1['term']
        for sub2 in SCHEMA.subterms(sub1['term']):
            TXT = TXT + "\n    - " + sub2['term']

TXT = TXT + """

## Terms

"""

for term in SCHEMA.terms():
    TXT = TXT + "\n### " + term['term'] + "\n"
    ks = ['term', 'label', 'scope', 'super-term', 'mandatory']
    for k in ks:
        if k in term:
            TXT = TXT + "*" + k + "*: " + str(term[k]) + "\n"
    if 'description' in term:
        TXT = TXT + "\n" + str(term[ 'description']) + "\n"
    if 'example-values' in term and term['example-values'] != '':
        TXT = TXT + "\n\n```" + str(term[ 'example-values']) + "\n```\n\n"

with open(output_readme, "w") as text_file:
    text_file.write(TXT)