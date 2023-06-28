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
        self.children = []

    def __str__(self, level=0):
        indent = "  " * level
        tree_str = f"{indent}- {self.title} ({self.id})\n"
        for child in self.children:
            tree_str += child.__str__(level + 1)
        return tree_str

def get_data(filename: str):
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

def draw_tree(category_dict):
        root_categories = []
        category_map = {}

        # Iterate over the category dictionary to create Category objects and populate the category map
        for category_id, category_object in category_dict.items():
            category = Category(category_object.id, category_object.title, category_object.code,
                                category_object.parent_id, category_object.url, category_object.url_en,
                                category_object.item_count, category_object.children_ids)
            category_map[category_id] = category

        # Build the category tree using the children_ids property
        for category_id, category_object in category_dict.items():
            parent_id = category_object.parent_id
            if parent_id == 0:
                root_categories.append(category_map[category_id])
            else:
                try:
                    parent_category = category_map[parent_id]
                    parent_category.children.append(category_map[category_id])
                except KeyError:
                    root_categories.append(category_map[category_id])

        return root_categories

def generate_cat_tree(source):
    a,b = get_data(source)
    r= deserialize_json(a, b)
    root_categories = draw_tree(r)

    res = ""
    for root_category in root_categories:
        res+=str(root_category)+"\n"
    return res

def exec(source, outfile):
    outfile = open(outfile, "w")
    outfile.write(generate_cat_tree(source))
    outfile.close()
