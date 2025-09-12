# raise Exception("It is failed due to this")
# assert(a != 0)
# try - except - finally block

ItemsInCart = 0

def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"Items in cart: {ItemsInCart}")


# Wrap each call separately to continue execution
for items in [4, -1, 5, 2]:
    try:
        add_to_cart(items)
    except Exception as e:
        print(e)
