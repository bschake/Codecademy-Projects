#python3 script.py
from utils import print_message, get_size, order_latte, order_mocha, exit

exit_phrase = ["stop", "bye", "exit"]

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = "y"
  drinks = []
  yes_list = ['y', 'sure', 'yes please', 'affirmative', 'yes', 'yeah']
  while order_drink in yes_list:
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)

    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(str(drink))

    while True:
      order_drink = input("Would you like to order another drink? (y/n) \n>")
      if order_drink in exit_phrase:
        return exit()
      if order_drink in yes_list or ["y", "n", "no", "nah", "no thanks"]:
        break
  print("Okay, so I have:")
  for item in drinks:
    print(" - " + item)
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n[d] London Fog \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  elif res == 'd':
    return 'London Fog'
  elif res in exit_phrase:
    pass
  else:
    print_message()
    return get_drink_type()
  
# Define new functions here!


coffee_bot()
