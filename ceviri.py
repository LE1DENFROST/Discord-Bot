from deep_translator import GoogleTranslator


def cevir(mesaj):
    turkish_text = mesaj
    translated_en = GoogleTranslator(source='auto', target='en').translate(turkish_text)
    return translated_en

def cevirtr(mesaj):
    turkish_text = mesaj
    translated_tr = GoogleTranslator(source='auto', target='tr').translate(turkish_text)
    return translated_tr