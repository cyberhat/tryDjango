from django.contrib import admin
from profiles.models import prof

# Register your models here.
class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = prof

admin.site.register(prof, profileAdmin)