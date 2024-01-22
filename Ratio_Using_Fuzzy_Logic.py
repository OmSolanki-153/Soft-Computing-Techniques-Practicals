# Practical 8A: Find the ratios using fuzzy logic
# Practical performed by Roll No: 04, Om Solanki

from fuzzywuzzy import fuzz

Str_A = 'Fuzzywuzzy is a lifesaver!'
Str_B = 'fuzzy wuzzy is a LIFE SAVER.'
ratio = fuzz.ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))

Str_A = 'Chicago Illinois'
Str_B = 'chicago'
ratio = fuzz.partial_ratio(Str_A.lower(), Str_B.lower())
print('partial_ratio: {}'.format(ratio))

Str_A = 'Gunner William kline'
Str_B = 'Kline, Gunner William'
ratio = fuzz.token_sort_ratio(Str_A, Str_B)
print('token_sort_ratio: {}'.format(ratio))

Str_A = 'The 300 meter steeplechase winner, Soufiane El Bakkali'
Str_B = 'Soufiane El Bakkali'
ratio = fuzz.token_set_ratio(Str_A, Str_B)
print('token_set_ratio: {}'.format(ratio))
