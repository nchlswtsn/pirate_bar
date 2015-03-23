import random
questions = {
  "strong": "Do ye like yer drinks strong? ",
  "salty": "Do ye like it with a salty tang? ",
  "bitter": "Are ye a lubber who likes it bitter? ",
  "sweet": "Would ye like a bit of sweetness with yer poison? ",
  "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
  "strong": ["glug of rum", "slug of whiskey", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

beverage = {}


def drink():
  if raw_input(questions["strong"]) == "Yes" or "yes":
    beverage["strong"] = ingredients["strong"]
  elif raw_input(questions["strong"]) == "No" or "no":
    return False  
  beverage["salty"] = raw_input(questions["salty"])
  if questions["salty"] == "Yes" or "yes":
    beverage["salty"] = ingredients["salty"]
  elif questions["salty"] == "No" or "no":
    return False  
  beverage["bitter"] = raw_input(questions["bitter"])
  if questions["bitter"] == "Yes" or "yes":
    beverage["bitter"] = ingredients["bitter"]
  elif questions["salty"] == "No" or "no":
    return False
  beverage["sweet"] = raw_input(questions["sweet"])
  if questions["sweet"] == "Yes" or "yes":
    beverage["sweet"] = ingredients["sweet"]
  elif questions["salty"] == "No" or "no":
    return False
  beverage["fruity"] = raw_input(questions["fruity"])
  if questions["fruity"] == "Yes" or "yes":
    beverage["fruity"] = ingredients["fruity"]
  elif questions["salty"] == "No" or "no":
    return False

drink()

cocktail = [random.choice(i) for i in beverage.values()]

print "Yer cocktail is a made of "
print cocktail

    
    

  



