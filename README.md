# Reeco Annotation Schema

This repository manages the Reeco Annotation Schema. 
Editing happens in this [Spreadsheet](https://docs.google.com/spreadsheets/d/1PZ11esT6COK7Y0mMZEHifY9hQeREbNSlRbC6dkYtjNg/edit?usp=sharing).

The reference documentation is in folder `schema/`.

To update the documentation:
```bash
python3 generate-schema.py && python3 generate-readme.py && git add schema/ && git commit -m "Update" && git push
```

