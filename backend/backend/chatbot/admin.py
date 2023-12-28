from django.contrib import admin

# Register your models here.
from .models import ProjectSession, ChatSession

class ProjectSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'project_link', 'user_id')
    
    class Meta:
        model = ProjectSession
        fields = '__all__'

class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'user_id', 'question')
    
    class Meta:
        model = ChatSession
        fields = '__all__'

admin.site.register(ProjectSession, ProjectSessionAdmin)
admin.site.register(ChatSession, ChatSessionAdmin)