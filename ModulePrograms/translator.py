from translate import Translator
#help(translate)
#help(translate.Translator)
trans1 = Translator(to_lang = 'bn')
eng_text = input('Enter text to be translated ')
translated_text = trans1.translate(text = eng_text)
print(translated_text)