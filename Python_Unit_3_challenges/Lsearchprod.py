def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices
product_list = []
product_list = [item for item in input("Enter the list products : ").split()]
print(product_list)
target_product = input("Enter the target_product Name :")
result = linear_search_product(product_list, target_product)
print(result)  
