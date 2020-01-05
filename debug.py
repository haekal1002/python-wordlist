first_name = 'haekal'
#last_name = 'smith'
#nickname = 'johnny'

last_name = ''
nickname = ''


first_name_up = first_name.title()
last_name_up = last_name.title()
nickname_up = nickname.title()

first_name_rev = first_name[::-1]
last_name_rev = last_name[::-1]
nickname_rev = nickname[::-1]

first_name_rev_up = first_name_up[::-1]
last_name_rev_up = last_name_up[::-1]
nickname_rev_up = nickname_up[::-1]

full_name = [first_name, last_name, nickname,
             first_name_up, last_name_up, nickname_up,
             first_name_rev, last_name_rev, nickname_rev,
             first_name_rev_up, last_name_rev_up, nickname_rev_up]

comb_name = []
for name1 in full_name:
    for name2 in full_name:
        print('name1: {}\tname2: {}'.format(name1, name2), end='')
        special = name2[:-1]+name2[-1].upper() if len(name2)>0 else ''
        conditions = (name2[::-1].lower(), name2[::-1],
                      name2.lower()      , name2[::-1].title(),
                      special            , name2.lower()[::-1],
                      name2.title()      , name2.title()[::-1],
                      name2)

        if name1 not in conditions:
            comb_name.append(name1+name2)
            print('\tPASSED', end='')
        print()

print('length: ', str(len(comb_name)))
print(set(comb_name))
