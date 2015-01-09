FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
Master = 'M'
Doctor = 'PHD' 

YEAR_IN_SCHOOL_CHOICES = (
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
    (Master, 'Master'),
    (Doctor, 'Doctor'),
)

# gender : true: man; false: woman; 
GENDER = (
    (True, 'man'),
    (False, 'woman'),
)

#country:
COUNTRY_CHOICES = (
    ('FR', 'France'),
    ('EN', 'United kingdom'),
    ('AU', 'Australia'),
    ('CA', 'Canada'),
    ('CH', 'Switzerland'),
    ('DE', 'Germany'),
    ('ES', 'Spain'),
    ('KR', 'Korea'),
    ('SG', 'Singapore'),
    ('JP', 'Japan'),
    ('IT', 'Italy'),
    ('US', 'United States'),
)

COUNTRY_NAME = {
    'FR' : 'France',
    'EN' : 'United kingdom',
    'AU' : 'Australia',
    'CA' : 'Canada',
    'CH' : 'Switzerland',
    'CN' : 'China',
    'DE' : 'Germany',
    'ES' : 'Spain',
    'KR' : 'Korea',
    'SG' : 'Singapore',
    'JP' : 'Japan',
    'IT' : 'Italy',
    'US' : 'United States',
}


LIST_COUNTRY_EUROPE = ['EN', 'FR', 'CH', 'DE','ES', 'IT']
LIST_COUNTRY_ASIA = ['JP', 'KR', 'SG']
LIST_COUNTRY_AMERICAN = ['US', 'CA']
LIST_COUNTRY = {
    'europe' : LIST_COUNTRY_EUROPE,
    'asia' : LIST_COUNTRY_ASIA,
    'american' : LIST_COUNTRY_AMERICAN,
    'australia' : ['AU'],
}

