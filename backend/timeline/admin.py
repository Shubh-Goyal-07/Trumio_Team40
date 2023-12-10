from django.contrib import admin

# Register your models here.
from .models import Timeline

class TimelineAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'weeks', 'timeline')

    class Meta:
        model = Timeline
        fields = '__all__'

admin.site.register(Timeline, TimelineAdmin)