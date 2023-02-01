from spellchecker import SpellChecker
import re

spell = SpellChecker()

# misspelled = spell.unknown(['candideete'])

# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))

#     # Get a list of `likely` options
#     print(spell.candidates(word))

sen = "hyy i am lookieng for job plece"
print(sen)

def spell_checker(sen):
    spliting_word = re.split(r"[^a-zA-Z0-9_]", sen)
    misspelled = spell.unknown(spliting_word)

    for word in misspelled:
        if spell.correction(word):
            new_word = spell.correction(word)
            sen = sen.replace(word, new_word)
            
    
    return sen

sen1 = spell_checker(sen)

print(sen1)


# spell.word_frequency.load_words(['microsoft', 'apple', 'google'])
# spell.known(['microsoft', 'google'])  # will return both now!


# english = SpellChecker()  # the default is English (language='en')
# spanish = SpellChecker(language='es')  # use the Spanish Dictionary
# russian = SpellChecker(language='ru')  # use the Russian Dictionary
# arabic = SpellChecker(language='ar')   # use the Arabic Dictionary