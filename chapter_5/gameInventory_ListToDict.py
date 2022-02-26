# Declare variable for item bag with starter stuff
player_bag = {"rope": 1,
              "gold": 42}

# Function to display nicely the items in your bag
def display_inventory(bag):
    print("Inventory:")
    item_total = 0
    for k, v in bag.items():
        print(str(v) + " " + str(k))
        item_total += v
        
    print("Total number of items: " + str(item_total))


# Function to add loot to bag after a monster kill
dragon_loot = ["gold", "dagger", "gold", "gold", "ruby"]

def add_to_inventory(bag, new_loot):
    # Create a list of keys from bag dictionary
    bag_keys = list(bag.keys())

    # Iterate through each item in monster loot, add to bag dictionary value if there, add new value if not and start at 1
    for item in new_loot:
        if (item in bag_keys):
            bag[item] += 1
        else:
            bag[item] = 1


# Test function call
display_inventory(player_bag)
add_to_inventory(player_bag, dragon_loot)
print("-------\nPlayer Kills Dragon\n-------")
display_inventory(player_bag)
