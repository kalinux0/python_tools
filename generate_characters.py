import sys
import random

character_lists = {
    #1 bytes
    0:"0123456789",
    #2 bytes
    1:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    #1 or 2 bytes
    2:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    #1 or 2 bytes with special chars
    3:"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,*/-+$#[]{}();:@€£><%+&=?"
}

character_len = 15
character_type = 3

arguments = sys.argv
argument_count = len(arguments)

if argument_count>=2:
    if str(arguments[1]) == 'help':
        print('Default character count:',character_len,
              'Default character type:',str(character_lists[character_type]),
              'Character count:','1-∞',
              'Character types:',character_lists,
              sep="\n")
        sys.exit(1)
        
    character_len = int(arguments[1])
    
    if argument_count==3:
        character_type = int(arguments[2])

array_len = range(character_len)
character_list = character_lists[character_type]
result = ''
for i in array_len:
    result+= random.choice(character_list)

print(result)

    
