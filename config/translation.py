translation.config
from modeltranslation.translator import translator, TranslationOptions
from futbool.models import Place

class NewsTranslationOptions(TranslationOptions):
    fields = ('task',)

translator.register(Place, NewsTranslationOptions)
