from django.contrib import admin

from social.models import Hashtag, Profile, Post

admin.site.register(Hashtag)
admin.site.register(Post)
admin.site.register(Profile)
