from django.contrib import admin
from .models import Event, NavLink , Exhibition_Entry

from django.utils.safestring import mark_safe


class NavlinkAdmin(admin.TabularInline):
    model = NavLink

class EventAdmin(admin.ModelAdmin):
   inlines = [NavlinkAdmin,]

admin.site.register(Event , EventAdmin)

class ExhibitionWallAdmin(admin.ModelAdmin):
    list_display =  (
        'title',
        'username',
        'front_view_preview',
        'category',
        'is_Verified'
    )

    readonly_fields = ('front_view_preview',)

    def front_view_preview(self, obj):
     return obj.front_view_preview

    front_view_preview.short_description = 'Banner Preview'
    front_view_preview.allow_tags = True
    
admin.site.register(Exhibition_Entry, ExhibitionWallAdmin)  