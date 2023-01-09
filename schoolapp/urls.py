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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('departments/', views.departments, name='departments'),
    path('programs/', views.programs, name='programs'),
    path('programs/<int:program_id>/courses/', views.program_details, name='program_details'),
    path('schools/<int:school_id>/programs/', views.school_details, name='school_details'),
    path('courses/', views.courses, name='courses'),
    path('online-admission/', views.online_admission, name='online-admission'),
    path('application-status/', views.templogintocheckapplicationstatus, name='templogintocheckapplicationstatus'),
    path('api/forgot-password/', views.user_forgot_password, name='user_forgot_password'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('admin-admissions/', views.admin_admissions_list, name='admin_admissions_list'),
    path('admin-admissions/<int:admission_id>/', views.admin_admissions_detail, name='admin_admissions_detail'),
    path('update-online-application/<str:nrc_no>/', views.updateonlineapplication, name='updateonlineapplication'),
    path('admin-admissions/<int:admission_id>/approve/', views.admin_approve_application, name='admin_approve_application'),
    path('admin-add-teacher/', views.add_teacher, name='add_teacher'),
    path('admin-list-teacher/', views.list_teacher, name='list_teacher'),
    path('admin-list-student/', views.list_students, name='list_students'),
    path('admin-list-school/', views.list_schools, name='list_schools'),
    path('admin-add-department/', views.add_department, name='add_department'),
    path('generatestudno/', views.generateStudentNumberRandomDigits, name='generateStudentNumberRandomDigits'),
]
