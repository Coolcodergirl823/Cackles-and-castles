import CAC
from CAC import the_first_game
from CAC_overclocked import the_second_game
print("main_menue")
print("what installment of the series do you want to play? ")
game = input(" hard or normal")
if game == "normal":
    the_first_game()
if game == "hard":
    the_second_game()