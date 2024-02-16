from modeltranslation.translator import translator, TranslationOptions
from .import models as product_models

class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(product_models.Item, ProductTranslationOptions)