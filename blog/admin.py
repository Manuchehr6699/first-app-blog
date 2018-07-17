from django.contrib import admin
from .models import Post
from .models import Profile


admin.site.register(Post)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)