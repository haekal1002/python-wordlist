import os

def data_stitch(array1, array2, character):
    for data1 in array1:
        for data2 in array2:
            yield data1 + character + data2

def convert2leet(word):
    # diciontary
    leet_dict = {'a' : '4', 'e' : '3', 'g' : '6', 
                 'i' : '1', 'o' : '0', 's' : '5', 
                 't' : '7'}
    leet_word = ''
    for letter in word:
        try:
            leet_word += leet_dict[letter.lower()]
        except:
            leet_word += letter
    
    return leet_word

def save_to_file(name, array_data, mode_option):
    print()
    if mode_option:
        data_leeted = [convert2leet(data) for data in array_data]
        array_data += data_leeted
        print('[+] Adding leet data to dictionary.')

    array_data = sorted(set(array_data))
    print('[+] Sorting and deleting the same data.')

    f = open(name, 'w')
    f.write(os.linesep.join(array_data))
    f.close()

    print('[+] Saving dictionary as {}'.format(name))
    print('[+] Counting {} words.'.format(len(array_data)))

def word_gen(data):
    # ---------- for birthdate ----------
    birthdate_yy = data['birthdate'][-2:]
    birthdate_yyy = data['birthdate'][-3:]
    birthdate_dd = data['birthdate'][:2]
    birthdate_mm = data['birthdate'][2:4]
    
    full_birthdate = [birthdate_yy, birthdate_yyy, birthdate_dd, birthdate_mm]
    comb_birthdate = []

    # dates could be same. so this iterates through all combination,
    # then deletes the same entry
    for bd1 in full_birthdate:
        for bd2 in full_birthdate:
            comb_birthdate.append(bd1+bd2)
            for bd3 in full_birthdate: 
                comb_birthdate.append(bd1+bd2+bd3)
    
    comb_birthdate = list(set(comb_birthdate))
    rev_comb_birthdate = [date[::-1]  for date in comb_birthdate]
    comb_birthdate += rev_comb_birthdate

    # ---------- for first_name, last_name, nickname ----------
    first_name = data['first_name']
    last_name = data['last_name']
    nickname = data['nickname']

    first_name_up = data['first_name'].title()
    last_name_up = data['last_name'].title()
    nickname_up = data['nickname'].title()

    first_name_rev = data['first_name'][::-1]
    last_name_rev = data['last_name'][::-1]
    nickname_rev = data['nickname'][::-1]

    first_name_rev_up = data['first_name'].title()[::-1]
    last_name_rev_up = data['last_name'].title()[::-1]
    nickname_rev_up = data['nickname'].title()[::-1]
    
    full_name = [first_name, last_name, nickname,
                 first_name_up, last_name_up, nickname_up,
                 first_name_rev, last_name_rev, nickname_rev,
                 first_name_rev_up, last_name_rev_up, nickname_rev_up]

    comb_name = []
    for name1 in full_name:
        for name2 in full_name:
            special = name2[:-1]+name2[-1].upper() if len(name2)>0 else ''
            conditions = (name2[::-1].lower(), name2[::-1], name2 ,
                          name2.lower()      , name2[::-1].title(),
                          special            , name2.lower()[::-1],
                          name2.title()      , name2.title()[::-1],)
            if name1 not in conditions:
                comb_name.append(name1+name2)
    
    comb_name += full_name

    # ----------- for pet's name, fav band, extra word ----------
    pets_name = data['pets_name']
    fav_band = data['fav_band']
    extra_word = data['extra_word']
    
    pets_name_up = pets_name.title()
    fav_band_up = fav_band.title()
    extra_word_up = [word.title() for word in extra_word]
    
    comb_word = [pets_name, fav_band, pets_name_up, fav_band_up]
    comb_word += extra_word
    comb_word += extra_word_up
    
    # ---------- Stores values ----------
    combination = []
    combination += comb_birthdate
    combination += list(data_stitch(comb_name, comb_birthdate, '_')) 
    combination += list(data_stitch(comb_name, comb_birthdate, '')) 
    combination += list(data_stitch(comb_word, comb_birthdate, '_')) 
    combination += list(data_stitch(comb_word, comb_birthdate, '')) 
    
    save_to_file(first_name+'.txt', combination, data['leet_mode'])

def main():
    first_name = input('> First Name: ').lower()
    while first_name == '':
        print('[-] At least put a name!')
        first_name = input('> First Name: ').lower()

    last_name  = input('> Last Name: ').lower()
    nickname   = input('> Nickname: ').lower()
    
    birthdate  = input('\n> Birthdate (DDMMYYYY): ')
    while (len(birthdate) != 8) and (len(birthdate) != 0):
        print('[-] Birthdate length should be 8 characters.')
        birthdate  = input('> Birthdate (DDMMYYYY): ')

    pets_name  = input('> Pet\'s Name: ').lower()
    fav_band   = input('> Favorite Band: ').lower()
    extra_word  = input('\n> Would you like to add extra key word? Y/N: ').lower()
    
    if extra_word == 'y':
        extra_word = input('    Insert words separated by coma. (i.e fish,globe,chicken): ')
        extra_word = [word.lower() for word in extra_word.split(',')]
    else:
        extra_word = ''

    leet_mode = input('> Leet mode? Y/N: ').lower()
    if leet_mode == 'y':
        leet_mode = True
    else:
        leet_mode = False

    data = {'first_name' : first_name, 'last_name' : last_name, 
            'nickname'   : nickname,   'birthdate' : birthdate, 
            'pets_name'  : pets_name,  'fav_band'  : fav_band, 
            'extra_word'  : extra_word, 'leet_mode': leet_mode}

    word_gen(data)

main()
