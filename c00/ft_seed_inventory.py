def ft_seed_inventory(name: str , number_of_seed: int , type : str):
    if type.__eq__("packets"):
        print(f"{name} seeds : {number_of_seed} {type} available ")
    elif type.__eq__("grams"):
        print(f"{name} seeds : {number_of_seed} {type} total ")
    elif type.__eq__("area"):
        print(f"{name} seeds : {number_of_seed} {type} meters ")
    else:
        print("type dont exist")