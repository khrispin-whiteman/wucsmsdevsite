from django import forms
from schoolapp.models import Admission, Program, User, School

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

APPLICATION_STATUS_CHOICES = (
    ('Pending', "Pending"),
    ('Verified', "Verified"),
    ('Approved', "Approved"),
    ('Rejected', "Rejected"),
)


class AddSchoolForm(forms.ModelForm):
    school_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter school name here',
            }
        ),
        label="School Name:",
    )

    description_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter school description here',
            }
        ),
        label="School Description:",
    )

    class Meta:
        model = School
        fields = ['school_name', 'school_description']


class AddDepartmentForm(forms.ModelForm):
    department_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter department name here',
            }
        ),
        label="Department Name:",
    )

    department_description = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter department description here',
            }
        ),
        label="Department Description:",
    )

    class Meta:
        model = School
        fields = ['department_name', 'department_description',]


class AddTeacherForm(forms.ModelForm):
    GENDER = (
        ("---------", "---------"),
        ('Male', "Male"),
        ('Female', "Female"),
    )

    USER_GROUPS = (
        ('Admissions Office', "Admissions Office"),
        ('Accounts Office', "Accounts Office"),
        ('Dean Of Students Affairs Office', "Dean Of Students Affairs Office"),
        ('ICT Office', "ICT Office"),
        ("Program Coordinator or Principal Lecturer Office", "Program Coordinator or Principal Lecturer Office"),
        ('Registrar Office', "Registrar Office"),
        ('Complete', "Complete"),
    )

    first_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter first name here',
            }
        ),
        label="First Name:",
    )

    last_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter last name here',
            }
        ),
        label="Last Name:",
    )

    phone = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter phone number here',
            }
        ),
        label="Phone Number",
    )

    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter a valid email here',
            }
        ),
        label="Email Address:",
    )

    gender = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=GENDER,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Gender',
            }
        ),
        label="Choose Your Gender Below",
    )

    user_group = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=USER_GROUPS,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'User Group',
            }
        ),
        label="Choose User Group Below",
    )

    username = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'User Name',
            }
        ),
        label="User Name",
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_member_of_staff', 'gender', 'user_group', 'phone', 'email']


class OnlineAdmissionForm(forms.ModelForm):
    GENDER = (
        ("---------", "---------"),
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
        ("---------", "---------"),
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
        ("---------", "---------"),
        ('Certificate', "Certificate"),
        ('Diploma', "Diploma"),
        ('Degree', "Degree"),
    )

    APPLICATION_STATUS_CHOICES = (
        ("---------", "---------"),
        ('Verified', "Verified"),
        ('Pending', "Pending"),
        ('Approved', "Approved"),
        ('Rejected', "Rejected"),
    )

    USER_GROUPS = (
        ("---------", "---------"),
        ('Admissions Office', "Admissions Office"),
        ('Accounts Office', "Accounts Office"),
        ('Dean Of Students Affairs Office', "Dean Of Students Affairs Office"),
        ('ICT Office', "ICT Office"),
        ("Program Coordinator or Principal Lecturer Office", "Program Coordinator or Principal Lecturer Office"),
        ('Registrar Office', "Registrar Office"),
        ('Complete', "Complete"),
    )
    #
    # subject = forms.CharField(
    #     # max_length=200,
    #     # widget=forms.TextInput(
    #     #     attrs={
    #     #         'type': 'text',
    #     #         'class': 'form-control',
    #     #         'placeholder': 'Subject or ticket summary',
    #     #     }
    #     # ),
    #     # label="Subject",
    #     max_length=200,
    #     widget=forms.Select(
    #         choices=SUBJECT_OPTIONS,
    #
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control',
    #             'placeholder': 'Subject',
    #         }
    #     ),
    #     label="Choose Ticket Subject/Type/Case Below",
    # )
    #

    # PART 1
    # PART 1
    first_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'first_name',
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter first name here',
            }
        ),
        label="First Name:",
    )
    last_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter last name here',
            }
        ),
        label="Last Name:",
    )
    other_names = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'optional',
            }
        ),
        label="Other Name:",
    )

    nrc_no = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter NRC number here',
            }
        ),
        label="NRC Number:",
    )

    phone_number = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter phone number here',
            }
        ),
        label="Phone Number",
    )

    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter a valid email here',
            }
        ),
        label="Email Address:",
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Date Of Birth',
            }
        ),
        label="Date Of Birth",
    )

    gender = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=GENDER,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Gender',
            }
        ),
        label="Choose Your Gender Below",
    )

    marital_status = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=MARITAL_STATUS,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Marital Status',
            }
        ),
        label="Choose Marital Status Below",
    )

    nationality = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=COUNTRIES,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Countries',
            }
        )
        ,
        label="Nationality",
    )

    physical_address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter your physical address here',
            }
        ),
        label="Physical Address",
    )

    postal_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter your postal address here',
            }
        ),
        label="Postal Address",
    )

    state_of_any_disabilities = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'optional',
            }
        ),
        label="State Disabilities If Any ",
    )

    # PART 2
    # PART 2
    sponsors_name_or_next_of_kin = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Sponsor’s Name Or Next of Kin:",
    )

    relationship_with_sponsor_or_next_of_kin = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Select(
            choices=RELATIONSHIP_WITH_GUARDIAN,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Choose Relationship With Sponsor Or Next of Kin Below:",
    )

    sponsor_or_next_of_kin_cell_no = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Sponsor Or Next of Kin Cell No:",
    )

    sponsor_or_next_of_kin_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Sponsor Or Next of Kin Address:",
    )

    # PART 3
    # PART 3
    program_applied_for = forms.ModelChoiceField(
        required=True,
        queryset=Program.objects.all(),
        label="Choose Program Of Choice Below",
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            })
    )

    school_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="High/Secondary School Name:",
    )

    school_start_year = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Start Year:",
    )

    school_end_year = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="End Year:",
    )

    has_certificate = forms.BooleanField(
        required=False,
        label="Certificate ",
    )

    has_diploma = forms.BooleanField(
        required=False,
        label="Diploma ",
    )

    has_degree = forms.BooleanField(
        required=False,
        label="Degree ",
    )


    # PART 3A
    # PART 3A
    subject_english = forms.IntegerField(
        required=False,
        widget = forms.NumberInput(
                attrs={
                    'style': 'width:6ch',
                    'oninput': 'limit_input()',
                    'class': 'form-control',
                }
            ),
               # widget=forms.TextInput(
        #     attrs={
        #         'type': 'text',
        #         'class': 'form-control',
        #         'placeholder': '',
        #     }
        # ),
        label="English:",
    )

    subject_mathematics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Mathematics:",
    )

    subject_biology_human_and_social = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Biology/Human & Social:",
    )

    subject_history = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="History:",
    )

    subject_religious_education = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Religious Education:",
    )

    subject_commerce = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Commerce:",
    )

    subject_home_economics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Home Economics:",
    )

    subject_geography = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Geography:",
    )

    subject_physical_science = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Physical Science:",
    )

    subject_chemistry = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Chemistry:",
    )

    subject_physics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Physics:",
        help_text='enter 0 if subject not taken'
    )

    subject_civic_education = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                    'style': 'width:6ch',
                    'oninput': 'limit_input()',
                    'class': 'form-control',
            }
        ),
        label="Civic Education:",
        help_text='enter 0 if subject not taken'
    )

    # application_status = forms.CharField(
    #     max_length=200,
    #     required=False,
    #     widget=forms.Select(
    #         choices=APPLICATION_STATUS_CHOICES,
    #
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control',
    #             'placeholder': 'application status',
    #         }
    #     ),
    #     label="Update Application Status Below:",
    # )


    # PART 3B
    # PART 3B
    scanned_deposit_slip = forms.FileField(
        label='Upload Scanned Deposit Slip:',
        required=True
    )

    scanned_nrc_front = forms.FileField(
        label='Upload Scanned National Registration Card (Front):',
        required=True
    )

    scanned_nrc_back = forms.FileField(
        label='Upload Scanned National Registration Card (Back):',
        required=True
    )

    scanned_statement_of_result = forms.FileField(
        label='Upload Scanned Grade 12 Results or equivalent of Results:',
        required=True
    )

    scanned_pq_certificate = forms.FileField(
        label='Upload Scanned Certificate (Optional):',
        required=False
    )

    scanned_pq_diploma = forms.FileField(
        label='Upload Scanned Diploma (Optional):',
        required=False
    )

    scanned_pq_degree = forms.FileField(
        label='Upload Scanned Degree (Optional):',
        required=False
    )


    # PART 4
    # PART 4
    declaration_confirmation = forms.BooleanField(
        required=True,
        label="I have read the declaration.",
    )



    #comment section
    admissions_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Admissions office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    accounts_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Accounts office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    dean_of_students_affairs_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Deans office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    ict_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'ICT office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    program_coordinator_or_principal_lecturer_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Program director office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    registrar_office_comment = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Registrars office comment',
                'rows': 4,
                'cols': 15,
            }
        ),
        label="Add Comment If Any Below:",
        help_text='enter comment here if any'
    )

    balance_due = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'K0.00',
            }
        ),
        label="Balance Due:",
        help_text='enter the balance here'
    )

    class Meta:
        model = Admission
        fields = ['first_name', 'last_name', 'other_names', 'nrc_no', 'phone_number', 'email', 'gender',
                  'date_of_birth',
                  'nationality', 'marital_status', 'physical_address', 'postal_address', 'state_of_any_disabilities',
                  'sponsors_name_or_next_of_kin', 'relationship_with_sponsor_or_next_of_kin', 'sponsor_or_next_of_kin_cell_no',
                  'sponsor_or_next_of_kin_address', 'program_applied_for', 'school_name',
                  'school_start_year', 'school_end_year', 'subject_english', 'subject_mathematics',
                  'subject_biology_human_and_social',
                  'subject_history', 'subject_religious_education', 'subject_commerce', 'subject_home_economics',
                  'subject_geography',
                  'subject_physical_science', 'subject_chemistry', 'subject_physics', 'subject_civic_education',
                  'has_certificate', 'has_diploma', 'has_degree', 'scanned_deposit_slip', 'scanned_nrc_front', 'scanned_nrc_back', 'scanned_statement_of_result',
                  'scanned_pq_certificate', 'scanned_pq_diploma', 'scanned_pq_degree', 'declaration_confirmation',
                  'temp_password', 'application_status',
                  'admissions_office_comment', 'accounts_office_comment', 'dean_of_students_affairs_office_comment',
                  'ict_office_comment', 'program_coordinator_or_principal_lecturer_office_comment', 'registrar_office_comment',
                  'balance_due']


class UpdateOnlineApplicationForm(forms.ModelForm):
    GENDER = (
        ("---------", "---------"),
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
        ('Other', "Other"),
    )

    RELATIONSHIP_WITH_GUARDIAN = (
        ("---------", "---------"),
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
        ('Complete', "Complete"),
    )
    #
    # subject = forms.CharField(
    #     # max_length=200,
    #     # widget=forms.TextInput(
    #     #     attrs={
    #     #         'type': 'text',
    #     #         'class': 'form-control',
    #     #         'placeholder': 'Subject or ticket summary',
    #     #     }
    #     # ),
    #     # label="Subject",
    #     max_length=200,
    #     widget=forms.Select(
    #         choices=SUBJECT_OPTIONS,
    #
    #         attrs={
    #             'type': 'text',
    #             'class': 'form-control',
    #             'placeholder': 'Subject',
    #         }
    #     ),
    #     label="Choose Ticket Subject/Type/Case Below",
    # )
    #

    # PART 1
    # PART 1
    first_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter first name here',
            }
        ),
        label="First Name:",
    )
    last_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter last name here',
            }
        ),
        label="Last Name:",
    )
    other_names = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter other names here',
            }
        ),
        label="Other Name:",
    )

    nrc_no = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter NRC number here',
            }
        ),
        label="NRC Number:",
    )

    phone_number = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter phone number here',
            }
        ),
        label="Phone Number",
    )

    email = forms.EmailField(
        max_length=200,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter a valid email here',
            }
        ),
        label="Email Address:",
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Date Of Birth',
            }
        ),
        label="Date Of Birth",
    )

    gender = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=GENDER,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Gender',
            }
        ),
        label="Choose Your Gender Below",
    )

    marital_status = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=MARITAL_STATUS,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Marital Status',
            }
        ),
        label="Choose Marital Status Below",
    )

    nationality = forms.CharField(
        max_length=200,
        widget=forms.Select(
            choices=COUNTRIES,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Countries',
            }
        )
        ,
        label="Nationality",
    )

    physical_address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter your physical address here',
            }
        ),
        label="Physical Address",
    )

    postal_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'optional',
            }
        ),
        label="Postal Address",
    )

    state_of_any_disabilities = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter any disability here',
            }
        ),
        label="State Disabilities If Any:",
    )

    # PART 2
    # PART 2
    sponsors_name_or_next_of_kin = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Sponsor’s Name Or Next of Kin:",
    )

    relationship_with_sponsor_or_next_of_kin = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Select(
            choices=RELATIONSHIP_WITH_GUARDIAN,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Choose Relationship With Sponsor Or Next of Kin Below:",
    )

    sponsor_or_next_of_kin_cell_no = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Sponsor Or Next of Kin Cell No:",
    )

    sponsor_or_next_of_kin_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'enter sponsor or next of kin address',
            }
        ),
        label="Sponsor Or Next of Kin Address:",
    )

    # PART 3
    # PART 3
    program_applied_for = forms.ModelChoiceField(
        required=False,
        queryset=Program.objects.all(),
        label="Choose Program Of Choice Below",
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            })
    )

    school_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="High/Secondary School Name:",
    )

    school_start_year = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Start Year:",
    )

    school_end_year = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="End Year:",
    )

    has_certificate = forms.BooleanField(
        required=False,
        label="Certificate ",
    )

    has_diploma = forms.BooleanField(
        required=False,
        label="Diploma ",
    )

    has_degree = forms.BooleanField(
        required=False,
        label="Degree ",
    )


    # PART 3A
    # PART 3A
    subject_english = forms.IntegerField(
        required=False,
        widget = forms.NumberInput(
                attrs={
                    'style': 'width:6ch',
                    'oninput': 'limit_input()',
                    'class': 'form-control',
                }
            ),
               # widget=forms.TextInput(
        #     attrs={
        #         'type': 'text',
        #         'class': 'form-control',
        #         'placeholder': '',
        #     }
        # ),
        label="English:",
    )

    subject_mathematics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Mathematics:",
    )

    subject_biology_human_and_social = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Biology/Human & Social:",
    )

    subject_history = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="History:",
    )

    subject_religious_education = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Religious Education:",
    )

    subject_commerce = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Commerce:",
    )

    subject_home_economics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Home Economics:",
    )

    subject_geography = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Geography:",
    )

    subject_physical_science = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Physical Science:",
    )

    subject_chemistry = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Chemistry:",
    )

    subject_physics = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width:6ch',
                'oninput': 'limit_input()',
                'class': 'form-control',
            }
        ),
        label="Physics:",
        help_text='enter 0 if subject not taken'
    )

    subject_civic_education = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                    'style': 'width:6ch',
                    'oninput': 'limit_input()',
                    'class': 'form-control',
            }
        ),
        label="Civic Education:",
        help_text='enter 0 if subject not taken'
    )

    application_status = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Select(
            choices=APPLICATION_STATUS_CHOICES,

            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'application status',
            }
        ),
        label="Update Application Status Below:",
    )


    # PART 3B
    # PART 3B
    scanned_deposit_slip = forms.FileField(
        label='Upload Scanned Deposit Slip:',
        required=True
    )

    scanned_nrc_front = forms.FileField(
        label='Upload Scanned National Registration Card (Front):',
        required=True
    )

    scanned_nrc_back = forms.FileField(
        label='Upload Scanned National Registration Card (Back):',
        required=True
    )

    scanned_statement_of_result = forms.FileField(
        label='Upload Scanned Grade 12 Results or equivalent of Results:',
        required=True
    )

    scanned_pq_certificate = forms.FileField(
        label='Upload Scanned Certificate (Optional):',
        required=False
    )

    scanned_pq_diploma = forms.FileField(
        label='Upload Scanned Diploma (Optional):',
        required=False
    )

    scanned_pq_degree = forms.FileField(
        label='Upload Scanned Degree (Optional):',
        required=False
    )


    # PART 4
    # PART 4
    declaration_confirmation = forms.BooleanField(
        required=True,
        label="I have read the declaration and agree.",
    )

    temp_password = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': '',
            }
        ),
        label="Temp Password:",
    )

    class Meta:
        model = Admission
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'other_names', 'nrc_no', 'phone_number', 'email', 'gender',
                  'date_of_birth',
                  'nationality', 'marital_status', 'physical_address', 'postal_address', 'state_of_any_disabilities',
                  'sponsors_name_or_next_of_kin', 'relationship_with_sponsor_or_next_of_kin', 'sponsor_or_next_of_kin_cell_no',
                  'sponsor_or_next_of_kin_address', 'program_applied_for', 'school_name',
                  'school_start_year', 'school_end_year', 'subject_english', 'subject_mathematics',
                  'subject_biology_human_and_social',
                  'subject_history', 'subject_religious_education', 'subject_commerce', 'subject_home_economics',
                  'subject_geography',
                  'subject_physical_science', 'subject_chemistry', 'subject_physics', 'subject_civic_education',
                  'has_certificate', 'has_diploma', 'has_degree', 'scanned_deposit_slip', 'scanned_nrc_front', 'scanned_nrc_back', 'scanned_statement_of_result',
                  'scanned_pq_certificate', 'scanned_pq_diploma', 'scanned_pq_degree', 'declaration_confirmation',
                  'temp_password']


