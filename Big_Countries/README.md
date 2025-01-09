# Big Countries Solution

This project provides a solution to filter and display big countries based on specific criteria:

```python
big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
```

### Criteria:
1. Area of at least **3,000,000 km²**.
2. Population of at least **25,000,000**.

The result includes the `name`, `population`, and `area` of the countries.
