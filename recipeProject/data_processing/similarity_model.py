import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict
import os

path = os.path.dirname(__file__)


def ingredient_compound_binary():
    ingredient_details = pd.read_csv(os.path.join(path, "../../python model/data/ingredient_info.tsv"), sep='\t')
    ingredients_compouds = pd.read_csv(os.path.join(path,"../../python model/data/ingredients_compounds.tsv"), sep='\t')
    compound_details = pd.read_csv(os.path.join(path,"../../python model/data/compound_info.tsv"), sep='\t')

    ingredients_compounds_joined = ingredient_details\
        .set_index("# id").join(ingredients_compouds.set_index("# ingredient id"))\
        .set_index("compound id").join(compound_details.set_index("# id"))\
        .drop(columns=["category", "CAS number"])

    compound_names = ingredients_compounds_joined[['Compound name']].drop_duplicates()
    ingredient_names = ingredients_compounds_joined[['ingredient name']].drop_duplicates()

    ingredient_names.to_pickle(os.path.join(path,"data/ingredient_names.pkl"))

    compounds = compound_names.values[:,0]
    ingredients = ingredient_names.values[:,0]

    ingredient_compounds_binary = []

    # for ingredient in ingredients:
    #     bin = []
    #     for compound in compounds:
    #         if
    for ingr in ingredients:
        ingredient_compoud = ingredients_compounds_joined.ix[ingredients_compounds_joined['ingredient name'] == ingr][['Compound name']].values[:,0]
        compounds_binary = ([1 if compound in ingredient_compoud else 0 for compound in compounds])
        ingredient_compounds_binary.append(compounds_binary)

    pd.DataFrame(ingredient_compounds_binary).to_pickle(os.path.join(path,"data/ingredient_compounds_binary.pkl"))


def get_recipe_ingredients_cos_similarity():

    ingredient_compounds_binary = pd.read_pickle(os.path.join(path,"data/ingredient_compounds_binary.pkl"))

    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(ingredient_compounds_binary).toarray()

    tfidf = pd.DataFrame.from_records(tfidf)
    tfidf.to_csv("data/tfidf_matrix.csv")

    cos = cosine_similarity(tfidf)

    return cos


def save_cos_similarities_to_pkl():
    """
    Gets and saves in pickle files the cosine similarities of the ingredients for both compounds and recipes and includes the
    ingredient labels for the columns and rows. The format of the sets is pandas DataFrame.
    """

    cos_compounds = pd.DataFrame(get_recipe_ingredients_cos_similarity())
    ingredient_names = pd.read_pickle(os.path.join(path,"data/ingredient_names.pkl"))

    cos_compounds.columns = ingredient_names.values[:, 0]
    cos_compounds.index = ingredient_names.values[:, 0]

    cos_compounds.to_pickle(os.path.join(path,"data/cos_compounds.pkl"))


def get_top_replacements(ingredient_name: str, threshold: float = 0.5):

    ingredient_name = ingredient_name.replace(' ', '_')
    cos_compounds = None
    try:
        cos_compounds = pd.read_pickle(os.path.join(path,"data/cos_compounds.pkl"))[ingredient_name]
    except:
        return {}

    d_descending = OrderedDict(sorted(cos_compounds.items(), key=lambda kv: kv[1], reverse=True))

    result = {}

    for k, v in d_descending.items():
        if (v < threshold):
            break
        if (k != ingredient_name):
            result[k] = v

    return result


if __name__ == "__main__":
    # ingredient_compound_binary()
    print(get_top_replacements(input("Ingredient name: ")))
