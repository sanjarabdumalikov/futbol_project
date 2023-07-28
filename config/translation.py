translation.config
from modeltranslation.translator import translator, TranslationOptions
from modeltranslation import translation
from futbool.models import Place


class NewsTranslationOptions(TranslationOptions):
    fields = ('task',)

translator.register(Place, NewsTranslationOptions)
