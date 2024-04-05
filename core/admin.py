from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Profile ,Post,LikePost

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
# admin.site.register(FollowersCount)