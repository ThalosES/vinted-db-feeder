# Vinted data scrapper

A series of data scrappers in Python that extract static information from the Vinted source code, being the perfect complement for a Vinted API wrapper.

## Install & Run

### Requirements

- Pip
- Python

1. Create a virtual environment

    ```bash
   python3 -m venv pyvenv/
   source venv/bin/activate
    ```

2. Run `requirements.txt`

   ```bash
    pip3 install -r requirements.txt
   ```

3. Run `main.py`

## Extracted data categories

| Element   | Fields Returned                                                                       |
|-----------|---------------------------------------------------------------------------------------|
| Brands    | Names, Ids                                                                            |
| Materials | Id, Name                                                                              |
| Colors    | Id, Color, Hex Code                                                                   |
| Sizes     | Id, Size, Category                                                                    |
| Categories| Id, Title, Code, Parent Id, URL, URL EN, Item Count                                    |
| Categories Children | Category Id, Child Id                                                       |

### Materials

- Available languages: 🇪🇸 🇫🇷 🇺🇸
  - [More languages can be added if html file included in `data/raw/materials`]

### Categories - Catalogs

- **Debug mode:** Builds the full decision tree

- **Exec mode:** Returns 2 CSVs:
  
  - `categories.csv`: Table of all the available categories and their attributes

  - `categories_children.csv`: Dictionary that models the Category->Children list relationship

## Performance

- Without brands search:

```bash
real    0m0,756s
user    0m0,457s
sys     0m0,041s
```

## Authors

[Álvaro Cabo](https://github.com/alvarocabo)

[Pepe Márquez](https://github.com/pxp9)
