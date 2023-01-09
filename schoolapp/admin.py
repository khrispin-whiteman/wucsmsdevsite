from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from schoolapp.models import Semester, Course, Session, Level, User, School, Program, Department, ProgramType, Student, \
    Admission, StudentNumber, SystemSettings


# Register your models here.
# class TheUserAdmin(UserAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'phone', 'address', 'email', 'is_student', 'is_lecturer', 'is_admissions_officer', 'is_accounts_officer', 'is_dean_of_students_officer', 'is_ict_officer', 'is_registrars_officer', 'is_pg_coordinators_officer')
#     list_display_links = ('first_name', 'last_name', 'phone', 'address', 'email', 'is_student', 'is_lecturer',  'is_admissions_officer', 'is_accounts_officer', 'is_dean_of_students_officer', 'is_ict_officer', 'is_registrars_officer', 'is_pg_coordinators_officer' )
#     list_per_page = 10
#     search_fields = ('first_name', 'last_name', 'phone', 'address', 'email', 'is_student', 'is_lecturer', 'is_librarian', 'is_parent', )
class TheUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'is_student', 'is_member_of_staff', 'user_group')
    list_display_links = ('first_name', 'last_name', 'phone', 'email', 'is_student', 'is_member_of_staff', 'user_group')
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'phone', 'address', 'email', 'user_group')
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (  # new fieldset added on to the bottom
            'More Fields',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'phone',
                    'is_student',
                    'is_member_of_staff',
                    'user_group',
                ),
            },
        ),
    )


class SemesterAdmin(ImportExportModelAdmin):
    list_display = ('semester', 'session', 'is_current_semester', 'next_semester_begins')
    search_fields = ('semester', 'session')
    list_per_page = 10


class SessionAdmin(ImportExportModelAdmin):
    list_display = ('session', 'is_current_session', 'next_session_begins')
    search_fields = ('session', )
    list_per_page = 10


class CourseAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = ('course_name', 'course_code', 'course_program', 'course_description', 'level', 'semester')
    search_fields = ('course_name', 'course_code', 'level')


class SchoolAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = ('school_name', 'school_description')
    search_fields = ('school_name', 'school_description')


class ProgramAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = ('program_name', 'program_description')
    search_fields = ('program_name', 'program_description')


class DepartmentAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_display = ('department_name', 'hod', 'department_description')
    search_fields = ('department_name', 'hod', 'department_description')


class LevelAdmin(ImportExportModelAdmin):
    list_display = ('level',)
    list_display_links = ('level',)
    list_per_page = 10
    search_fields = ('level',)


class ProgramTypeAdmin(ImportExportModelAdmin):
    list_display = ('pg_type_name', 'pg_type_description')
    list_display_links = ('pg_type_name', 'pg_type_description')
    list_per_page = 10
    search_fields = ('pg_type_name', 'pg_type_description')


class StudentNumberAdmin(ImportExportModelAdmin):
    list_display = ('full_student_no',)
    list_display_links = ('full_student_no',)
    list_per_page = 10
    search_fields = ('full_student_no',)


class SystemSettingsAdmin(ImportExportModelAdmin):
    list_display = ('student_no_last_digits_length',)
    list_display_links = ('student_no_last_digits_length',)
    list_per_page = 10
    search_fields = ('student_no_last_digits_length',)


class StudentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'student_number', 'program', 'admission_date', 'level')
    list_display_links = ('id', 'user', 'student_number', 'program', 'admission_date', 'level')
    list_per_page = 10
    search_fields = ('user', 'student_number', 'program', 'admission_date', 'level')
    autocomplete_fields = ('user', 'program')


class AdmissionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'nrc_no', 'phone_number', 'email', 'gender', 'program_applied_for')
    list_display_links = ('id', 'first_name', 'last_name', 'nrc_no', 'phone_number', 'email', 'gender', 'program_applied_for')
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'nrc_no', 'phone_number', 'email', 'gender', 'program_applied_for')


admin.site.register(Session, SessionAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(User, TheUserAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(ProgramType, ProgramTypeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(StudentNumber, StudentNumberAdmin)
admin.site.register(SystemSettings, SystemSettingsAdmin)