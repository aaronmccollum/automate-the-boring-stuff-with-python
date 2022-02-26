# Declare variable for item bag with starter stuff
player_bag = {"rope": 1,
              "torch": 6,
              "gold": 42,
              "dagger": 1,
              "arrow": 12}

# Function to display nicely the items in your bag
def display_inventory(bag):
    print("Inventory:")
    item_total = 0
    for k, v in bag.items():
        print(str(v) + " " + str(k))
        item_total += v
        
    print("Total number of items: " + str(item_total))


# Test function call
display_inventory(player_bag)
