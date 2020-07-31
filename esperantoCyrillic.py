import keyboard

#Diacritics are formed with ` key and latin key with the exception of ĵ which is formed with the q key

latin = ['b',
         'c',
         'd',
         'f',
         'g',
         'h',
         'i',
         'k',
         'l',
         'm',
         'n',
         'p',
         'r',
         's',
         't',
         'u',
         'v',
         'z']

cyrillic = ['б',
            'ц',
            'д',
            'ф',
            'г',
            'Һ',
            'и',
            'к',
            'л',
            'м',
            'н',
            'п',
            'р',
            'с',
            'т',
            'у',
            'в',
            'з']

lDiacritics = ['` + c',
               '` + g',
               '` + h',
               'q',
               '` + s',
               '` + u']

cDiacritics = ['ч',
               'џ',
               'х',
               'ж',
               'ш',
               'ў',]

keyboard.block_key('`')
keyboard.block_key('q')
for item in latin:
    keyboard.block_key(item)
    keyboard.block_key(item.upper())


while True:
    for l, c in zip(latin, cyrillic):
        if keyboard.is_pressed(l) or keyboard.is_pressed(l.upper()):
            keyboard.write(c)
    for l, c in zip(lDiacritics, cDiacritics):
        if keyboard.is_pressed(l):
            keyboard.write(c)
    
