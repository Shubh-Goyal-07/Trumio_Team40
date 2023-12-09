from django.contrib import admin

# Register your models here.
from .models import Pointers, AudioURL, ImageURL, CreateVideo, AvatarURL, Timeline, FlashCard

class PointersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'pointers', 'topic')

    class Meta:
        model = Pointers
        fields = '__all__'

class AudioURLAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'audio_url')

    class Meta:
        model = AudioURL
        fields = '__all__'

class ImageURLAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'image_url')

    class Meta:
        model = ImageURL
        fields = '__all__'

class AvatarURLAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'avatar_url')

    class Meta:
        model = AvatarURL
        fields = '__all__'

class CreateVideoAdmin(admin.ModelAdmin):
    list_display = ('avatar_url', 'content', 'user_id', 'pointer_id', 'video_url', 'topic')

    class Meta:
        model = CreateVideo
        fields = '__all__'

class TimelineAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'weeks', 'timeline')

    class Meta:
        model = Timeline
        fields = '__all__'

class FlashCardAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'summary', 'image', 'content')

    class Meta:
        model = FlashCard
        fields = '__all__'

admin.site.register(Pointers, PointersAdmin)
admin.site.register(AudioURL, AudioURLAdmin)
admin.site.register(ImageURL, ImageURLAdmin)
admin.site.register(AvatarURL, AvatarURLAdmin)
admin.site.register(CreateVideo, CreateVideoAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(FlashCard, FlashCardAdmin)
