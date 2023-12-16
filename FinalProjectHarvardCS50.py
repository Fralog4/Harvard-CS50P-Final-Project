import pandas as pd
import numpy as np
def Missing_cards(Card_Pokemon, serie, num_tot_cards):
    # Filter for the series names
    serie_choosen = Card_Pokemon[Card_Pokemon['Nome_Serie'] == serie] #I manually selected the table I need
    serie_choosen.loc[:, 'Numero_Carta'] = pd.to_numeric(serie_choosen['Numero_Carta'])
    #I used .loc method for label-based indexing,this allow you to select data from a DataFrame using labels
    #Create an array to find which numbers miss
    #setdiff1d finds the differences between two array so we need to create a new array with arange to make the confront
    missing_numbers = np.setdiff1d(np.arange(1, num_tot_cards+1),
                                   serie_choosen['Numero_Carta'].unique())
    return list(missing_numbers)    #this is the value of missing number cards

def read_input_user():
    serie_input = input('Serie?: ')
    num_tot_cards_input = int(input('Numero carte?: '))
    return serie_input, num_tot_cards_input

def print_result(serie, risultato):
    print(f'Numeri mancanti per la serie {serie}: {risultato}')

def main():
    Card_Pokemon = pd.DataFrame({
        'Nome_Serie': ['Cerchio', 'Diamante', 'Stella', 'Cerchio', 'Cerchio', 'Stella'],
        'Numero_Carta': ['3', '47', '5', '45', '32', '4'],
        'Valutazione': ['85.00', '15.00', '8.00', '12.00', '13.00', '12.00'],
        'Numero_di_copie_posseduto': ['1', '3', '2', '2', '3', '1']
    })
#All the value are in italian because is an italian stock of cards
    print(Card_Pokemon)    #I print because I want to see my collection

    serie, num_tot_cards = read_input_user()
    result = Missing_cards(Card_Pokemon, serie, num_tot_cards)
    print_result(serie, result)

if __name__ == "__main__":
    main()
