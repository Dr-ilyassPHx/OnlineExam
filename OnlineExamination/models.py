from django.db import models
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify

FRUIT_CHOICES= [
    ('form1', 'Form 1'),
    ('form2', 'Form 2'),
    ('form3', 'Form 3'),
    ('form4', 'Form 4'),
    ('lower6', 'Lower 6'),
    ('upper6', 'Upper 6'),
    ('professional', 'Professional'),
    ]

def upload_image(instance, filename):
    return "%s/%s" % (instance.user, filename)





class Student(models.Model):
    user = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number must be entered in the define format")
    phone = models.CharField(validators=[phone_regex], max_length=12)
    email = models.EmailField()
    national_ID = models.CharField(null=True, max_length=20, unique=True)
    study_level = models.CharField(null=True, max_length=20, choices=FRUIT_CHOICES)
    password = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    stream = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    mentor = models.ForeignKey('StudyMentor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user)

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/default.png"


class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    no_of_ques = models.CharField(max_length=20)
    total_marks = models.CharField(max_length=20)
    year = models.CharField(null=True, max_length=4)
    #time_duration = models.DurationField(default='00:00:00')

    def __str__(self):
        return str(self.exam_name)


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=30,null=True ,choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')))
    time_limitation = models.CharField(null=True, max_length=30)
    option1 = models.CharField(max_length=100)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)
    def __str__(self):
        return str(self.question)



class StudyMentor(models.Model):
    idmentor = models.AutoField(primary_key=True, unique=True)
    user = models.CharField(max_length=20, unique=True)
    FirstName = models.CharField(max_length=20, unique=True)
    LastName = models.CharField(max_length=20)
    phone_regexMentor = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Phone number must be entered in the define format")
    phone = models.CharField(validators=[phone_regexMentor], max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=20, default=1234)
    national_ID = models.CharField(null=True, max_length=20, unique=True)
    national_ID_image = models.ImageField(upload_to=upload_image, null=True, blank=True, height_field='height_field', width_field='width_field')
    address = models.CharField(max_length=200, blank=True)
    subject = models.TextField(max_length=500)
    #students = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idmentor)



class Staff(models.Model):
    idstaff = models.AutoField(primary_key=True, unique=True)
    user = models.CharField(max_length=20, unique=True)
    FirstName = models.CharField(max_length=20, unique=True)
    LastName = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20, default=1234)


    def __str__(self):
        return str(self.idmentor)

