from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from campus.core.models import User, Document, AcademicInfo

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'course']
    fieldsets = UserAdmin.fieldsets + (
        ("Academic Information", {'fields': ('course', 'registration_number', 'role')}),
    )
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser and obj != request.user:
            # Remove grupo de permissões
            return [(name, {'fields': [f for f in opts['fields'] if f != 'role']}) for name, opts in fieldsets]
        return fieldsets
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_type', 'status', 'estimated_date', 'requester']
    list_filter = ['doc_type', 'status']
    search_fields = ['requester__username', 'reason']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.requester = request.user
        super().save_model(request, obj, form, change)
@admin.register(AcademicInfo)
class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'status', 'term']
    list_filter = ['term', 'status']
    search_fields = ['user__username', 'subject']
