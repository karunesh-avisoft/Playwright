def test_inventory(inventory_page):    
    # further inventory page tests added here    
    inventory_page.open_burger_menu()
    
    inventory_page.close_burger_menu()
    
    inventory_page.verify_products()
    # sorting products
    inventory_page.apply_sort('az')
    inventory_page.apply_sort('za')
    inventory_page.apply_sort('lohi')       
    inventory_page.apply_sort('hilo')
    
    inventory_page.add_to_cart()
    inventory_page.remove_from_cart()
    
    inventory_page.open_cart()