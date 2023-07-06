from django.contrib import admin
from .models import Profile

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         'id',
#         'pkid',
#         'user',
#         'first_name',
#         'last_name',
#         'email',
#         'date_joined',
#         'gender',
#         'profile_photo',
#         'role',
#         'description',
#         ]
#     list_filter = ['gender', 'is_active', 'is_staff']
#     list_display_links = [
#         'id',
#         'pkid',
#         'user',
#         ]
#     # fieldsets zobaczyc co mozna zmienic w widoku admina tutaj

admin.site.register(Profile)