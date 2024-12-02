from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import secrets


def generate_referral_code():
    return str(uuid.uuid4())[:8]



#tutor register
class User(AbstractUser):
   
    first_name =models.CharField(max_length=50,null=True)
    last_name =models.CharField(max_length=50,null=True)
    username =models.CharField(max_length=50,null=True, unique =True)
    password = models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    is_tutor=models.BooleanField(verbose_name="Tutor Status",null=True,default=False,blank=True)
    is_student = models.BooleanField(verbose_name="Student Status",null=True,default=False,blank=True)
    is_affiliate = models.BooleanField(verbose_name="Affiliate Status",null=True,default=False,blank=True)
    is_superuser = models.BooleanField(verbose_name="Superuser Status",null=True,default=False,blank=True)
    is_active = models.BooleanField(verbose_name="Active Status",null=True,default=True,blank=True)
    is_staff = models.BooleanField(verbose_name="Staff Status",null=True,default=False,blank=True)
    last_login = models.DateTimeField(auto_now=True, null = True)
    date_joined = models.DateTimeField(auto_now_add=True, null = True)
    email = models.EmailField(max_length=255, null=True, unique=True)
    # referral_code = models.CharField(max_length=10, unique=True, default=generate_referral_code)
    #referrer = models.CharField(max_length=255,null=True )
    referer = models.CharField(max_length=255,null=True)

    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"

    def __str__(self):
        return self.username
    
   
    
   
    

    
## add courses
class available_Courses(models.Model):
    author = models.ForeignKey(User, related_name="tutoraddcourse",on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=30,null=True)
    slug=models.SlugField(max_length=20,null=True)

    class Meta:
        verbose_name="available_Courses"
        verbose_name_plural="available Courses"
        
    def __str__(self):
        return self.title
#add course module
class coursemodule(models.Model):
    course = models.ForeignKey(available_Courses, null=True, related_name="availablecoursemodules", on_delete=models.CASCADE)
    module = models.CharField(max_length=30,null=True)
    title = models.CharField(max_length=255, null=True, blank=True,unique=True)

    def __str__(self):
        return f'{self.module} {self.title}'



    
#tutor to add live classes

class liveclass(models.Model):
   #  course = models.ForeignKey(available_Courses, related_name="liveclasscourse",on_delete=models.CASCADE,null=True)
     class_name=models.ForeignKey(coursemodule, related_name="moduleliveclass",on_delete=models.CASCADE,null=True)
     class_description=models.TextField(max_length=1000,verbose_name="About the Live Class",null=True)
     class_link=models.CharField(max_length=255,unique=True,null=True,blank=False)
     def __str__(self):
         return f'{self.class_name}'
     
#student attendance 

class studentatten(models.Model):
    student_email=models.EmailField(max_length=100, unique=True,null=True, verbose_name ="Student Email") 
    course_code = models.ForeignKey(coursemodule, related_name="courseattendance",on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=10,choices=(('P','PRESENT'),('A','ABSENT')),default='PRESENT')
    entry_time = models.DateTimeField( null=True, auto_now_add = True, auto_now = False,blank=True)
    #student_name = models.ForeignKey(User, related_name="userattendance",on_delete=models.CASCADE,null=True)

    def __str__(self):
       return f"{self.course_code}  {self.student_email} "
    
    class Meta:
        verbose_name="studentattendance"
        verbose_name_plural="Student Attendance"
 
  

class registercoursestu(models.Model):
    course=models.ForeignKey(available_Courses, related_name="sturegcoursename",null=True, on_delete=models.CASCADE)
    email=models.CharField(max_length=50, null=True, unique=True)
    FirstName=models.CharField(max_length=50, null=True)
    LastName=models.CharField(max_length=50, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True, auto_now=False)
    def __str__(self):
        return f' {self.FirstName} {self.LastName} {self.course}'

#password reset 

    

class anouncement(models.Model):
    Tutor = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=255, null=True,unique=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f'{self.title} By {self.Tutor}'
    
#Tutor create assignment and class work
class CreateAssignment(models.Model):
    Tutor = models.CharField(max_length=20, null=True)
    course= models.ForeignKey(available_Courses, related_name="createassginmentcourse", null=True,on_delete=models.CASCADE)
    title =models.CharField(max_length=255, null=True,unique=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(null=True, auto_now=True)


    def __str__(self):
       return f'{self.title} assignment for {self.course}'
    
# add course timetable schedules

class coursetimetable(models.Model):
    course=models.ForeignKey(coursemodule, related_name="timetablecourse", null=True,on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    link = models.CharField(max_length=255,null=True)
      
    def __str__(self):
        return f'{self.course} {self.date}'

#add exam for courses
    
class examtimetable(models.Model):
    course=models.ForeignKey(coursemodule, related_name="timetableexam", null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    link = models.CharField(max_length=255,null=True)
      
    def __str__(self):
        return f'{self.course} {self.date}'


class Transaction(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    amount = models.PositiveIntegerField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference

#referal code for affiliate
"""  
class Referal (models. Model):
    user = models.ForeignKey(User, null=True, related_name="userreferal", on_delete = models.CASCADE)
    referal_code = models.CharField(max_length = 255, null =True, unique = True)
    referal_link = models.CharField(max_length=255, null=True,unique=True)
    create_at = models.DateTimeField(auto_now_add= True)
    referrer = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referred_users')
    def __str__(self):
        return self.referal_link
 
# referal tracker
class ReferralTracker(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referred_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referred_user.username} referred by {self.referrer.username}"
"""

class ReferralCode(models.Model):
    """
    Model for referral code.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=154, unique=True)

    def generate_code(self):
        username = self.user.username
        random_code = secrets.token_hex(2)
        return username+random_code

    def save(self, *args, **kwargs):
        self.code = self.generate_code()

        return super(ReferralCode, self).save(*args, **kwargs)


class Referral(models.Model):
    """
    For capturing who referred whom.
    """
    referred_by = models.ForeignKey(User, unique=False, on_delete=models.DO_NOTHING, related_query_name='my_referral')
    referred_to = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_query_name='has_referred')
    
class Wallet(models.Model):
    """
    Wallet to store affiliate's credits.
    """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    credits = models.FloatField(default=0.0)
#ended

class promotedcourses(models.Model):
   title = models.CharField(max_length=255,unique=True, null=True)
   user = models.ForeignKey(User, null=True, related_name="userpromotedcourse", on_delete = models.CASCADE)
   course = models.ForeignKey(available_Courses, null=True, related_name="coursepromotedcourse", on_delete = models.CASCADE)
   create_at = models.DateTimeField(auto_now_add= True,null=True)
   description = models.TextField(null = True)
   def __str__(self):
       return self.title
    




