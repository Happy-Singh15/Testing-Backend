import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Exercise

@register(Exercise)
class ProductIndex(AlgoliaIndex):
    fields = ('title', 'bodypart', 'level')   # fields to be indexed
    settings = {'searchableAttributes': ['bodypart']}
    index_name = 'exercise_index'
