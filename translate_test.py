# from googletrans import Translator

# translator = Translator()

# print(translator.detect("hey how are you doing"))


# print(translator.translate("hey how are you doing", dest='pl'))

# translator = Translator(service_urls=['translate.googleapis.com'])
# translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')

# import translators as ts
# phrase = ts.google('Trudno powiedzieć, większość moich części jest z Chin' , to_language = 'en')


from langdetect import detect_langs, detect
print(detect_langs('hej'))
print(detect('hej'))



