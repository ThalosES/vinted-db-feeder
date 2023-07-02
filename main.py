from lib import get_brands_ids, get_colors, get_materials, get_sizes, constants, get_categories

def debug():
    # Get brands ids from names
    # get_brands_ids.exec(constants.BRANDS_FOLDER, constants.BRANDS_OUTFILE)

    # Get materials
    get_materials.exec(constants.MATERIALS_FOLDER, constants.MATERIALS_OUTFOLDER, constants.MATERIALS_OUTFILE)

    # Get sizes
    get_sizes.exec(constants.SIZES_FOLDER, constants.SIZES_OUTFILE)

    # Get colors
    get_colors.exec(constants.COLORS_OUTFILE)
    
    # Get Categories

    get_categories.exec(constants.CATEGORIES_INFILE, constants.CATEGORIES_OUTFILE, constants.CATEGORIES_TREE_OUTFILE)


if(__name__=="__main__"):
    # get_materials.exec(constants.MATERIALS_FOLDER, constants.MATERIALS_OUTFOLDER, constants.MATERIALS_OUTFILE)
    # NEVER RUN COUNTRIES
    get_categories.exec(constants.CATEGORIES_INFILE, constants.CATEGORIES_OUTFILE, constants.CATEGORIES_TREE_OUTFILE)
