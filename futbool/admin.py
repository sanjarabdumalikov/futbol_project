from django.contrib import admin
from .forms import FootballForms
from .models import Place,Booking
class FootballAdmin(admin.ModelAdmin):
    form = FootballForms
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Booking)
admin.site.register(Place)
