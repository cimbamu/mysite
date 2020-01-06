from django.contrib import admin
admin.site.site_header = 'Machine Learing'

from.models import Article
admin.site.register(Article)
