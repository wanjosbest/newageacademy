from django.db import models
from django.contrib.auth.models import AbstractUser

"""
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
    referer = models.CharField(max_length=255,null=True,blank=True)
    

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

    def __str__ (self):
        return self.reference

#referal code for affiliate
class Referral (models. Model):
    user = models.ForeignKey(User, null=True, related_name="userreferal", on_delete = models.CASCADE)
    referal_code = models.CharField(max_length = 255, null =True, unique = True)
    create_at = models.DateTimeField(auto_now_add= True)
    
    def __str__ (self):
        return self.referal_code
 
# referal tracker
class ReferralTracker(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referred_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referred_user.username} referred by {self.referrer.username}"




class promotedcourses(models.Model):
   title = models.CharField(max_length=255,unique=True, null=True)
   user = models.ForeignKey(User, null=True, related_name="userpromotedcourse", on_delete = models.CASCADE)
   course = models.ForeignKey(available_Courses, null=True, related_name="coursepromotedcourse", on_delete = models.CASCADE)
   create_at = models.DateTimeField(auto_now_add= True,null=True)
   description = models.TextField(null = True)
   def __str__(self):
       return self.title
    
"""
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['education_platform']

# Users collection
users_collection = db['users']
available_courses_collection = db['available_courses']
course_modules_collection = db['course_modules']
live_classes_collection = db['live_classes']
student_attendance_collection = db['student_attendance']
registered_courses_collection = db['registered_courses']
announcements_collection = db['announcements']
assignments_collection = db['assignments']
course_timetables_collection = db['course_timetables']
exam_timetables_collection = db['exam_timetables']
transactions_collection = db['transactions']
referrals_collection = db['referrals']
referral_trackers_collection = db['referral_trackers']
promoted_courses_collection = db['promoted_courses']

# Example: Inserting data into collections
# Users
def insert_user(data):
    users_collection.insert_one({
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "username": data.get("username"),
        "password": data.get("password"),
        "address": data.get("address"),
        "is_tutor": data.get("is_tutor", False),
        "is_student": data.get("is_student", False),
        "is_affiliate": data.get("is_affiliate", False),
        "is_superuser": data.get("is_superuser", False),
        "is_active": data.get("is_active", True),
        "is_staff": data.get("is_staff", False),
        "last_login": datetime.now(),
        "date_joined": datetime.now(),
        "email": data.get("email"),
        "referer": data.get("referer")
    })

# Available Courses
def insert_course(data):
    available_courses_collection.insert_one({
        "author_id": data.get("author_id"),
        "title": data.get("title"),
        "slug": data.get("slug")
    })

# Course Modules
def insert_course_module(data):
    course_modules_collection.insert_one({
        "course_id": data.get("course_id"),
        "module": data.get("module"),
        "title": data.get("title")
    })

# Live Classes
def insert_live_class(data):
    live_classes_collection.insert_one({
        "class_name_id": data.get("class_name_id"),
        "class_description": data.get("class_description"),
        "class_link": data.get("class_link")
    })

# Student Attendance
def insert_student_attendance(data):
    student_attendance_collection.insert_one({
        "student_email": data.get("student_email"),
        "course_code_id": data.get("course_code_id"),
        "status": data.get("status", "PRESENT"),
        "entry_time": datetime.now()
    })

# Registered Courses
def insert_registered_course(data):
    registered_courses_collection.insert_one({
        "course_id": data.get("course_id"),
        "email": data.get("email"),
        "FirstName": data.get("FirstName"),
        "LastName": data.get("LastName"),
        "date": datetime.now()
    })

# Announcements
def insert_announcement(data):
    announcements_collection.insert_one({
        "Tutor": data.get("Tutor"),
        "title": data.get("title"),
        "content": data.get("content"),
        "date": datetime.now()
    })

# Assignments
def insert_assignment(data):
    assignments_collection.insert_one({
        "Tutor": data.get("Tutor"),
        "course_id": data.get("course_id"),
        "title": data.get("title"),
        "content": data.get("content"),
        "date": datetime.now()
    })

# Course Timetables
def insert_course_timetable(data):
    course_timetables_collection.insert_one({
        "course_id": data.get("course_id"),
        "date": data.get("date"),
        "time": data.get("time"),
        "link": data.get("link")
    })

# Exam Timetables
def insert_exam_timetable(data):
    exam_timetables_collection.insert_one({
        "course_id": data.get("course_id"),
        "title": data.get("title"),
        "date": data.get("date"),
        "time": data.get("time"),
        "link": data.get("link")
    })

# Transactions
def insert_transaction(data):
    transactions_collection.insert_one({
        "reference": data.get("reference"),
        "email": data.get("email"),
        "amount": data.get("amount"),
        "verified": data.get("verified", False),
        "date_created": datetime.now()
    })

# Referrals
def insert_referral(data):
    referrals_collection.insert_one({
        "user_id": data.get("user_id"),
        "referal_code": data.get("referal_code"),
        "created_at": datetime.now()
    })

# Referral Tracker
def insert_referral_tracker(data):
    referral_trackers_collection.insert_one({
        "referrer_id": data.get("referrer_id"),
        "referred_user_id": data.get("referred_user_id"),
        "created_at": datetime.now()
    })

# Promoted Courses
def insert_promoted_course(data):
    promoted_courses_collection.insert_one({
        "title": data.get("title"),
        "user_id": data.get("user_id"),
        "course_id": data.get("course_id"),
        "created_at": datetime.now(),
        "description": data.get("description")
    })
