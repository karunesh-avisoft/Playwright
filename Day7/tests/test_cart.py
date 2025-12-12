def test_cart_page(add_items_to_cart:InventoryPage, page:Page):
    """Test to verify cart page opens and displays correct items"""
    inventory_page = add_items_to_cart
    inventory_page.open_cart()
    
    from pages.cart_page import CartPage
    cart_page = CartPage(page)
    cart_page.verify_open()
    
    # Verify correct number of items in cart
    cart_items = cart_page.cart_items.count()
    assert cart_items == inventory_page.cart_count, f"Expected {inventory_page.cart_count} items in cart, found {cart_items}"