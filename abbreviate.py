abbr = {'the': '', 'and': '', 'of': '', 'in': '', 'on': '',
        '\&': '', 'series': ''}

with open('codings.txt') as f:
    for line in f:
        splt = line.strip().split(',')
        abbr[splt[0]] = splt[1]

acronyms = {'Plos': 'PLoS', 'Jama': 'JAMA', 'Bmc': 'BMC', 'Nmr': 'NMR',
            'Bmj': 'BMJ', 'Ieee': 'IEEE', 'Bba': 'BBA', 'Pm\&r': 'PMR'}

new_ref = []

with open('references.bib') as f:
    for line in f:
        if 'journal' in line:
            brackets = line[line.find('{')+1:line.find('}')]
            words = [x.lower().strip(':,') for x in brackets.split(' ')]
            if len(words) == 1:
                new_j = words
            else:
                new_j = [abbr.get(word, word) for word in words]
                new_j = filter(None, new_j)
            new_j = [word.capitalize() for word in new_j]
            new_j = [acronyms.get(word.strip(), word) for word in new_j]
            new_j = ' '.join(new_j)
            new_j = new_j.replace('\'', '')
            new_j = new_j.replace(' (methodological)', '')
            # print(new_j)
            new_line = '  journal={' + new_j + '},\n'
            new_ref.append(new_line)
        else:
            new_ref.append(line)

with open('references_abbr.bib', 'w+') as f:
    f.write(''.join(new_ref))

