# </> The world is our


# Contact Generator is a function made by AfraL to create a .vcf file from a raw text file which contains phone numbers in this format : 06 ** ** ** **
# Don't forget that this script is for educationnal purpose only, you should not use this script for illegal business but for a marketing goal or for educationnal purpose
# We will not be responsible of what you will do with this powerful tool !

import os
import string
import random

def generate_random_strings(chars):
    #try:
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=chars))
    random_string = str(random_string)
        
    #except:
        #print('\nError, cant generate random strings, make sure the script is updated')
        #os.system('exit')
    
    return random_string
    
    
def contact_generator(list, output):
    # Open the plain text file and load all content into memory
    linestring = open(list, 'r').read()
    lines = linestring.split('\n')

    # VCF format

    fmt = """
BEGIN:VCARD
VERSION:2.1
N:;%NOME_COGNOME%;;;
FN:%NOME_COGNOME%
TEL;CELL:%NUM%
END:VCARD
"""

    # Loop onto the contact list to create a single vcf file
    export = ""
    i = 0
    while i < len(lines):
        #print( "linea ", i)
        nome = generate_random_strings(chars=int(10))
        contact = fmt.replace('%NOME_COGNOME%', nome)

        nome = lines[i]
        num = "+33" + nome[1:]
        contact = contact.replace('%NUM%', num)
  
        i += 1
        export += contact

    # File saving
    out_file = open(str(output) + ".vcf", "w")
    out_file.write(export)
    out_file.close()
