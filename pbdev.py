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
print beverage


def strong():
  """Find out user preferences and assign to new dictionary"""
  answer = raw_input(questions["strong"]).lower()
  if answer == "yes":
    beverage["strong"] = ingredients["strong"]
  elif answer == "no":
    return False   

def salty():
  answer = raw_input(questions["salty"]).lower()
  if answer == "yes":
    beverage["salty"] = ingredients["salty"]
  elif answer == "no":
    return False

def bitter():  
  answer = raw_input(questions["bitter"]).lower()
  if answer == "yes":
    beverage["bitter"] = ingredients["bitter"]
  elif answer == "no":
    return False

def sweet():  
  answer = raw_input(questions["sweet"]).lower()
  if answer == "yes":
    beverage["sweet"] = ingredients["sweet"]
  elif answer == "no":
    return False
 
def fruity():
  answer = raw_input(questions["fruity"]).lower()
  if answer == "yes":
    beverage["fruity"] = ingredients["fruity"]
  elif answer == "no":
    return False
  
strong()
salty()
bitter()
sweet()
fruity()

cocktail = [random.choice(i) for i in beverage.values()]

print "Yer cocktail is a made with a "
print cocktail

    
    

  



