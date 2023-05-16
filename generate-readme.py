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

def makeLink(o):
    if 'type' in o:
        return "[%s](#%s)" % (o['type'],o['type'])
    if 'term' in o:
        return "[%s](#%s)" % (o['term'],o['term'])
    else:
        return "[%s](#%s)" % (o,o)

SCHEMA = Schema()

TXT = TXT + """

## Containers and Components
"""

TXT = TXT + """

Template for containers (remove terms that you don't need):
```yaml
---
container-id: fabulous
type: Project
name: The Fabulous Project
description: The Fabulous Project is a very important part of the ecosystem.
image: http://www.example.org/myimage.png
logo:  http://www.example.org/logo.png
work-package: 
- WP1
- WP2
pilot:
- ThePilot
project: a-fabulous-project
funder:
  - name: Lorem Ipsum Funder
    url: https://www.lorem-ipsum-funder.org
    grant-agreement: "01234556"
credits: "This project has received funding from the Lorem Ipsum Funder research and innovation programme under grant agreement 01234556."
bibliography:
- main-publication: "Brown, L. (2019). The Role of Parenting Styles in Child Development. Child Development Perspectives, 13(3), 145-153."
- publication: 
  - "Smith, J. (2020). The Impact of Social Media on Mental Health. Journal of Psychology and Behavioral Sciences, 15(2), 45-62."
- has-part:
  - fabulous-component-source-code
  - fabulous-docs
  - fabulous-tutorials
  - fabulous-evaluation
  - fabulous-requirements
  - fabulous-dataset

---

# The Fabulous Project

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

[Link to the website](http://www.example.org)
```

Template for components (remove terms that you don't need):

```yaml
---
component-id: fabulous-component-source-code
type: Software
name: The Fabulous Source Code
description: Source code of The Fabulous
logo: https://www.example.org/logo.png
work-package: 
- WP1
- WP2
pilot:
- ThePilot
project: a-fabulous-project
resource: https://github.com/fabulous-inc/repo1/releases
demo: https://www.example.org/fabulous/demo
release-date: 2023/01/18
release-number: v1.0-alpha
release-link: https://github.com/fabulous-inc/repo1/releases/tag/v0.8.1
doi: 10.5281/zenodo.000000
changelog: https://github.com/fabulous-inc/repo1/releases/tag/v0.8.1
licence:
- Apache-2.0
copyright: "Copyright (c) 2023 Fabolous, Inc"
contributors:
- A developer <http://www.example.org>
related-components:
- informed-by:
  - fabulous-requirements
- use-case:
  - fabulous-uc
- story:
  - fabulous-story
- persona:
  - fabulous-persona
- documentation: 
  - fabulous-component-docs
  - fabulous-component-tutorials
- extends:
  - "A Java project Jena https://www.example.org"
- reuses:
  - "Apache Camel https://camel.apache.org/"
- generated-by:
  - The AI code generator http://www.my-software-factory.com
- evaluated-in:
  - fabulous-evaluation
credits: "This project has received funding from the Lorem Ipsum Funder research and innovation programme under grant agreement 01234556."

---

# The Fabulous Component

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

[Link to the website](http://www.example.org)

```

"""

TXT = TXT + """

### List of types

Container types:
"""
# List of container types
for component in SCHEMA.containers():
    TXT = TXT + "\n - " + makeLink(component) + " " + SCHEMA.asString(component, 'description')
    for sub1 in SCHEMA.subtypes(component['type']):
        TXT = TXT + "\n   - " + makeLink(sub1) + " " + SCHEMA.asString(sub1, 'description')

TXT = TXT + """

Component types:
"""
# List of component types
for component in SCHEMA.components():
    TXT = TXT + "\n - " + makeLink(component)
    for sub1 in SCHEMA.subtypes(component['type']):
        TXT = TXT + "\n   - " + makeLink(sub1)
        for sub2 in SCHEMA.subtypes(sub1['type']):
            TXT = TXT + "\n    - " + makeLink(sub2)
            for sub3 in SCHEMA.subtypes(sub2['type']):
                TXT = TXT + "\n     - " + makeLink(sub3)
                for sub4 in SCHEMA.subtypes(sub3['type']):
                    TXT = TXT + "\n      - " + makeLink(sub4)
 
# List of terms to annotate containers
TXT = TXT + """

### Terms for Containers
"""
for term in SCHEMA.termsFor('Container'):
    TXT = TXT + "\n - " + makeLink(term)
    for sub1 in SCHEMA.subterms(term):
        TXT = TXT + "\n   - " + makeLink(sub1)
        for sub2 in SCHEMA.subterms(sub1):
            TXT = TXT + "\n     - " + makeLink(sub2)
            for sub3 in SCHEMA.subterms(sub2):
                TXT = TXT + "\n       - " + makeLink(sub3)
    


TXT = TXT + """

### Terms for Components

"""
for term in SCHEMA.termsFor('Component'):
    TXT = TXT + "\n - " + makeLink(term)
    for sub1 in SCHEMA.subterms(term):
        TXT = TXT + "\n   - " + makeLink(sub1)
        for sub2 in SCHEMA.subterms(sub1):
            TXT = TXT + "\n      - " + makeLink(sub2)
            for sub3 in SCHEMA.subterms(sub2):
                TXT = TXT + "\n        - " + makeLink(sub3)
                for sub4 in SCHEMA.subterms(sub4):
                    TXT = TXT + "\n          - " + makeLink(sub4)

TXT = TXT + """

## Types (A-Z)

"""
types = SCHEMA.types()
for typee in sorted(types, key = lambda x: x['type'].lower()):
    TXT = TXT + "\n### " + typee['type'] + "\n\n"
    ks = ['type', 'label', 'supertype-id']
    TXT = TXT + "\n| Type | Label | Super type | \n | ----- | ----- | ----- |"
    TXT = TXT + "\n |" + typee['type'] + " | " + typee['label'] + "|" 
    if 'supertype-id' in typee: 
        TXT = TXT + typee['supertype-id'] 
    TXT = TXT + "|\n"
    if 'description' in typee:
        TXT = TXT + "\n\n" + str(typee[ 'description'])
    # if 'example-values' in term and term['example-values'].strip() != '':
    #    TXT = TXT + "\n\nExample:\n\n```\n" + str(term[ 'example-values']) + "\n```\n\n"

TXT = TXT + """

## Terms (A-Z)

"""
# sorted(self._yaml['terms'], key = lambda pos: self._yaml['terms'][pos]['_position'])
terms = SCHEMA.terms()
doneTerms = []
for term in sorted(terms, key = lambda x: x['term'].lower()):
    if term['term'] not in doneTerms:
        TXT = TXT + "\n### " + term['term'] + "\n"
        doneTerms.append(term['term'])
    else:
        TXT = TXT + "\nThe term " + term['term'] + " can also be used in a " + term['scope'] + "\n" 
    TXT = TXT + "\n| Term | Label | Scope | Super term | Mandatory |"
    TXT = TXT + "\n| ---- | ---- | ---- | ---- | ---- |"
    ks = ['term', 'label', 'scope', 'super-term', 'mandatory']
    TXT = TXT + "\n"
    for k in ks:
        if k in term:
            TXT = TXT + " | " + str(term[k]) 
        else:
            TXT = TXT + " | "
    TXT = TXT + "\n\n"
    
    # TXT = TXT + "\n\n**domain**: " 
    # for d in term['domain']:
    #     TXT = TXT + "\n\n - " + makeLink(d) 
    if 'description' in term:
        TXT = TXT + "\n\n" + str(term[ 'description'])
    if 'example-values' in term and len(term['example-values']) != 0:
        TXT = TXT + "\n\nExample:\n"
        for example in term['example-values']:
            TXT = TXT + "\n```\n" + str(example) + "\n```\n"

TXT = TXT + """

## Licences

"""

for licence in SCHEMA.licences():
    TXT = TXT + "\n### " + licence['title'] + "\n"
    TXT = TXT + "\n\n*Licence:* " + licence['title'] 
    TXT = TXT + "\n\n*Use code:* `" + licence['code'] + '`'
    TXT = TXT + "\n\n*Publisher:* " + licence['publisher'] 
    TXT = TXT + "\n\n*Legal text:* [" + licence['link'] + "](" + licence['link'] + ")\n\n"

with open(output_readme, "w") as text_file:
    text_file.write(TXT)