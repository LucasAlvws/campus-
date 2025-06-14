from datetime import date, timedelta

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from campus.core.models import AcademicInfo, Course, Document, User


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
        if request.user.is_superuser or request.user.role == 'coordinator':
            return True
        if obj is not None and obj.id != request.user.id:
            return False
        return True

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'coordinator':
            return True
        if obj is not None and obj.id != request.user.id:
            return False
        return True

    def get_readonly_fields(self, request, obj=None):
        base_readonly = super().get_readonly_fields(request, obj)

        if request.user.is_superuser or request.user.role == 'coordinator':
            return base_readonly

        academic_fields = (
            'course',
            'registration_number',
            'role',
            'is_superuser',
            'is_staff',
            'user_permissions',
            'groups',
        )
        return base_readonly + academic_fields


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_type', 'status', 'estimated_date', 'requester']
    list_filter = ['doc_type', 'status']
    search_fields = ['requester__username', 'reason']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.requester = request.user
        super().save_model(request, obj, form, change)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.requester = request.user
            obj.estimated_date = date.today() + timedelta(days=5)
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        # Ensure requester can't be changed manually
        readonly = super().get_readonly_fields(request, obj)
        return readonly + ('requester',)
@admin.register(AcademicInfo)
class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'status', 'term']
    list_filter = ['term', 'status']
    search_fields = ['user__username', 'subject']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    ordering = ('name',)
