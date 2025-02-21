from django.contrib import admin
from .models import Swimmer, SwimStroke, SwimMeet, SwimStrokeSkills, SkillLevel

admin.site.register(Swimmer)
admin.site.register(SwimStroke)
admin.site.register(SwimMeet)
admin.site.register(SwimStrokeSkills)
admin.site.register(SkillLevel)

