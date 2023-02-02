from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from schoolapp.models import Semester, Course, Session, Level, User, School, Program, Department, ProgramType, Student, \
    Admission, StudentNumber, SystemSettings, Payment, PaymentType, PaymentStructure, TakenCourse, Result


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
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'user_group')
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
    list_display = ('program_name', 'program_code', 'program_duration', 'program_type', 'program_coordinator', 'program_school', 'program_description')
    list_per_page = 10
    search_fields = ('program_name', 'program_code', 'program_duration', 'program_description')
    autocomplete_fields = ('program_type', 'program_coordinator', 'program_school')
    list_filter = ('program_type', 'program_duration', 'program_school')


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
    list_display = ('id', 'user', 'student_admission_details', 'level')
    list_display_links = ('id', 'user', 'student_admission_details', 'level')
    list_per_page = 10
    search_fields = ('user', 'student_admission_details__student_number', 'level')
    autocomplete_fields = ('user', 'student_admission_details', )
    date_hierarchy = 'student_registration_date'


class AdmissionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'nrc_no', 'phone_number', 'email', 'gender', 'program_applied_for')
    list_display_links = ('id', 'first_name', 'last_name', 'nrc_no', 'phone_number', 'email', 'gender', 'program_applied_for')
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'nrc_no', 'phone_number', 'student_number__full_student_no', 'email', 'gender', 'program_applied_for__program_name')


#  accounts modules
class PaymentTypeAdmin(ImportExportModelAdmin):
    list_display = ('payment_type_name',)
    list_display_links = ('payment_type_name',)
    list_per_page = 10
    search_fields = ('payment_type_name',)


class PaymentStructureAdmin(ImportExportModelAdmin):
    list_display = ('payment_level', 'amount_to_be_paid', 'payment_description')
    list_display_links = ('payment_level', 'amount_to_be_paid', 'payment_description')
    list_per_page = 10
    search_fields = ('payment_level__level', 'amount_to_be_paid', 'payment_description__payment_type_name',)


class PaymentAdmin(ImportExportModelAdmin):
    list_display = ('student', 'amountpaid', 'actualamountpaid', 'paymentstructure', 'balance', 'total_amount_to_be_paid', 'semester', 'paymentstatus', 'paymentdate')
    list_display_links = ('student', 'amountpaid', 'actualamountpaid', 'paymentstructure', 'balance', 'total_amount_to_be_paid', 'semester', 'paymentstatus', 'paymentdate')
    list_per_page = 10
    search_fields = ('student__user__username', 'amountpaid', 'actualamountpaid', 'paymentstructure__amount_to_be_paid', 'balance', 'total_amount_to_be_paid', 'paymentstatus', 'paymentdate')
    date_hierarchy = 'paymentdate'
    list_filter = ('semester', )


class TakenCourseAdmin(ImportExportModelAdmin):
    list_display = ('student', 'semester', 'course', 'ca', 'ca2', 'exam', 'total', 'grade', 'comment')
    list_display_links = ('student', 'semester', 'course', 'ca', 'ca2', 'exam', 'total', 'grade', 'comment')
    list_per_page = 10
    search_fields = ('student__full_student_no', 'semester', 'course', 'ca', 'ca2', 'exam', 'total', 'grade', 'comment')
    list_filter = ('semester',)


class ResultAdmin(ImportExportModelAdmin):
    list_display = ('student', 'course', 'gpa', 'cgpa', 'semester', 'session', 'level')
    list_display_links = ('student', 'course', 'gpa', 'cgpa', 'semester', 'session', 'level')
    list_per_page = 10
    search_fields = ('student__full_student_no', 'semester', 'course', 'gpa', 'cgpa',)
    list_filter = ('semester', 'level')


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
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(PaymentStructure, PaymentStructureAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(TakenCourse, TakenCourseAdmin)
admin.site.register(Result, ResultAdmin)