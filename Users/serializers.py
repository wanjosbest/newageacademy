from rest_framework import serializers
import requests
from django.conf import settings
from .models import User,available_Courses,liveclass,studentatten,anouncement,CreateAssignment,coursetimetable,examtimetable,registercoursestu,coursemodule,promotedcourses
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .models import Referral, ReferralCode, Wallet
from .services import CreateReferral, SendReferral




class REGAPISerializer(serializers.ModelSerializer):
      class Meta:
            model= User
            fields= "__all__"
     
      def create(self, validated_data):
          user = super(REGAPISerializer, self).create(validated_data)
          user.set_password(validated_data['password'])
          user.save()
          return user
      """
      def create(self, validated_data):
        referral_code = validated_data.pop('referral_code', None)
        referrer = None
        if referral_code:
           user = User.objects.create_user(**validated_data, referrer=referral_code)
           user.save()
      """
class available_Courses_registrationserialization(serializers.ModelSerializer):
    class Meta:
        model=available_Courses
        fields=("id","title","slug","author",)

class coursemoduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = coursemodule
        fields = "__all__"


class liveclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = liveclass
        fields = ("class_name","class_description","class_link",)

# student attendance

class studentattendanceSerializer(serializers.ModelSerializer):
      class Meta:
          model =studentatten
          fields =("student_email","course_code","status",)


class ChangePasswordSerializer(serializers.Serializer):
      old_password = serializers.CharField(required=True)
      new_password = serializers.CharField(required=True)

#Reset password 



#student register course

class sturegistercourseSerializer(serializers.ModelSerializer):
      class Meta:
          model =registercoursestu
          fields =("course",)


#tutor and admin add anouncements
class anouncementSerializer(serializers.ModelSerializer):
      class Meta:
          model =anouncement
          fields =("id","title","content",)

#tutor create assignment and class work
class CreateAssignmentSerializer(serializers.ModelSerializer):
      class Meta:
          model =CreateAssignment
          fields =("id","title","content","course")


#tutor and admin add class timetable

class coursetableSerializer(serializers.ModelSerializer):
      class Meta:
          model = coursetimetable
          fields = ("id","course","date","time","link",)

#exams timetable
class examtableSerializer(serializers.ModelSerializer):
      class Meta:
          model = examtimetable
          fields = ("id","title","course","date","time","link",)
"""
class ReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Referal
        fields = ("id","user","referal_code","create_at","referal_link","referrer",)
"""    
# affilate referal section
class UserSerializer(serializers.ModelSerializer):
    referral_code = serializers.CharField(max_length=154, write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'referral_code']
        extra_kwargs = {'password':{'write_only':True}}
   
    def create(self, validated_data):
        """
        Creates a new user with/without referral code.
        """
        referral_code = ''
        referred_by = ''
        if validated_data.get('referral_code'):
            referral_code = validated_data.pop('referral_code')
            try:
                referred_by = ReferralCode.objects.get(code=referral_code).user
            except ObjectDoesNotExist:
                pass
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        if referred_by:
            referral = CreateReferral(referred_by=referred_by, referred_to=user)
            referral.new_referral()
            for value in (referred_by, user):
                wallet = Wallet.objects.get(user=value)
                wallet.credits += 100
                wallet.save()
        return user


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['credits']


class ReferralCodeSerializer(serializers.ModelSerializer):
    to_email = serializers.EmailField(write_only=True)

    class Meta:
        model = ReferralCode
        fields = ['code', 'to_email']
        extra_kwargs = {'code':{'read_only':True}}

    def create(self, validated_data):
        to_email = validated_data.get('to_email')
        current_user =  self.context['request'].user
        code = ReferralCode.objects.get(user=current_user).code
        sendReferral = SendReferral(mail_id=to_email, referral_code=code)
        sendReferral.send_referral_mail()
        return validated_data
#affiliate promoted courses

class promotedcoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = promotedcourses
        fields = ("id","title","description","user","course","create_at",)
    
