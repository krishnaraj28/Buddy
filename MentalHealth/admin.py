from django.contrib import admin
from .models import CustomUser,Profile,Event,Like,Resource,Appointment

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Resource)
admin.site.register(Like)
admin.site.register(Appointment)


# Register your models here.
