import wikipedia
wikipedia.set_lang('uz')


def wiki_bot(test):
    try:
        result = wikipedia.summary(test)
        return result
    except:
        return "Kechirasiz bunday malumot topilmadi"