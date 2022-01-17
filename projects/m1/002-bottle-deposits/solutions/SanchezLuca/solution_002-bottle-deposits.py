print('--Hello! Please insert below the number of the bottle for each size for calculate your refund.--')

small = int(input ('Number of bottles up to 1L included --> '))
big = int(input ('Number of bottles above 1L --> '))

deposit_small = (small * 0.1)
deposit_big = (big * 0.25)
tot_deposit = (deposit_small + deposit_big)

print('The ammount of your refund is -->',tot_deposit,'$')