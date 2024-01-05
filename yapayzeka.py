
from deep_translator import GoogleTranslator
import google.generativeai as palm

API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
palm.configure(api_key=API_KEY)
def mesajlas(mesaj):
    turkish_text = mesaj
    translated_en = GoogleTranslator(source='auto', target='en').translate(turkish_text)
    response = palm.chat(messages=translated_en, temperature=0.2, context='Speak like a CEO')
    response = response.reply(translated_en)
    ceviri_response = GoogleTranslator(source='auto', target='tr').translate(response.last)
    return ceviri_response
          
        
         
        



