'''
Tip calculator
'''


def tip_calculator():
    print('This is your friendly tip calculator to help you when you may be stuck in a rut!')

    #final price
    f_price = float(input('What was the final bill tally?\n$'))
    

    #total people
    t_people = float(input('How many are splitting the bill?\n'))

    #tip percent
    t_percent = float(input('What % of a tip shall we leave? (Number value excluding %)\n')) / 100

    #calculate the final results to the 2 decimal place
    final = '{:.2f}'.format(f_price * t_percent / t_people)

    print(f'It is ideal to pay ${final} each.')


tip_calculator()