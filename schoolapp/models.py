from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



# Create your models here.
COUNTRIES = (
    ('Zambia', 'Zambia'),
    ('AD', 'Andorra'),
    ('AE', 'United Arab Emirates'),
    ('AF', 'Afghanistan'),
    ('AG', 'Antigua & Barbuda'),
    ('AI', 'Anguilla'),
    ('AL', 'Albania'),
    ('AM', 'Armenia'),
    ('AN', 'Netherlands Antilles'),
    ('Angola', 'Angola'),
    ('AQ', 'Antarctica'),
    ('AR', 'Argentina'),
    ('AS', 'American Samoa'),
    ('AT', 'Austria'),
    ('AU', 'Australia'),
    ('AW', 'Aruba'),
    ('AZ', 'Azerbaijan'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BB', 'Barbados'),
    ('BD', 'Bangladesh'),
    ('BE', 'Belgium'),
    ('BF', 'Burkina Faso'),
    ('BG', 'Bulgaria'),
    ('BH', 'Bahrain'),
    ('BI', 'Burundi'),
    ('BJ', 'Benin'),
    ('BM', 'Bermuda'),
    ('BN', 'Brunei Darussalam'),
    ('BO', 'Bolivia'),
    ('BR', 'Brazil'),
    ('BS', 'Bahama'),
    ('BT', 'Bhutan'),
    ('BV', 'Bouvet Island'),
    ('BW', 'Botswana'),
    ('BY', 'Belarus'),
    ('BZ', 'Belize'),
    ('CA', 'Canada'),
    ('CC', 'Cocos (Keeling) Islands'),
    ('CF', 'Central African Republic'),
    ('CG', 'Congo'),
    ('CH', 'Switzerland'),
    ('Ivory Coast', 'Ivory Coast'),
    ('CK', 'Cook Islands'),
    ('CL', 'Chile'),
    ('CM', 'Cameroon'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('CR', 'Costa Rica'),
    ('CU', 'Cuba'),
    ('Cape Verde', 'Cape Verde'),
    ('CX', 'Christmas Island'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DJ', 'Djibouti'),
    ('DK', 'Denmark'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('Algeria', 'Algeria'),
    ('EC', 'Ecuador'),
    ('EE', 'Estonia'),
    ('Egypt', 'Egypt'),
    ('EH', 'Western Sahara'),
    ('Eritrea', 'Eritrea'),
    ('ES', 'Spain'),
    ('Ethiopia', 'Ethiopia'),
    ('FI', 'Finland'),
    ('FJ', 'Fiji'),
    ('FK', 'Falkland Islands (Malvinas)'),
    ('FM', 'Micronesia'),
    ('FO', 'Faroe Islands'),
    ('FR', 'France'),
    ('FX', 'France, Metropolitan'),
    ('Gabon', 'Gabon'),
    ('GB', 'United Kingdom (Great Britain)'),
    ('GD', 'Grenada'),
    ('GE', 'Georgia'),
    ('GF', 'French Guiana'),
    ('Ghana', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GL', 'Greenland'),
    ('Gambia', 'Gambia'),
    ('Guinea', 'Guinea'),
    ('GP', 'Guadeloupe'),
    ('GQ', 'Equatorial Guinea'),
    ('GR', 'Greece'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('GT', 'Guatemala'),
    ('GU', 'Guam'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HK', 'Hong Kong'),
    ('HM', 'Heard & McDonald Islands'),
    ('HN', 'Honduras'),
    ('HR', 'Croatia'),
    ('HT', 'Haiti'),
    ('HU', 'Hungary'),
    ('ID', 'Indonesia'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IN', 'India'),
    ('IO', 'British Indian Ocean Territory'),
    ('IQ', 'Iraq'),
    ('IR', 'Islamic Republic of Iran'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JO', 'Jordan'),
    ('JP', 'Japan'),
    ('Kenya', 'Kenya'),
    ('KG', 'Kyrgyzstan'),
    ('KH', 'Cambodia'),
    ('KI', 'Kiribati'),
    ('Comoros', 'Comoros'),
    ('KN', 'St. Kitts and Nevis'),
    ('KP', 'Korea, Democratic People\'s Republic of'),
    ('KR', 'Korea, Republic of'),
    ('KW', 'Kuwait'),
    ('KY', 'Cayman Islands'),
    ('KZ', 'Kazakhstan'),
    ('LA', 'Lao People\'s Democratic Republic'),
    ('LB', 'Lebanon'),
    ('LC', 'Saint Lucia'),
    ('LI', 'Liechtenstein'),
    ('LK', 'Sri Lanka'),
    ('Liberia', 'Liberia'),
    ('Lesotho', 'Lesotho'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('LV', 'Latvia'),
    ('Libya', 'Libya'),
    ('Morocco', 'Morocco'),
    ('MC', 'Monaco'),
    ('MD', 'Moldova, Republic of'),
    ('Madagascar', 'Madagascar'),
    ('MH', 'Marshall Islands'),
    ('Mali', 'Mali'),
    ('MN', 'Mongolia'),
    ('MM', 'Myanmar'),
    ('Macau', 'Macau'),
    ('MP', 'Northern Mariana Islands'),
    ('MQ', 'Martinique'),
    ('Mauritania', 'Mauritania'),
    ('MS', 'Monserrat'),
    ('MT', 'Malta'),
    ('Mauritius', 'Mauritius'),
    ('MV', 'Maldives'),
    ('Malawi', 'Malawi'),
    ('MX', 'Mexico'),
    ('MY', 'Malaysia'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('NC', 'New Caledonia'),
    ('Niger', 'Niger'),
    ('NF', 'Norfolk Island'),
    ('Nigeria', 'Nigeria'),
    ('NI', 'Nicaragua'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('NP', 'Nepal'),
    ('NR', 'Nauru'),
    ('NU', 'Niue'),
    ('NZ', 'New Zealand'),
    ('OM', 'Oman'),
    ('PA', 'Panama'),
    ('PE', 'Peru'),
    ('PF', 'French Polynesia'),
    ('PG', 'Papua New Guinea'),
    ('PH', 'Philippines'),
    ('PK', 'Pakistan'),
    ('PL', 'Poland'),
    ('PM', 'St. Pierre & Miquelon'),
    ('PN', 'Pitcairn'),
    ('PR', 'Puerto Rico'),
    ('PT', 'Portugal'),
    ('PW', 'Palau'),
    ('PY', 'Paraguay'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),
    ('RO', 'Romania'),
    ('RU', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Seychelles', 'Seychelles'),
    ('Sudan', 'Sudan'),
    ('SE', 'Sweden'),
    ('SG', 'Singapore'),
    ('SH', 'St. Helena'),
    ('SI', 'Slovenia'),
    ('SJ', 'Svalbard & Jan Mayen Islands'),
    ('SK', 'Slovakia'),
    ('SL', 'Sierra Leone'),
    ('SM', 'San Marino'),
    ('Senegal', 'Senegal'),
    ('Somalia', 'Somalia'),
    ('SR', 'Suriname'),
    ('ST', 'Sao Tome & Principe'),
    ('SV', 'El Salvador'),
    ('SY', 'Syrian Arab Republic'),
    ('Swaziland', 'Swaziland'),
    ('TC', 'Turks & Caicos Islands'),
    ('Chad', 'Chad'),
    ('TF', 'French Southern Territories'),
    ('Togo', 'Togo'),
    ('TH', 'Thailand'),
    ('TJ', 'Tajikistan'),
    ('TK', 'Tokelau'),
    ('TM', 'Turkmenistan'),
    ('TN', 'Tunisia'),
    ('TO', 'Tonga'),
    ('TP', 'East Timor'),
    ('TR', 'Turkey'),
    ('TT', 'Trinidad & Tobago'),
    ('TV', 'Tuvalu'),
    ('TW', 'Taiwan, Province of China'),
    ('Tanzania', 'Tanzania'),
    ('UA', 'Ukraine'),
    ('Uganda', 'Uganda'),
    ('UM', 'United States Minor Outlying Islands'),
    ('US', 'United States of America'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VA', 'Vatican City State (Holy See)'),
    ('VC', 'St. Vincent & the Grenadines'),
    ('VE', 'Venezuela'),
    ('VG', 'British Virgin Islands'),
    ('VI', 'United States Virgin Islands'),
    ('VN', 'Viet Nam'),
    ('VU', 'Vanuatu'),
    ('WF', 'Wallis & Futuna Islands'),
    ('WS', 'Samoa'),
    ('YE', 'Yemen'),
    ('YT', 'Mayotte'),
    ('YU', 'Yugoslavia'),
    ('South Africa', 'South Africa'),
    ('Zambia', 'Zambia'),
    ('Zaire', 'Zaire'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Unknown or unspecified country', 'Unknown or unspecified country'),
)

SEMESTER = (
    ('FIRST', "First"),
    ('SECOND', "Second"),
    ('THIRD', "Third"),
)

GENDER = (
    ('Male', "Male"),
    ('Female', "Female"),
    ('Other', "Other"),
)

MARITAL_STATUS = (
    ("---------", "---------"),
    ('Single', "Single"),
    ('Married', "Married"),
    ('Widowed', "Widowed"),
    ('Divorced', "Divorced"),
    ('Separated', "Separated"),
)

RELATIONSHIP_WITH_GUARDIAN = (
    ("Father", "Father"),
    ("Mother", "Mother"),
    ("Brother", "Brother"),
    ("Sister", "Sister"),
    ("Uncle", "Uncle"),
    ("Aunty", "Aunty"),
    ("Cousin", "Cousin"),
    ("Grand-Parent", "Grand-Parent"),
    ("Husband", "Husband"),
    ("Wife", "Wife"),
    ("Other", "Other"),
)

PROFESSIONAL_QUALIFICATION = (
    ('Certificate', "Certificate"),
    ('Diploma', "Diploma"),
    ('Degree', "Degree"),
)

APPLICATION_STATUS_CHOICES = (
    ('Verified', "Verified"),
    ('Pending', "Pending"),
    ('Approved', "Approved"),
    ('Rejected', "Rejected"),
)

USER_GROUPS = (
    ('Admissions Office', "Admissions Office"),
    ('Accounts Office', "Accounts Office"),
    ('Dean Of Students Affairs Office', "Dean Of Students Affairs Office"),
    ('ICT Office', "ICT Office"),
    ("Program Coordinator or Principal Lecturer Office", "Program Coordinator or Principal Lecturer Office"),
    ('Registrar Office', "Registrar Office"),
    ('Other', "Other"),
)


class User(AbstractUser):
    is_student = models.BooleanField(default=False, blank=True, null=True)
    is_member_of_staff = models.BooleanField(default=False)
    # is_admissions_officer = models.BooleanField(default=False)
    # is_accounts_officer = models.BooleanField(default=False)
    # is_dean_of_students_officer = models.BooleanField(default=False)
    # is_ict_officer = models.BooleanField(default=False)
    # is_registrars_officer = models.BooleanField(default=False)
    # is_pg_coordinators_officer = models.BooleanField(default=False)
    user_group = models.CharField('User Group', max_length=60, blank=True, null=True, choices=USER_GROUPS)
    phone = models.CharField(max_length=60, blank=True, null=True)
    # address = models.CharField(max_length=60, blank=True, null=True)
    # picture = models.ImageField(upload_to="users/pictures/%Y/%m/%d'", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # def get_picture(self):
    #     no_picture = f'{settings.STATIC_URL}schoolapp/images/img_avatar.png'
    #     try:
    #         return self.picture.url
    #     except Exception:
    #         return no_picture

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username

    def __str__(self):
        return self.get_full_name()


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    hod = models.ForeignKey(User, default='', null=True, help_text='Head of department', on_delete=models.SET_NULL)
    department_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.department_name


class School(models.Model):
    school_name = models.CharField(max_length=200)
    school_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school_name


class ProgramType(models.Model):
    pg_type_name = models.CharField('Program Type Name', max_length=200)
    pg_type_description = models.TextField('Program Type Description', null=True, blank=True)

    def __str__(self):
        return self.pg_type_name


class Program(models.Model):
    program_name = models.CharField(max_length=200)
    program_code = models.CharField(null=True, blank=True, max_length=200)
    program_school = models.ForeignKey(School, on_delete=models.CASCADE)
    program_type = models.ForeignKey(ProgramType, blank=True, on_delete=models.CASCADE)
    program_description = models.TextField()
    program_duration = models.CharField('Duration', null=True, blank=True, max_length=200)
    program_coordinator = models.ForeignKey(User, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.program_name


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    next_semester_begins = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{str(self.session)} - {str(self.semester)}'


class Level(models.Model):
    level = models.CharField('Year', max_length=200, )

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = 'Levels/Years of Study'
        verbose_name = 'Level/Year of Study'


class Course(models.Model):
    course_name = models.CharField('Course Name', max_length=200)
    course_code = models.CharField('Course Code', max_length=200)
    course_program = models.ForeignKey(Program, verbose_name='Program', help_text='Program to which the course belongs',
                                       on_delete=models.CASCADE)
    course_description = models.TextField('Course Description', null=True, blank=True)
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    level = models.ForeignKey(Level, verbose_name='Year', default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(null=True, blank=True, max_length=20, unique=True)
    program = models.ForeignKey(Program, verbose_name='Program', default='', on_delete=models.CASCADE)
    admission_date = models.DateField(auto_now_add=True, null=True, blank=True)
    level = models.ForeignKey(Level, verbose_name='Current Year Of Study', default='', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.get_full_name()}, {str(self.level)}Year'

    def save(self, **kwargs):
        if not self.id:
            # set is_student to be true
            u = User.objects.get(pk=self.user.pk)
            u.is_student = True
            u.save(force_update=u.is_active)
            super(Student, self).save()

    # def get_absolute_url(self):
    #     return reverse('profile')


class StudentNumber(models.Model):
    full_student_no = models.CharField(max_length=10, verbose_name='Full Student Number')

    def __str__(self):
        return self.full_student_no


class Admission(models.Model):
    # Persanal particulars
    application_date = models.DateField(auto_now=True)
    first_name = models.CharField(max_length=200, default='', verbose_name='First Name')
    last_name = models.CharField(max_length=200, default='', verbose_name='Last Name')
    other_names = models.CharField(max_length=200, null=True, blank=True, verbose_name='Other Names')
    nrc_no = models.CharField(max_length=200, unique=True, help_text='each NRC can only be used once',
                              verbose_name='NRC Number')
    phone_number = models.CharField(max_length=13, default='', verbose_name='Phone Number', )
    email = models.EmailField(max_length=200, verbose_name='Email Address', help_text='Required for communication')
    gender = models.CharField(max_length=200, default='Male', choices=GENDER, verbose_name='Gender')
    date_of_birth = models.DateField(max_length=200, null=True, blank=True, verbose_name='DOB', )
    nationality = models.CharField(max_length=200, choices=COUNTRIES, default='Zambia', verbose_name='Nationality', )
    # nationality = CountryField('Nationality', null=True, blank=True)
    marital_status = models.CharField(max_length=200, default='Single', choices=MARITAL_STATUS,
                                      verbose_name='Marital Status')
    physical_address = models.CharField(max_length=200, default='', verbose_name='Physical Address', )
    postal_address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Postal Address', )
    state_of_any_disabilities = models.CharField(max_length=200, null=True, blank=True,
                                                 verbose_name='State Disabilities If Any')

    # Part 2: Family Information
    sponsors_name_or_next_of_kin = models.CharField(max_length=200, null=True, blank=True,
                                                    verbose_name='Sponsor’s Name Or Next of Kin')
    relationship_with_sponsor_or_next_of_kin = models.CharField(max_length=200, null=True, blank=True,
                                                                choices=RELATIONSHIP_WITH_GUARDIAN,
                                                                verbose_name='Relationship with Sponsor Or Next Of Kin')
    sponsor_or_next_of_kin_cell_no = models.CharField(max_length=200, null=True, blank=True,
                                                      verbose_name='Sponsor Or Next of Kin Cell No')
    sponsor_or_next_of_kin_address = models.CharField(max_length=200, null=True, blank=True,
                                                      verbose_name='Sponsor Or Next of Kin Address')

    # Part 3: Qualifications and Program of choice
    program_applied_for = models.ForeignKey(Program, verbose_name='Program of Choice', blank=True, null=True,
                                            on_delete=models.DO_NOTHING)
    # Schools attended
    # School 1
    school_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='School Name')
    school_start_year = models.DateField(max_length=200, null=True, blank=True, verbose_name='Start Year')
    school_end_year = models.DateField(max_length=200, null=True, blank=True, verbose_name='End Year')
    # School 2
    # school_2_name = models.CharField(max_length=200, default='', verbose_name='School 2 Name')
    # school_2_years_from = models.CharField(max_length=200, default='', verbose_name='School 2 Years From')
    # school_2_years_to = models.CharField(max_length=200, default='', verbose_name='School 2 Years To')
    # Subjects and grades
    subject_english = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='English')
    subject_mathematics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Mathematics')
    subject_biology_human_and_social = models.PositiveSmallIntegerField(null=True, blank=True,
                                                        verbose_name='Biology/Human & Social')
    subject_history = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='History')
    subject_religious_education = models.PositiveSmallIntegerField(null=True, blank=True,
                                                   verbose_name='Religious Education')
    subject_commerce = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Commerce')
    subject_home_economics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Home Economics')
    subject_geography = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Geography')
    subject_physical_science = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Physical Science')
    subject_chemistry = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Chemistry')
    subject_physics = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Physics')
    subject_civic_education = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Civic Education')

    has_certificate = models.BooleanField(max_length=200, default=False, verbose_name='Certificate')
    has_diploma = models.BooleanField(max_length=200, default=False, verbose_name='Diploma')
    has_degree = models.BooleanField(max_length=200, default=False, verbose_name='Degree')

    # FILE ATTACHMENTS
    scanned_deposit_slip = models.FileField(upload_to="payments/deposits/%Y/%m/%d'", )
    scanned_nrc_front = models.FileField(null=True, blank=True, upload_to="id/nrc/%Y/%m/%d'", )
    scanned_nrc_back = models.FileField(null=True, blank=True, upload_to="id/nrc/%Y/%m/%d'", )
    scanned_statement_of_result = models.FileField(upload_to="qualifications/statement_of_result/%Y/%m/%d'", )
    scanned_pq_certificate = models.FileField(
        upload_to="qualifications/professional_qualification/%Y/%m/%d'", blank=True, null=True)
    scanned_pq_diploma = models.FileField(
        upload_to="qualifications/professional_qualification/%Y/%m/%d'", blank=True, null=True)
    scanned_pq_degree = models.FileField(
        upload_to="qualifications/professional_qualification/%Y/%m/%d'", blank=True, null=True)

    # Part 4: Declaration
    # Applicant
    declaration_confirmation = models.BooleanField(default=False, verbose_name='I have read the declaration')

    student_number = models.ForeignKey(StudentNumber, max_length=200, default='', verbose_name='Student Number',
                                       on_delete=models.CASCADE)
    application_status = models.CharField(max_length=200, default='Pending', blank=True, null=True, choices=APPLICATION_STATUS_CHOICES,
                                          verbose_name='Application Status')
    application_stage = models.CharField(max_length=200, default='Admissions Office', choices=USER_GROUPS,
                                         verbose_name='Application Stage')

    # approvals
    # approvals
    admissions_office = models.BooleanField(max_length=200, default=False, verbose_name='Admissions Office')
    admissions_office_comment = models.TextField(blank=True, null=True, verbose_name='Admissions Office Comment')
    admissions_office_user = models.ForeignKey(User, related_name='admissions_office_user', blank=True, null=True,
                                               on_delete=models.DO_NOTHING)

    accounts_office = models.BooleanField(max_length=200, default=False, verbose_name='Accounts Office')
    accounts_office_comment = models.TextField(blank=True, null=True, verbose_name='Accounts Office Comment')
    accounts_office_user = models.ForeignKey(User, related_name='accounts_office', blank=True, null=True,
                                             on_delete=models.DO_NOTHING)

    dean_of_students_affairs_office = models.BooleanField(max_length=200, default=False, verbose_name='Dean Of Students Affairs')
    dean_of_students_affairs_office_comment = models.TextField(blank=True, null=True, verbose_name='Deans Office Comment')
    dean_of_students_affairs_office_user = models.ForeignKey(User, related_name='dean_of_students_affairs_user',
                                                             blank=True, null=True, on_delete=models.DO_NOTHING)

    ict_office = models.BooleanField(max_length=200, default=False, verbose_name='ICT Office')
    ict_office_comment = models.TextField(blank=True, null=True, verbose_name='ICT Office Comment')
    ict_office_user = models.ForeignKey(User, related_name='ict_office_user', blank=True, null=True,
                                        on_delete=models.DO_NOTHING)

    program_coordinator_or_principal_lecturer_office = models.BooleanField(max_length=200, default=False,
                                                                           verbose_name='Program Coordinator Or Principal Lecturer')
    program_coordinator_or_principal_lecturer_office_comment = models.TextField(blank=True, null=True, verbose_name='PG Coordinator Office Comment')
    program_coordinator_or_principal_lecturer_office_user = models.ForeignKey(User,
                                                                              related_name='program_coordinator_or_principal_lecturer_user',
                                                                              blank=True, null=True,
                                                                              on_delete=models.DO_NOTHING)

    registrar_office = models.BooleanField(max_length=200, default=False, verbose_name='Registrar')
    registrar_office_comment = models.TextField(blank=True, null=True, verbose_name='Registrar Office Comment')
    registrar_office_user = models.ForeignKey(User, related_name='registrar_office_user', blank=True, null=True,
                                              on_delete=models.DO_NOTHING)

    temp_password = models.CharField('Temp Password', max_length=200, null=True, blank=True)
    balance_due = models.CharField('Balance Due', max_length=200, null=True, blank=True)
    intake = models.ForeignKey(Session, verbose_name='Intake', null=True, blank=True, max_length=200, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class SystemSettings(models.Model):
    student_no_last_digits_length = models.IntegerField('Last Digits Length',
                                                        help_text='The number of digits after the date on the student number: YYMMdigits',
                                                        blank=True, null=True)

    def __str__(self):
        return str(self.student_no_last_digits_length)

    class Meta:
        verbose_name_plural = 'System Settings'
