from django.contrib import admin
from app.models import State, City, Hospital, Facility, Availability

# Register your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal , instance , **kwaegs):
    facilities = Facility.objects.all()
    for facility in facilities:
     availability =  Availability(hospital=instance , facility = facility)
    availability.save()

@receiver(post_save, sender=Facility)
def afterFacilitySave(signal , instance , **kwaegs):
    hospitals = Hospital.objects.all()
    for hospital in hospitals:
     availability =  Availability(hospital=hospital , facility = instance)
    availability.save()    

class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display=['title']


    # def oxygen_beds(self , object):
    #     return f'{object.oxygen_beds_available}/{object.oxygen_beds_total}'  

    # def oxygen_cylinder(self , object):
    #     return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'              
                
    # def ventilator(self , object):
    #     return f'{object.ventilator_available}/{object.ventilator_total}'  


class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name', 'phone', 'address']


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name', 'state']   

class AvailabilityAdmin(admin.ModelAdmin):
    model = Availability
    list_display = ['hospital', 'facility', 'total', 'available'  ,'updated_at']  
    list_editable= ['total', 'available']



admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility , FacilityAdmin)
admin.site.register(Availability , AvailabilityAdmin)
