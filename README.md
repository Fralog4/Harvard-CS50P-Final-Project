# Pokemon Card finder
#### Video Demo: https://youtu.be/ojHr_lLHDfs

## Description
This code helps to find the missing cards of a specific series within your collection of Pokémon trading cards. To achieve this, I used a function called Missing_Cards, where I compare the cards we have with an array generated on the spot using the arange method from the Numpy library. The value for this array is set as the imaginary total number of cards for that series. The result is the difference between the two arrays, which represents the missing cards.
To respect the standard for this project I divided this program in 3 main sections like:
1)def missing cards in which I filtered my Pandas DataFrame selecting specific rows and columns plus I made a new array to make the difference between new one and the original
2)def read input user;
3)def that prints the results of the operations made in the first def;
4)def main in which I call the original Data Frame that represent my immaginary collection cards
Summary:
This Python script analyzes a Pokémon card collection using pandas and numpy, identifying missing card numbers in a specified series.
Import Libraries: Import the necessary libraries, pandas as pd and numpy as np.
Define Function Missing_cards: This function takes a DataFrame of Pokémon cards (Card_Pokemon), a specific series name (serie), and the total number of cards in a series (num_tot_cards). It filters the DataFrame based on the chosen series, converts the card numbers to numeric values, and then uses numpy's setdiff1d to find the missing card numbers.
Define Function read_input_user: This function prompts the user for input regarding the series name (serie_input) and the total number of cards in the series (num_tot_cards_input), converting the latter to an integer.
Define Function print_result: This function takes the series name (serie) and the result of missing card numbers (risultato) and prints a formatted message indicating the missing card numbers for the specified series.
Define Function main: In this function, a sample DataFrame (Card_Pokemon) is created to represent a Pokémon card collection. The script then prints this collection, prompts the user for input using read_input_user, calls the Missing_cards function, and prints the results using print_result.
Run Main If Script is Executed Directly: The main() function is executed only if the script is run directly (not imported as a module).
## Installation & Use
1. Clone the code.
2. Run the command `pip install -r requirements.txt` in the app directory.
3. Just run the code and if you want you can change your collection dataframe
