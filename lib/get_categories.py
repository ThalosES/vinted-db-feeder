import json

class Category:
    def __init__(self, id: int, title, code: str, parent_id:int, url,
                 url_en, item_count: int, children_ids: list[int]):
        self.id = id
        self.title = title
        self.code = code
        self.parent_id = parent_id
        self.url = url
        self.url_en = url_en
        self.item_count = item_count
        self.children_ids = children_ids

def get_data(filename):
    file = open(filename, "r")
    r =json.load(file)
    return (r["catalogs"], r["catalog_children_tree"])

def deserialize_json(catalogs: dict, tree: dict):
    res = {}
    for id in catalogs:
        catalog=catalogs.get(id)
        children_ids = tree.get(str(catalog["id"]), [])
        cat = Category(catalog["id"], catalog["title"],
                            catalog["code"], catalog["parent_id"], 
                            catalog["url"], catalog["url_en"], 
                            catalog["item_count"], children_ids)
        res[catalog["id"]] = cat
    return res

def exec(filename):
    a: dict
    b: dict 
    a,b = get_data(filename)

    r= deserialize_json(a, b)
    #print(r)
