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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.role == 'coordinator':
            return qs
        return qs.filter(id=request.user.id)

    def has_change_permission(self, request, obj=None):
        # Allow superuser or coordinator to edit anyone
        if request.user.is_superuser or request.user.role == 'coordinator':
            return True
        # Allow regular user to edit only their own profile
        if obj is not None and obj.id != request.user.id:
            return False
        return True

    def has_view_permission(self, request, obj=None):
        # Same logic as above
        if request.user.is_superuser or request.user.role == 'coordinator':
            return True
        if obj is not None and obj.id != request.user.id:
            return False
        return True

    def get_readonly_fields(self, request, obj=None):
        # Prevent normal users from changing their own role or other sensitive fields
        if request.user.is_superuser or request.user.role == 'coordinator':
            return super().get_readonly_fields(request, obj)
        return super().get_readonly_fields(request, obj) + ('role', 'is_superuser', 'is_staff', 'user_permissions', 'groups')

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
