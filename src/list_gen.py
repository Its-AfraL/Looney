import string


def generate_num_list(indicatifs, list_name):

    with open(list_name, 'w') as l:
        indicatifs = indicatifs.split(',')
        for indicatif in indicatifs:
            # 01 : Region parisienne
            # 02 : Region nord-ouest / Ocean Indien
            # 03 : Region nord-est
            # 04 : Region sud-est
            # 05 : Region sud-ouest / Ocean Atlantique
            # 09 : Box internet
            # 06/07 : Mobiles
            # 08 : Tarification speciale
            n = 1
            # range trop grand pour un for, on utilise while.
            while n < 100000000:
                l.write(indicatif + (8 - len(str(n))) * "0" + str(n) + "\n")
                n += 1
