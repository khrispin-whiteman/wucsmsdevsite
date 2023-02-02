from django.urls import path
from schoolapp import views

urlpatterns = [
    # testing urls
    path('testtemplate/', views.testtemplate, name='testtemplate'),
    path('applicationreport/<int:id>/', views.application_report, name='application_report'),
    # path('generatestudentno/', views.generateStudentNumber, name='generateStudentNumber'),
    path('generatestudentnorandomly/', views.generateStudentNumberRandomDigits, name='generateStudentNumberRandomDigits'),

    # system urls
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('departments/', views.departments, name='departments'),
    path('programs/', views.programs, name='programs'),
    path('programs/admin/', views.admin_list_programs, name='admin_list_programs'),
    path('programs/<int:program_id>/courses/', views.program_details, name='program_details'),
    path('schools/<int:school_id>/programs/', views.school_details, name='school_details'),
    path('courses/', views.courses, name='courses'),
    path('online-admission/', views.online_admission, name='online-admission'),
    path('admin-student-registration/', views.admin_online_student_registration, name='admin_student_registration'),
    path('application-status/', views.templogintocheckapplicationstatus, name='templogintocheckapplicationstatus'),
    path('api/forgot-password/', views.user_forgot_password, name='user_forgot_password'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('admin-admissions/', views.admin_admissions_list, name='admin_admissions_list'),
    path('admin-admissions/<int:admission_id>/', views.admin_admissions_detail, name='admin_admissions_detail'),
    path('update-online-application/<str:student_no>/', views.updateonlineapplication, name='updateonlineapplication'),
    path('admin-admissions/<int:admission_id>/approve/', views.admin_approve_application, name='admin_approve_application'),
    path('admin-add-staff/', views.add_staff, name='add_staff'),
    path('admin-search-application/', views.search_applicant_by_student_no, name='search_applicant_by_student_no'),
    path('admin-add-student/<int:application_id>/', views.add_student, name='add_student'),
    path('admin-add-school/', views.add_school, name='add_school'),
    path('admin-list-staff/', views.list_staff, name='list_staff'),
    path('admin-list-student/', views.list_students, name='list_students'),
    path('admin-list-school/', views.list_schools, name='list_schools'),
    path('admin-add-department/', views.add_department, name='add_department'),
    path('generatestudno/', views.generateStudentNumberRandomDigits, name='generateStudentNumberRandomDigits'),

    # accounts urls
    path('accounts/payments/types/', views.payment_types_list, name='payment_types_list'),
    path('accounts/payments/structures/', views.payment_structures_list, name='payment_structures_list'),
    path('accounts/payments/collections/', views.payment_collections_list, name='payment_collections_list'),
    path('accounts/payments/collect/', views.payment_collect, name='payment_collect'),
    path('accounts/payments/types/add/', views.add_payment_type, name='add_payment_type'),
    path('accounts/payments/structures/add/', views.add_payment_structure, name='add_payment_structure'),

    # results
    path('score/add/', views.add_score, name='add_score'),
    path('score/<int:id>/', views.add_score_for, name='add_score_for'),
]
