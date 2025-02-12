

from django.shortcuts import render,HttpResponse,get_object_or_404
import os
import requests
from django.template.loader import render_to_string
from rest_framework import generics
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views
#from .serializers import (REGAPISerializer,available_Courses_registrationserialization,liveclassSerializer,
#                          studentattendanceSerializer,anouncementSerializer,CreateAssignmentSerializer,
 #                         ChangePasswordSerializer,coursetableSerializer,examtableSerializer,
 ####                         sturegistercourseSerializer,coursemoduleSerializer,promotedcoursesSerializer,
 #                         ReferalSerializer
 #                        )

from rest_framework import status
from rest_framework.response import Response
from  rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
#from .models import (User,available_Courses,studentatten,anouncement,CreateAssignment,User,available_Courses,
#                     studentatten,coursetimetable,examtimetable,registercoursestu,coursemodule,promotedcourses,
#                     Referral
#)
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import update_session_auth_hash
from rest_framework.generics import GenericAPIView
from django.utils.encoding import force_str
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.forms import PasswordResetForm
from rest_framework.views import APIView
from academy.settings import EMAIL_HOST_USER
from django.core.mail import  send_mail,BadHeaderError
from .paystack import Paystack


"""
#Admin CRUD USers
#admin create user
@csrf_protect
@api_view(["POST"])
def tutor_register(request):
    if request.method=="POST":
       serializer=REGAPISerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#authenticated users to view users
@csrf_protect
@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def gettutor(request):
    if request.user.is_authenticated:
      post=User.objects.all()
      if request.method=="GET":
        serializer=REGAPISerializer(post, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED) 
# only admin can update users
@api_view(["PUT"])
@csrf_protect

#@permission_classes([IsAdminUser])
def update_tutor(request,id):
    post=User.objects.get(id=id)
    if request.user.is_superuser:
        if request.method=="PUT":
            serializer=REGAPISerializer(post,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response( status=status.HTTP_401_UNAUTHORIZED)
@permission_classes([IsAdminUser])
def update_tutor(request,id):
    post=User.objects.get(id=id)
    if request.method=="PUT":
         serializer=REGAPISerializer(post,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#only admin can delete users
@csrf_protect
@api_view(["DELETE"])
#@permission_classes([IsAdminUser])
def delete_tutor(request,id):
      if request.user.is_superuser:
        post=User.objects.get(id=id)
        if request.method=="DELETE":
          post.delete()
          return Response(status = status.HTTP_204_NO_CONTENT)
      return Response(status = status.HTTP_401_UNAUTHORIZED)


#userlogin
@csrf_protect
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        #serializer=REGAPISerializer(data=request.data)
        user = None
       
        if not user:
            user = authenticate(username=username, password=password)
        if user:
           login(request, user)
        if user.is_authenticated:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK,)
    return Response( status=status.HTTP_401_UNAUTHORIZED)
 

     
#admin login
@csrf_protect
@api_view(['POST'])
def admin_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if not user:
            user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
        else:
            return Response( status=status.HTTP_401_UNAUTHORIZED)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
#admin logout

@api_view(['POST'])
@csrf_protect
def admin_logout(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            logout(request)
            return Response( status = status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status = status.HTTP_403_FORBIDDEN)

      

    #user logout

@api_view(['POST'])
@csrf_protect
def user_logout(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            logout(request)
            return Response( status = status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status = status.HTTP_403_FORBIDDEN)


###course CRUD BY ADMIN
@csrf_protect
@api_view(["POST"])
#@permission_classes([IsAdminUser])
def addCourses(request):
    if request.user.is_superuser:
        if request.method=="POST":
         serializer=available_Courses_registrationserialization(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)


@csrf_protect
@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def getCourses(request):
    #if request.user.is_authenticated:
      post=available_Courses.objects.all()
      if request.method=="GET":
        serializer=available_Courses_registrationserialization(post, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
   # return Response(status = status.HTTP_401_UNAUTHORIZED) 

@csrf_protect   
@api_view(["PUT"])
#@permission_classes([IsAdminUser])
def updateCourses(request,id):
    if request.user.is_superuser:
       post=available_Courses.objects.get(id=id)
       if request.method=="PUT":
         serializer=available_Courses_registrationserialization(post,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
        

@csrf_protect
@api_view(["DELETE"])
#@permission_classes([IsAdminUser])
def deleteCourses(request,id):
    if request.user.is_superuser:
      post=available_Courses.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_204_NO_CONTENT)
    return Response(status = status.HTTP_401_UNAUTHORIZED)


#add course modules
@csrf_protect
@api_view(["POST"])
#@permission_classes([IsAdminUser])
def addCoursemodule(request):
    if request.user.is_superuser:
        if request.method=="POST":
         serializer=coursemoduleSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#view course modules
@csrf_protect
@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def getCoursemodule(request):
    if request.user.is_authenticated:
      post=coursemodule.objects.all()
      if request.method=="GET":
        serializer=coursemoduleSerializer(post, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED)

#update course module

@csrf_protect   
@api_view(["PUT"])
#@permission_classes([IsAdminUser])
def updateCoursemodule(request,id):
    if request.user.is_superuser:
       post=coursemodule.objects.get(id=id)
       if request.method=="PUT":
         serializer=coursemoduleSerializer(post,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

#delete course module
@csrf_protect
@api_view(["DELETE"])
#@permission_classes([IsAdminUser])
def deleteCoursemodule(request,id):
    if request.user.is_superuser:
      post=coursemodule.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_204_NO_CONTENT)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
   

    
# admin allow only tutor to add live class posts
@csrf_protect
@api_view(["POST"])
def tutorliveclasspost(request):
    if request.user.is_tutor: 
       if request.method =="POST":
          serializer = liveclassSerializer(data = request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(status = status.HTTP_401_UNAUTHORIZED)

# storing student attendance

@csrf_protect   
@api_view(["POST"])
#@permission_classes([IsAdminUser])
def atten(request):
    if request.user.is_student:
       course = request.data.get("course_code")
       student_email = request.user.email
      
       if request.user:
          if request.method=="POST":
             saveattendance=studentatten.objects.create(course_code_id=course,student_email=student_email)
             serializer = studentattendanceSerializer(data = request.data)
             saveattendance.save()
             return Response( status = status.HTTP_201_CREATED)
       return Response(status = status.HTTP_401_UNAUTHORIZED)        
    return Response(status = status.HTTP_401_UNAUTHORIZED)


#tutor change password
@api_view(['POST'])
def change_password(request):
    if request.user.is_authenticated:
       if request.method == 'POST':
          serializer = ChangePasswordSerializer(data=request.data)
          if serializer.is_valid():
             user = request.user
             if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
          return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response ( status = status.HTTP_401_UNAUTHORIZED)


#student register courses
#create
@api_view(["POST"])
def registercourse(request):
    if request.user.is_student:
       if request.method=="POST":
          course_id = request.data.get("course")
          email = request.user.email
          firstname = request.user.first_name
          lastname = request.user.last_name
          serializers = sturegistercourseSerializer(data = request.data)
          if serializers.is_valid():
             savecourse = registercoursestu.objects.create(course_id=course_id,email=email, FirstName=firstname, LastName=lastname)
             savecourse.save()
             return Response({"Course registered"}, status= status.HTTP_201_CREATED)
       return Response( status= status.HTTP_400_BAD_REQUEST)
    return Response( status= status.HTTP_401_UNAUTHORIZED)


          
#admin and tutor CRUD anouncement

@api_view(["POST"])
def createanouncement(request):
    if request.user.is_tutor or request.user.is_superuser:
       if request.method=="POST":
          title= request.data.get("title")
          content = request.data.get("content")
          Tutor = request.user.username
          serializers = anouncementSerializer(data = request.data)
          if serializers.is_valid():
            saveanouncement= anouncement.objects.create(title=title,content=content,Tutor=Tutor)
            saveanouncement.save()
            return Response({"Anouncement created"}, status= status.HTTP_201_CREATED)
       return Response( status= status.HTTP_400_BAD_REQUEST)
    return Response( status= status.HTTP_401_UNAUTHORIZED)

#delete
@csrf_protect
@api_view(["DELETE"])
def deleteanouncement(request,id):
    if request.user.is_superuser:
      post=anouncement.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_204_NO_CONTENT)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#view anouncement
@csrf_protect
@api_view(["GET"])
def viewanouncement(request):
    if request.user.is_authenticated:
      post=anouncement.objects.all()
      if request.method=="GET":
        serializer=anouncementSerializer(post, many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED) 

#update anouncement
@csrf_protect   
@api_view(["PUT"])
#@permission_classes([IsAdminUser])
def updateanouncement(request,id):
    if request.user.is_superuser or request.user.is_tutor:
       post=anouncement.objects.get(id=id)
       if request.method=="PUT":
         serializer=anouncementSerializer(post,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#end of anouncement CRUD

#tutor create assignments and class works

@api_view(["POST"])
def createassignment(request):
    if request.user.is_tutor:
       if request.method=="POST":
          title= request.data.get("title")
          content = request.data.get("content")
          course = request.data.get("course")
          Tutor = request.user.username
          serializers = CreateAssignmentSerializer(data = request.data)
          if serializers.is_valid():
             saveassignment= CreateAssignment.objects.create(title=title,content=content,Tutor=Tutor,course_id=course)
             saveassignment.save()
             return Response({"assignment created"}, status= status.HTTP_201_CREATED)
       return Response( status= status.HTTP_400_BAD_REQUEST)
    return Response( status= status.HTTP_401_UNAUTHORIZED)

#delete
@csrf_protect
@api_view(["DELETE"])
def deleteassignment(request,id):
    if request.user.is_superuser or request.is_tutor:
      post=CreateAssignment.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#view assignment or class work
@csrf_protect
@api_view(["GET"])
def viewassignment(request):
    if request.user.is_authenticated:
      post=CreateAssignment.objects.all()
      if request.method=="GET":
         serializer=CreateAssignmentSerializer(post, many=True)
         return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED) 

#update assignment
@csrf_protect   
@api_view(["PUT"])
def updateassignment(request,id):
    if request.user.is_superuser or request.user.is_tutor:
       post=CreateAssignment.objects.get(id=id)
       if request.method=="PUT":
          serializer=CreateAssignmentSerializer(post,data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#end of assignment and class work CRUD

# tutor and admin add class time table
#add schedule
@api_view(["POST"])
@csrf_protect
def addclassschedule(request):
    if request.user.is_superuser or request.is_tutor:
       if request.method =="POST":
          serializer = coursetableSerializer(data = request.data)
          if serializer.is_valid():
             serializer.save()
             return Response ( status = status.HTTP_201_CREATED)
       return Response ( status= status.HTTP_400_BAD_REQUEST)
    return Response ( status = status.HTTP_401_UNAUTHORIZED)
   
#update schedule
@csrf_protect   
@api_view(["PUT"])
def updateclassschedule(request,id):
    if request.user.is_superuser or request.user.is_tutor:
       post=coursetimetable.objects.get(id=id)
       if request.method=="PUT":
          serializer=coursetableSerializer(post,data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)

#view schedule
@csrf_protect
@api_view(["GET"])
def viewclassschedule(request):
    if request.user.is_authenticated:
      post=coursetimetable.objects.all()
      if request.method=="GET":
         serializer=coursetableSerializer(post, many=True)
         return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED) 
#delete schedule
@csrf_protect
@api_view(["DELETE"])
def deleteclassschedule(request,id):
    if request.user.is_superuser or request.is_tutor:
      post=coursetimetable.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_401_UNAUTHORIZED)


#tutor and admin CRUD exam timetable
@api_view(["POST"])
@csrf_protect
def createtimetable(request):
   if request.user.is_tutor:
      if request.method=="POST":
         serializer = examtableSerializer( data = request.data)
         if serializer.is_valid():
            serializer.save()
            return Response( status = status.HTTP_201_CREATED)
      return Response( status = status.HTTP_400_BAD_REQUEST)
   return Response( status = status.HTTP_401_UNAUTHORIZED)
#update exams timetable
@csrf_protect   
@api_view(["PUT"])
def updateexamtimetable(request,id):
    if request.user.is_superuser or request.user.is_tutor:
       post=examtimetable.objects.get(id=id)
       if request.method=="PUT":
          serializer=examtableSerializer(post,data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
# view examtimetable
@csrf_protect
@api_view(["GET"])
def viewexamtimetable(request):
    if request.user.is_authenticated:
      post=examtimetable.objects.all()
      if request.method=="GET":
         serializer=examtableSerializer(post, many=True)
         return Response(serializer.data,status=status.HTTP_302_FOUND)
    return Response(status = status.HTTP_401_UNAUTHORIZED)
#delete exams timetable
@csrf_protect
@api_view(["DELETE"])
def deleteexamtimetable(request,id):
    if request.user.is_superuser or request.is_tutor:
      post=examtimetable.objects.get(id=id)
      if request.method=="DELETE":
         post.delete()
         return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_401_UNAUTHORIZED)

#paystack payment processing
class PaystackInitPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        email = request.user.email
        if email:   
           paystack = Paystack()
           response = paystack.initialize_payment(email, amount)
           if response and response.get('status'):
              return Response(response['data'], status=status.HTTP_200_OK)
        return Response({"error": "Please use registered email"}, status=status.HTTP_401_UNAUTHORIZED)

#verify payment
class PaystackVerifyPaymentView(APIView):
    def get(self, request, *args, **kwargs):
        reference = request.query_params.get("reference")
        if not reference:
            return Response({"error": "Reference is required"}, status=status.HTTP_400_BAD_REQUEST)

        paystack = Paystack()
        response = paystack.verify_payment(reference)
        if response and response.get('status'):
            data = response['data']
            # You can save the transaction details or mark it as verified
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)

#webhook
class PaystackWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        payload = request.data
        event = payload.get("event")
        if event == "charge.success":
            # Process successful payment
            print("Payment verified:", payload)
        return Response(status=status.HTTP_200_OK)
    
    
    # generate referal code

class ReferalView(APIView):
      def post(self, request):
          if request.user.is_affiliate:
             user = request.user
             try:
                 referal =Referral.objects.get (user = user)
                 serializer = ReferalSerializer(referal)
                 return Response(serializer.data, status = status.HTTP_201_CREATED)
             except Referral.DoesNotExist:
                referal_code = request.user.username
                referal = Referral.objects.create(user = user, referal_code = referal_code)
                serializer = ReferalSerializer(referal)
                return Response(serializer.data, status = status.HTTP_201_CREATED)
          return Response( status = status.HTTP_401_UNAUTHORIZED)
    
       
      
         
#affiliate promoted course view

class promotedcourseView(APIView):
    
    def post(self,request):
        if request.user.is_affiliate:
           user = request.user
           course = request.data.get("course")
           description = request.data.get("description")
           title = request.data.get("title")
           savepromoted = promotedcourses.objects.create(user = user, course_id = course,title = title, description = description)
           savepromoted.save()
           serializer = promotedcoursesSerializer(savepromoted)
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response( status = status.HTTP_401_UNAUTHORIZED)
    
#referal count
@api_view(["GET"])
@csrf_protect
def refferalcount(request):
    if request.user.is_affiliate:
       userrefferal = User.objects.filter(referer =f"{request.user.username}")
       totalrefferals = userrefferal.count()
       initialprice = 1000
       totalprice = totalrefferals * initialprice
       return Response (f" your total referals is:{totalrefferals} and your total earning is: N{totalprice}")
    return Response( status = status.HTTP_401_UNAUTHORIZED)

"""
from django.shortcuts import render, redirect
from .mongo import users_collection
from .forms import UserForm
from pymongo import MongoClient

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Insert new user into MongoDB
            user_data = form.cleaned_data
            users_collection.insert_one(user_data)
            return redirect('create-user')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def index(request):
    return render(request, "user_form.html")



   