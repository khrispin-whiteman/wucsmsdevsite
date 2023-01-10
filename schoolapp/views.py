import socket
from smtplib import SMTPAuthenticationError
import arrow
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from schoolapp.models import User, Department, School, Program, Course, StudentNumber, SystemSettings, Admission, \
    Session
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .forms import OnlineAdmissionForm, AddTeacherForm, AddSchoolForm, AddDepartmentForm, UpdateOnlineApplicationForm
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import random
import string
from django.http import FileResponse
from fpdf import FPDF


# Create your views here.
def index(request):
    # Get list of departments
    departments = Department.objects.all()
    # Get list of schools
    schools = School.objects.all()
    return render(request, "schoolapp/landingpages/index.html",
                  {
                      'departments': departments,
                      'schools': schools,
                  })


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_forgot_password(request):
    return render(request, "schoolapp/systempages/forgot-password.html", {})


def dashboard(request):
    # Get list of departments
    departments = Department.objects.all()
    # Get list of schools
    schools = School.objects.all()
    return render(request, "schoolapp/systempages/index.html",
                  {
                      'departments': departments,
                      'schools': schools,
                  })


def testtemplate(request):
    return render(request, 'schoolapp/landingpages/templogin.html', {})


def templogintocheckapplicationstatus(request):
    print('Method Called')
    if request.method == 'POST':
        nrc_no = request.POST.get('nrc_no')
        tmp_password = request.POST.get('tmp_password')
        print('NRC: ', nrc_no)
        print('PASSWORD: ', tmp_password)
        if Admission.objects.filter(nrc_no__exact=nrc_no, temp_password__exact=tmp_password):
            print('FOUND')
            application_details = Admission.objects.get(nrc_no__exact=nrc_no, temp_password__exact=tmp_password)
            return render(request, 'schoolapp/landingpages/checkapplicationstatus.html',
                          {
                              'application_detail': application_details,
                              'nrc_no': nrc_no
                          })
        else:
            return render(request, 'schoolapp/landingpages/templogin.html',
                          {
                              'message': 'NRC Number or Password not correct!'
                          })
    else:
        return render(request, 'schoolapp/landingpages/templogin.html', {})


def checkapplicationstatus(request, nrc_no):
    return render(request, 'schoolapp/landingpages/checkapplicationstatus.html',
                  {
                      'nrc_no': nrc_no,
                  })


def generateStudentNumberRandomDigits():
    # get the year and month
    year_month = arrow.now().format('YYMM')

    # get the length of the last digits from the database
    ss = SystemSettings.objects.all().first()
    if ss:
        length = ss.student_no_last_digits_length
    else:
        length = 4
    random_str = ''.join(
        random.choice(string.digits) for _ in range(length)
    )

    # random_str = int(random_str) + 1
    # txt = str(random_str)
    # x = txt.zfill(length)
    x = random_str.zfill(length)

    student_number = year_month + x
    # print('STUDENT NO: ', student_number + str(type(student_number)))
    # check if number already taken
    if StudentNumber.objects.filter(full_student_no__exact=student_number):
        print('Number Already Taken!')
        generateStudentNumberRandomDigits()
    else:
        return student_number


# generate student number
# def generateStudentNumber(request):
#     student_number = arrow.now().format('YYMM')
#     num_from_db = StudentNumber.objects.all().aggregate(Max('digit'))['digit__max']
#     # print('NUM FROM DB: ', num_from_db)
#     lenth = 4
#     num_from_db = num_from_db + 1
#     txt = str(num_from_db)
#     x = txt.zfill(lenth)
#
#     student_number = student_number + x
#     # print('STUDENT NO: ', student_number + str(type(student_number)))
#     # check if number already taken
#     if StudentNumber.objects.filter(full_student_no__exact=student_number):
#         print('Number Already Taken!')
#         student_no = generateStudentNumberRandomDigits(request)
#         return student_no
#     else:
#         obj = StudentNumber()
#         return HttpResponse(student_number)


# generate temp password for application status checking
def generateTempPassword(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def online_admission(request):
    programs = Program.objects.all()
    if request.method == 'POST':
        application_form = OnlineAdmissionForm(request.POST, request.FILES)
        print('PROGRAM: ', request.POST.get('program_applied_for'))

        if application_form.is_valid():
            print('FORM IS VALID')
            # get temp password
            tmp_password = generateTempPassword(10)
            application_form.temp_password = tmp_password
            # print('PASSWORD: ', tmp_password)

            # get program using id
            program = Program.objects.get(id=request.POST.get('program_applied_for'))

            # generate student number
            student_no = generateStudentNumberRandomDigits()
            sn_obj = StudentNumber.objects.create(full_student_no=student_no)
            print('STUDENT NO: ', sn_obj.full_student_no)

            obj = application_form.save(commit=False)
            obj.program_applied_for = program
            obj.student_number = sn_obj
            obj.temp_password = tmp_password
            obj.intake = Session.objects.get(is_current_session=True)
            obj.save()

            # notify applicant via mail
            # get email content
            firstname = application_form.cleaned_data.get('first_name')
            subject = 'WUC Online Application'
            message = 'Dear, ' + application_form.cleaned_data.get(
                "first_name") + ' ' + application_form.cleaned_data.get("last_name") + '\n\n' \
                                                                                       'Your application for the program ' + str(
                application_form.cleaned_data.get('program_applied_for')) + \
                      ' has been successfully submitted, you will be notified once it has been reviewed by the school' \
                      ' administration. You can check the status of your application via this link https://wucsmstest.pythonanywhere.com/application-status/ \n' \
                      'You will be required to provide your NRC number and the temporal system gerated password.\n\n' \
                      'NRC No.: ' + application_form.cleaned_data.get('nrc_no') + '\n' \
                                                                                  'PASSWORD: ' + tmp_password + '\n' \
                                                                                                                'LINK: https://wucsmstest.pythonanywhere.com/application-status/\n\n' \
                                                                                                                'Keep the information above safe or you will be unable to see your application status.\n\n' \
                                                                                                                'You can go back and make changes to your application details before close of application,\n' \
                                                                                                                'For more information, contact the academic office on: 0900000000 or 0700000000'

            from_email = 'chrispinkay@gmail.com'
            try:
                send_mail(subject, message, from_email, recipient_list=[application_form.cleaned_data.get('email'), ],
                          fail_silently=False)

            except socket.gaierror:
                print('NO INTERNET ACCESS')
                return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
            except ConnectionError:
                print('CONNECTION ERROR')
                return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
            except SMTPAuthenticationError:
                return HttpResponse('Host Email Username and Password not accepted, Email Not Sent!')

            # add a success page to be rendered
            messages.success(request, 'Application Successfully Submitted!')
            context = {
                'message': messages,
                'form': application_form,
                'programs': programs
            }
            return render(request, 'schoolapp/landingpages/application_successful.html', context)
            # return redirect('index')

        else:
            print('FORM IS NOT VALID', application_form.errors)
            messages.error(request, application_form.errors)
            context = {
                'message': application_form.errors,
                'form': application_form,
                'programs': programs
            }
            return render(request, 'schoolapp/landingpages/online_registration.html', context)
    else:
        # Get list of departments
        departments = Department.objects.all()

        # Get list of schools
        schools = School.objects.all()

        # Get list of programs
        programs = Program.objects.all()

        application_form = OnlineAdmissionForm()
        return render(request, "schoolapp/landingpages/online_registration.html",
                      {
                          'departments': departments,
                          'schools': schools,
                          'programs': programs,
                          'form': application_form,
                      })


def updateonlineapplication(request, nrc_no):
    if request.method == 'POST':
        application = Admission.objects.get(nrc_no=nrc_no)
        form = UpdateOnlineApplicationForm(request.POST, request.FILES, instance=application)
        print('INSIDE POST')
        print(form.errors)
        if form.is_valid():
            print('FORM IS VALID')
            form.save()

            # pre-populate the form with an existing band
            # return redirect('templogintocheckapplicationstatus')
            return render(request, 'schoolapp/landingpages/checkapplicationstatus.html',
                          {
                              'application_detail': application,
                              'nrc_no': nrc_no
                          })
        else:
            return render(request, 'schoolapp/landingpages/update_application.html',
                          {
                              'form': form,
                              'application_detail': application,
                              'nrc_no': nrc_no
                          })

    application = Admission.objects.get(nrc_no=nrc_no)
    form = UpdateOnlineApplicationForm(instance=application)
    return render(request, 'schoolapp/landingpages/update_application.html',
                  {
                      'form': form,
                      'application': application,
                  })


def departments(request):
    # Get list of departments
    departments = Department.objects.all()

    # Get list of schools
    schools = School.objects.all()
    return render(request, "schoolapp/systempages/departments.html",
                  {
                      'departments': departments,
                      'schools': schools,
                  })


def add_department(request):
    add_department_form = AddDepartmentForm()
    if request.method == 'POST':
        add_department_form = AddDepartmentForm(request.POST, request.FILES)
        print('INSIDE POST')
        if add_department_form.is_valid():
            print('FORM VALID')
            print(add_department_form.cleaned_data['department_name'])
            print(add_department_form.cleaned_data['department_description'])
            add_department_form.save()
            # return redirect('departments')
            departments = Department.objects.all()
            return render(request, 'schoolapp/systempages/departments.html',
                          {
                              'departments': departments,
                          })

        else:
            return render(request, 'schoolapp/systempages/add-department.html',
                          {
                              'add_department_form': add_department_form,
                          })
    return render(request, 'schoolapp/systempages/add-department.html',
                  {
                      'add_department_form': add_department_form,
                  })


def school_details(request, school_id):
    # Get list of departments
    departments = Department.objects.all()

    # Get list of schools
    schools = School.objects.all()

    # Get the school
    school = School.objects.get(id=school_id)

    # get a list of programs in that selected school
    programs = Program.objects.filter(program_school_id=school_id)
    return render(request, "schoolapp/landingpages/programs_list.html",
                  {
                      'departments': departments,
                      'schools': schools,
                      'school': school,
                      'programs': programs,
                  })


def programs(request):
    # Get list of departments
    departments = Department.objects.all()

    # Get list of schools
    schools = School.objects.all()

    # Get list of programs
    programs = Program.objects.all()
    return render(request, "schoolapp/landingpages/programs_list.html",
                  {
                      'departments': departments,
                      'schools': schools,
                      'programs': programs,
                  })


def program_details(request, program_id):
    # Get list of departments
    departments = Department.objects.all()

    # Get list of schools
    schools = School.objects.all()

    # Get the program
    program = Program.objects.get(id=program_id)

    # get a list of courses in that selected program
    courses = Course.objects.filter(course_program_id=program_id)
    return render(request, "schoolapp/landingpages/courses_list.html",
                  {
                      'program': program,
                      'courses': courses,
                      'departments': departments,
                      'schools': schools,
                  })


def courses(request):
    # Get list of departments
    departments = Department.objects.all()
    # Get list of schools
    schools = School.objects.all()
    # Get list of courses
    courses = Course.objects.all()
    return render(request, "schoolapp/landingpages/courses_list.html",
                  {
                      'departments': departments,
                      'schools': schools,
                      'courses': courses,
                  })


@login_required()
def admin_admissions_list(request):
    global admissions
    users = User.objects.all()

    if request.user.user_group == 'Admissions Office':
        print('Admissions Office')
        admissions = Admission.objects.filter(application_stage='Admissions Office')

    elif request.user.user_group == 'Accounts Office':
        print('Accounts Office')
        admissions = Admission.objects.filter(application_stage='Accounts Office')

    elif request.user.user_group == 'Dean Of Students Affairs Office':
        print('Dean Of Students Affairs Office')
        admissions = Admission.objects.filter(application_stage='Dean Of Students Affairs Office')

    elif request.user.user_group == 'ICT Office':
        print('ICT Office')
        admissions = Admission.objects.filter(application_stage='ICT Office')

    elif request.user.user_group == 'Program Coordinator or Principal Lecturer Office':
        print('Program Coordinator or Principal Lecturer Office')
        admissions = Admission.objects.filter(application_stage='Program Coordinator or Principal Lecturer Office')

    elif request.user.user_group == 'Registrar Office':
        print('Registrar Office')
        admissions = Admission.objects.filter(application_stage='Registrar Office')

    elif request.user.is_staff or request.user.is_superuser:
        print('Super User')
        admissions = Admission.objects.all()

    return render(request, 'schoolapp/systempages/admin_admissions_list.html',
                  {
                      'admissions': admissions,
                  })
    # return HttpResponse('Yoh!')


@login_required()
def admin_admissions_detail(request, admission_id):
    admission_details = Admission.objects.get(id=admission_id)
    print('INSIDE ADMIN ADMISSIONS DETAIL')
    if request.method == 'POST':
        print('INSIDE POST')
        online_admission_form = OnlineAdmissionForm(request.POST, request.FILES)
        if online_admission_form.is_valid():
            print('FORM VALID')
            online_admission_form.save()

            return HttpResponse('Approved!')
        else:
            return render(request, 'schoolapp/systempages/admin_admissions_details.html',
                          {'online_admission_form': online_admission_form})
    online_admission_form = OnlineAdmissionForm()
    return render(request, 'schoolapp/systempages/admin_admissions_details.html',
                  {
                      'admission_details': admission_details,
                      'online_admission_form': online_admission_form,
                  })


@login_required()
def admin_approve_application(request, admission_id):
    form = OnlineAdmissionForm()
    # get the admission with given id
    admission_details = Admission.objects.get(id=admission_id)
    if request.user.user_group == 'Admissions Office':
        if request.method == 'POST':
            # print('INSIDE POST')
            # if the status picked is 'Verified'
            if request.POST['application_status'] == 'Verified':
                admission_details.application_status = request.POST['application_status']
                admission_details.admissions_office_comment = request.POST['admissions_office_comment']
                admission_details.application_stage = 'Accounts Office'
                admission_details.admissions_office = True
                admission_details.admissions_office_user = request.user
                print('ADMINISTER USER: ', request.user)
                admission_details.save()

    if request.user.user_group == 'Accounts Office':
        if request.method == 'POST':
            # print('INSIDE POST')
            # if the status picked by accounts is 'Verified'
            if request.POST['application_status'] == 'Verified':
                # admission_details.balance_due = request.POST['balance_due']
                admission_details.accounts_office_comment = request.POST['accounts_office_comment']
                admission_details.application_status = request.POST['application_status']
                admission_details.application_stage = 'Registrar Office'
                admission_details.accounts_office = True
                admission_details.accounts_office_user = request.user
                print('ACCOUNTS USER: ', request.user)
                admission_details.save()

            if request.POST['application_status'] == 'Pending':
                admission_details.balance_due = request.POST['balance_due']
                admission_details.accounts_office_comment = request.POST['accounts_office_comment']
                admission_details.application_status = request.POST['application_status']
                admission_details.application_stage = 'Accounts Office'
                admission_details.accounts_office = False
                admission_details.accounts_office_user = request.user
                print('ACCOUNTS USER: ', request.user)
                admission_details.save()

    # if request.user.user_group == 'Dean Of Students Affairs Office':
    #     admission_details.application_stage = 'ICT Office'
    #     admission_details.dean_of_students_affairs_office = True
    #     admission_details.dean_of_students_affairs_office_user = request.user
    #     print('ICT USER: ', request.user)
    #     admission_details.save()

    # if request.user.user_group == 'ICT Office':
    #     if request.method == 'POST':
    #         # print('INSIDE POST')
    #         admission_details.ict_office_comment = request.POST['ict_office_comment']
    #         admission_details.save()
    #
    #     admission_details.application_stage = 'Program Coordinator or Principal Lecturer Office'
    #     admission_details.ict_office = True
    #     admission_details.ict_office_user = request.user
    #     admission_details.save()

    # if request.user.user_group == 'Program Coordinator or Principal Lecturer Office':
    #     if request.method == 'POST':
    #         # print('INSIDE POST')
    #         admission_details.program_coordinator_or_principal_lecturer_office_comment = request.POST['program_coordinator_or_principal_lecturer_office_comment']
    #         admission_details.save()
    #
    #     admission_details.application_stage = 'Registrar Office'
    #     admission_details.program_coordinator_or_principal_lecturer_office = True
    #     admission_details.program_coordinator_or_principal_lecturer_office_user = request.user
    #     admission_details.save()

    if request.user.user_group == 'Registrar Office':
        if request.POST['application_status'] == 'Rejected':
            print('INSIDE POST')
            admission_details.registrar_office_comment = request.POST['registrar_office_comment']
            admission_details.application_status = request.POST['application_status']
            admission_details.application_stage = 'Registrar Office'
            admission_details.accounts_office = False
            admission_details.accounts_office_user = request.user
            print('REGISTRAR USER: ', request.user)
            admission_details.save()

            # notify applicant via mail
            subject = 'Admission Confirmation'

            message = 'Dear Mr./Mrs./Ms. ' + str(admission_details.last_name) + '\n' \
            'Thank you for your application for admission to [name of college]. \n' \
            'After reviewing your application and supporting documentation, we regret that we must decline your application at this time. \n' \
            'The applicant pool for this academic year has exceeded our available openings for admission. \n' \
            'The decision has been difficult, and although you show outstanding potential as a student, the competition is intense. \n' \
            'You are welcome to apply after you complete your GRE testing, which was not included in this year’s application. \n' \
            'It is a requirement for admission at Woodlands University College.\n\n' \
            'We appreciate your consideration of Woodlands University College, along with the time and effort you put into your application. \n' \
            'We wish you the best of success in your academic endeavors. We encourage you to continue pursuit of your academic goals.\n\n' \

            'Sincerely,\n\n' \

            '' + request.user.get_full_name()

        from_email = 'chrispinkay@gmail.com'

        try:
            if request.POST['application_status'] == 'Rejected':
                send_mail(subject, message, from_email, recipient_list=[admission_details.email, ],
                          fail_silently=False)

        except socket.gaierror:
            print('NO INTERNET ACCESS')
            return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
        except ConnectionError:
            print('CONNECTION ERROR')
            return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
        except IntegrityError:
            return redirect('list_teacher')

    if request.POST['application_status'] == 'Approved':
        print('INSIDE POST')
        admission_details.registrar_office_comment = request.POST['registrar_office_comment']
        admission_details.application_status = request.POST['application_status']
        admission_details.application_stage = 'Registrar Office'
        admission_details.application_stage = 'Approved'
        admission_details.registrar_office = True
        admission_details.registrar_office_user = request.user
        admission_details.save()

        # notify applicant via mail
        subject = 'Admission Confirmation'

        message = 'Dear ' + str(admission_details.first_name) + ', \n\n' \
                 'This is ' + request.user.get_full_name() + ' from the registrars office of Woodlands University College, ' \
                 'I want to congratulate you that you have been qualified for Admission ' + str(
                 admission_details.program_applied_for) + ', and you ' \
                 'are requested to contact the administration department for further process. Your first semester classes ' \
                 'will start on (Date). \n\n' \
                 'Kindly meet the concerned person for fee structure, and course details, etc. ' \
                 'You are among those lucky people who have got the chance to study in such a renowned university. ' \
                 'Looking forward to your action against this letter and hope that you will contact us as early as possible.\n\n ' \
                 'You can go back and make changes before close of application.\n\n' \
                 'Yours sincerely, \n\n' \
                 'Name… \n' \
                 'Registrars Office \n\n' \
                 'Woodlands University College \n\n' \
                 '09777777777 or 09888888888'

        from_email = 'chrispinkay@gmail.com'

        try:
            if request.POST['application_status'] == 'Approved':
                send_mail(subject, message, from_email, recipient_list=[admission_details.email, ],
                          fail_silently=False)

        except socket.gaierror:
            print('NO INTERNET ACCESS')
            return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
        except ConnectionError:
            print('CONNECTION ERROR')
            return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
        except IntegrityError:
            return redirect('list_teacher')


    # get all admissions
    global admissions
    if request.user.user_group == 'Admissions Office':
        admissions = Admission.objects.filter(application_stage='Admissions Office')
    elif request.user.user_group == 'Accounts Office':
        admissions = Admission.objects.filter(application_stage='Accounts Office')
    # elif request.user.user_group == 'Dean Of Students Affairs Office':
    #     admissions = Admission.objects.filter(application_stage='Dean Of Students Affairs Office')
    elif request.user.user_group == 'ICT Office':
        admissions = Admission.objects.filter(application_stage='ICT Office')
    elif request.user.user_group == 'Program Coordinator or Principal Lecturer Office':
        admissions = Admission.objects.filter(application_stage='Program Coordinator or Principal Lecturer Office')
    elif request.user.user_group == 'Registrar Office':
        admissions = Admission.objects.filter(application_stage='Registrar Office')
    print('STATUS: ', status)
    message = 'Application Successfully Verified!'
    if request.user.user_group == 'Registrar Office':
        message = 'Application Successfully Approved!'
    return render(request, 'schoolapp/systempages/admin_admissions_list.html',
                  {
                      'success_message': message,
                      'admissions': admissions,
                  })


# lists teachers
@login_required()
def list_teacher(request):
    teachers = User.objects.filter(is_active=True, is_staff=True, is_member_of_staff=True)
    return render(request, 'schoolapp/systempages/teachers.html', {
        'teachers': teachers,
    })


# add teacher
@login_required()
def add_teacher(request):
    if request.method == 'POST':
        add_teacher_form = AddTeacherForm(request.POST, request.FILES)
        print('INSIDE POST')

        if add_teacher_form.is_valid():
            print('FORM VALID')
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(5))

            form = add_teacher_form.save(commit=False)
            print('USERNAME: ', add_teacher_form.cleaned_data.get('first_name'))
            f_name = add_teacher_form.cleaned_data.get('first_name')
            form.username = request.POST.get('first_name')
            form.is_member_of_staff = True
            form.is_staff = True

            form.set_password(result_str)
            print('FORM VALID', result_str)
            try:
                form.save()
            except IntegrityError:
                return redirect('list_teacher')

            # notify agent via mail
            subject = 'User Account Creation'
            message = 'Dear, ' + str(f_name) + '\n\n' \
                                               'Your account on Woodlands University College web portal was successfully created.\n\n' \
                                               'Your Login credentials are below:\n\n' \
                                               'USERNAME: ' + str(f_name) + '\n' \
                                                                            'PASSWORD: ' + str(result_str) + '\n\n' \
                                                                                                             'Log into your account by Visiting the link below:\n\n' \
                      + request.get_host()

            from_email = 'chrispinkay@gmail.com'

            try:
                send_mail(subject, message, from_email, recipient_list=[add_teacher_form.cleaned_data.get('email'), ],
                          fail_silently=False)

            except socket.gaierror:
                print('NO INTERNET ACCESS')
                return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
            except ConnectionError:
                print('CONNECTION ERROR')
                return HttpResponse('Check Your Internet Connection And Try Again. Email not sent')
            except IntegrityError:
                return redirect('list_teacher')

            teachers = User.objects.filter(is_member_of_staff=True)
            return render(request, 'schoolapp/systempages/teachers.html', {
                'add_teacher_form': add_teacher_form,
                'success_message': 'Lecturer Added Successfully',
                'teachers': teachers
            })

    add_teacher_form = AddTeacherForm()
    return render(request, 'schoolapp/systempages/add-teacher.html', {
        'add_teacher_form': add_teacher_form,
        'error_message': 'Lecturer Not Added'
    })


# lists teachers
@login_required()
def list_students(request):
    students = User.objects.filter(is_student=True)
    return render(request, 'schoolapp/systempages/students.html', {
        'students': students,
    })


# lists teachers
@login_required()
def list_schools(request):
    schools = School.objects.all()
    return render(request, 'schoolapp/systempages/schools.html', {
        'schools': schools,
    })


# add teacher
@login_required()
def add_school(request):
    if request.method == 'POST':
        add_school_form = AddSchoolForm(request.POST, request.FILES)
        print('INSIDE POST')

        if add_school_form.is_valid():
            print('FORM VALID')
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(5))

            add_school_form.save()
            print('SCHOOL NAME: ', add_school_form.cleaned_data.get('school_name'))

            schools = School.objects.all()
            return render(request, 'schoolapp/systempages/edit_school.html', {
                'add_school_form': add_school_form,
                'success_message': 'School Added Successfully',
                'schools': schools
            })

    add_school_form = AddSchoolForm()
    return render(request, 'schoolapp/systempages/add-teacher.html', {
        'add_teacher_form': add_school_form,
        'error_message': 'Teacher Not Added'
    })


@login_required()
def list_schools(request):
    schools = School.objects.all()
    return render(request, 'schoolapp/systempages/schools.html', {
        'schools': schools,
    })

# add teacher
# @login_required()
# def add_student(request):
#     if request.method == 'POST':
#         add_teacher_form = AddStudentForm(request.POST, request.FILES)
#         print('INSIDE POST')
#
#         if add_teacher_form.is_valid():
#             print('FORM VALID')
#             form = add_teacher_form.save(commit=False)
#             form.username = request.POST.get('first_name')
#             form.is_member_of_staff = True
#             form.set_password(generateTempPassword(5))
#             form.save()
#
#             teachers = User.objects.filter(is_member_of_staff=True)
#             return render(request, 'schoolapp/systempages/teachers.html', {
#                 'add_teacher_form': add_teacher_form,
#                 'success_message': 'Teacher Added Successfully',
#                 'teachers': teachers
#             })
#
#     add_student_form = AddStudentForm()
#     return render(request, 'schoolapp/systempages/add-teacher.html', {
#         'add_teacher_form': add_teacher_form,
#         'error_message': 'Teacher Not Added'
#     })


def application_report(request, id):
    application_details = Admission.objects.get(id=id)
    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 5, 'WOODLANDS UNIVERSITY COLLEGE', 0, 1)
    pdf.set_font('Arial', '', 13)
    pdf.cell(40, 5, 'Ibex Hill 2457 Main Street',0,1)
    pdf.set_font('Arial', '', 13)
    pdf.cell(40, 5, 'Lusaka',0,1)
    pdf.cell(40, 5, 'E-mail: woodlandsuniversity@wuc.uni',0,1)
    pdf.cell(40, 12, 'CALL: 0966186239',0,1)
    pdf.set_font('Times', 'B', 15)
    pdf.cell(40, 5, 'Personal Particulars',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Full Name'.ljust(30)} {'Student Number'.ljust(20)}", 0, 1)
    pdf.cell(200, 8,
             f"{application_details.first_name + ' ' + application_details.other_names + ' ' + application_details.last_name + ' '.ljust(30)} {'Student Number'.ljust(20)}",
             0, 1)
    # pdf.cell(200, 8, f"{application_details.first_name.ljust(30)} {'Student Number'.ljust(20)}", 0, 1)
    # pdf.line(10, 30, 150, 30)
    # pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)
    pdf.output('Wuc Application Form.pdf', 'F')
    return FileResponse(open('Wuc Application Form.pdf', 'rb'), as_attachment=True, content_type='application/pdf')