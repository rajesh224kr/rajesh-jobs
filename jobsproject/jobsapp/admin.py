from django.contrib import admin
from jobsapp.models import Hydjobsinfo,Delhijobsinfo,Punejobsinfo,Noidajobsinfo
# Register your models here.
class HydjobsinfoAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','PhoneNumber']

class DelhijobsinfoAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','PhoneNumber']

class PunejobsinfoAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','PhoneNumber']

class NoidajobsinfoAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','PhoneNumber']

admin.site.register( Hydjobsinfo,HydjobsinfoAdmin)
admin.site.register(Delhijobsinfo,DelhijobsinfoAdmin)
admin.site.register(Punejobsinfo,PunejobsinfoAdmin)
admin.site.register(Noidajobsinfo,NoidajobsinfoAdmin)