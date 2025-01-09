import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # filtering the products that are low fats and recyclable
    filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    # returning the product_id of the filtered products converted to a DataFrame
    return pd.DataFrame(filtered_products['product_id'])






