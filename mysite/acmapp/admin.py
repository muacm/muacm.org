from django.contrib import admin
from acmapp.models import (
    Event,
    Project,
    TeamMember,
    Blog
)
# Register your models here.

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Blog)
