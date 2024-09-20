from django.contrib import admin
from .models import Profile,Certification,Education,Project,WorkExperience
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)