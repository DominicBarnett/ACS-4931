# by Kami Bigdely
# Split temporary variable
# This program calculates the total weight of different burger configurations
# by combining various ingredients with their respective weights

# Define individual ingredient weights in grams
patty = 70  # [gr] - weight of a single beef patty
pickle = 20  # [gr] - weight of a pickle slice
tomatoes = 25  # [gr] - weight of tomato slices
lettuce = 15  # [gr] - weight of lettuce
buns = 95  # [gr] - weight of burger buns (top and bottom)

# Calculate total weight for NY Burger ingredients
# NY Burger uses 2 patties, 4 pickles, 3 tomatoes, 2 lettuce portions, and 2 buns
ny_patties_weight = 2 * patty  # Total weight of 2 beef patties
ny_pickles_weight = 4 * pickle  # Total weight of 4 pickle slices
ny_tomatoes_weight = 3 * tomatoes  # Total weight of 3 tomato slices
ny_lettuce_weight = 2 * lettuce  # Total weight of 2 lettuce portions
ny_buns_weight = 2 * buns  # Total weight of 2 buns (top and bottom)

# Calculate total NY Burger weight by summing all ingredients
ny_burger_weight = ny_patties_weight + ny_pickles_weight + ny_tomatoes_weight + ny_lettuce_weight + ny_buns_weight
print("NY Burger Weight", ny_burger_weight)

# Define additional ingredients for Seoul Kimchi Burger
kimchi = 30  # [gr] - weight of kimchi (Korean fermented vegetables)
mayo = 5  # [gr] - weight of mayonnaise
golden_fried_onion = 20  # [gr] - weight of golden fried onions

# Calculate total weight for Seoul Kimchi Burger
# This burger uses the same base ingredients as NY Burger plus kimchi, mayo, and fried onions
seoul_kimchi_burger_weight = (
    ny_patties_weight + ny_pickles_weight + ny_tomatoes_weight +
    kimchi + mayo + golden_fried_onion + ny_buns_weight
)
print("Seoul Kimchi Burger Weight", seoul_kimchi_burger_weight)
