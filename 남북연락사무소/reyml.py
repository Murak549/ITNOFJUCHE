with open('NKBK_state_names_l_english.yml', 'r', encoding='UTF8') as file:
    lines = file.readlines()

with open('NKBK_state_names_l_english.yml', 'w', encoding='UTF8') as file:
    for line in lines:
        if line.startswith(' STATE_'):
            state_number = int(line.split(':')[0].split('_')[1])
            if state_number >= 909:
                line = ' STATE_' + str(state_number + 26) + line.split(':')[1]
        file.write(line)
