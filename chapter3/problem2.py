letter = '''
            Dear <|Name|>,
            you are selected,
            <|Date|>.
        '''

newLetter = letter.replace("<|Name|>" , "Afaque Azam").replace("<|Date|>","24 september 2026")

print(newLetter)