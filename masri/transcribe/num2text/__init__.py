from . import lang_MT

def num2text(number, lang='mt', to='cardinal', **kwargs):
    converter = lang_MT.Num2Word_MT()
    number = str(number)
    number = number.replace(",", "")
    number = converter.str_to_number(number)

    return getattr(converter, 'to_{}'.format(to))(number, **kwargs)

