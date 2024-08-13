# Write code below 💖
# So Random 🧙‍♂️

import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
  return name.capitalize()

capped_suffixes = list(map(capitalize_suffix, suffixes))
#print (capped_suffixes)

def create_fantasy_name(lis11, list2):
  return random.choice(lis11) + ' ' + random.choice(list2)

#num_names = 10
fantasy_names = [create_fantasy_name(prefixes, capped_suffixes) for name in range(10)]

def fire_in_name(name):
  return "Fire" in name
filtered_names = list(filter(fire_in_name, fantasy_names))

#print (filtered_names)

def concatenate_names(acc, name):
  return acc + ',' + name

reduced_names = reduce(concatenate_names, filtered_names )
#print (reduced_names)

def display_info():
  print("Fantasy Names:")
  for name in fantasy_names:
      print(name)
      #print (type(fantasy_names))
      print()
  print('Filtered names with \'Fire\':', list(filtered_names))
  print('Concatenated names:', reduced_names)

display_info()