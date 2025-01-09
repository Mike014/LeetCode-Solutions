# Recyclable and Low Fat Products

This project provides a solution to filter and retrieve the `product_id` values for products that satisfy the following conditions:

- **`low_fats`**: The product is low fat (`'Y'`).
- **`recyclable`**: The product is recyclable (`'Y'`).

### Solution
The filtering is done using Pandas with the following code:

```python
filtered_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
filtered_product_ids = pd.DataFrame(filtered_products['product_id'])
```

### Explanation
1. **Filtering**:
   - The condition `(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')` selects only the rows where both conditions are true.
2. **Extracting `product_id`**:
   - The filtered `product_id` values are extracted into a new Pandas DataFrame.

### Result
The result is a DataFrame containing only the `product_id` of products meeting both conditions.
