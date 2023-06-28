from lib import get_brands_ids, get_materials, get_sizes, constants

if(__name__=="__main__"):
    
    # Get brands ids from names
    get_brands_ids.exec(constants.BRANDS_FOLDER, constants.BRANDS_OUTFILE)

    # Get materials
    get_materials.exec(constants.MATERIALS_OUTFILE)