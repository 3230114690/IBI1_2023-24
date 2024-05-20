def favorite_bond(birth_year):
    bond_actors = {
        "Roger Moore": (1973, 1986),
        "Timothy Dalton": (1987, 1994),
        "Pierce Brosnan": (1995, 2005),
        "Daniel Craig": (2006, 2021)
    }
    for actor, (start, end) in bond_actors.items():
        if start <= birth_year <= end:
            return actor
    return "Unknown"  
# If the birth year doesn't fall within any Bond actor's career
# How to call the function
birth_year=int(input('please enter your birth year:'))
favorite = favorite_bond(birth_year)
print("Favorite James Bond actor:", favorite)
