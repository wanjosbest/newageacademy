from django.urls import path
from .import views
from Users.views import  PaystackInitPaymentView,PaystackVerifyPaymentView,PaystackWebhookView,promotedcourseView

urlpatterns =[
    
     path("api/admin-login/",views.admin_login, name="admin_login"),
     path("api/admin-logout/",views.admin_logout, name="admin_logout"),
     path("api/user-login/",views.user_login, name="user_login"),
     path('api/paystack/initialize/', PaystackInitPaymentView.as_view(), name='paystack-initialize'),
     path('api/paystack/verify/<str:reference>/', PaystackVerifyPaymentView.as_view(), name='paystack-verify'),
     path('api/paystack/webhook/', PaystackWebhookView.as_view(), name='paystack-webhook'),
     path("api/user-logout/",views.user_logout, name="user-logout"),
     #ADMIN CRUD Tutor
     path("api/tutor-register/",views.tutor_register, name="tutor_register"),
     path("api/get-tutor/",views.gettutor, name="view_tutor"),
     path("api/update-tutor/<str:id>/",views.update_tutor, name="update_user"),
     path("api/delete-tutor/<str:id>/",views.delete_tutor, name="delete_user"),
     #admin CRUD courses
     path("api/addcourse/",views.addCourses, name="addcourse"),
     path("api/getcourse/",views.getCourses, name="getcourse"),
     path("api/updatecourse/<str:id>/",views.updateCourses, name="updatecourse"),
     path("api/deletecourse/<str:id>/",views.deleteCourses, name="deletecourse"),
      #admin CRUD course modules
     path("api/addcourse-module/",views.addCoursemodule, name="addcoursemodule"),
     path("api/getcourse-module/",views.getCoursemodule, name="getcoursemodule"),
     path("api/updatecourse-module/<str:id>/",views.updateCoursemodule, name="updatecoursemodule"),
     path("api/deletecourse-module/<str:id>/",views.deleteCoursemodule, name="deletecoursemodule"),
     #end ADMIN CRUD

     # allow only tutor to add live class
     path("api/addliveclasspost/", views.tutorliveclasspost, name = "tutorliveclass"),

     # attendance
     path("api/student-attendance/",views.atten, name="studentattendance"),
     # password change
     path('api/change-password/', views.change_password, name='change_password'),

     # forgort password 
     # path("api/forgot-password/", views.reset_request, name="forgot_password"),
     #reset
     #path("api/reset-password/", views.reset_password, name="reset_password"),
     #student register course
     path("api/register-course/", views.registercourse, name="registercourse"),
     #tutor and admin CRUD anouncements
     path("api/create-anouncement/", views.createanouncement, name="createanouncement"),
     path("api/delete-anouncement/<str:id>/", views.deleteanouncement, name="deleteanouncement"),
     path("api/view-anouncement/", views.viewanouncement, name="viewanouncement"),
     path("api/update-anouncement/<str:id>/", views.updateanouncement, name="updateanouncement"),
     # tutor & Admin CRUD assignment
     path("api/create-assignment/", views.createassignment, name="createassignment"),
     path("api/delete-assignment/<str:id>/", views.deleteassignment, name="deleteassignment"),
     path("api/view-assignment/", views.viewassignment, name="viewassignment"),
     path("api/update-assignment/<str:id>/", views.updateassignment, name="updateassignment"),

     # CRUD class schedule

     path("api/create-schedule/",views.addclassschedule, name="addclassschedule"),
     path("api/update-schedule/<str:id>/", views.updateclassschedule, name="updateshedule"),
     path("api/delete-schedule/<str:id>/", views.deleteclassschedule, name="deleteschedule"),
     path("api/view-schedule/", views.viewclassschedule, name="viewschedule"),

     #CRUD exam timetable
     path("api/create-examtimetable/",views.createtimetable, name="createtimetable"),
     path("api/update-examtimetable/<str:id>/", views.updateexamtimetable, name="updateexamtimetable"),
     path("api/delete-examtimetable/<str:id>/", views.deleteexamtimetable, name="deleteexamtimetable"),
     path("api/view-examtimetable/", views.viewexamtimetable, name="viewexamtimetable"),
     # referal code
     path("api/referral/", views.ReferalView.as_view(), name="referral"),
     path("api/promote-course/", views.promotedcourseView.as_view(), name="promotedcourse"),
     # register user with referal link
     # path("api/register-user/",views.referalregister, name="register-user"),
     path("api/getrefferalsdetails/", views.refferalcount, name = "referalcount"),
     
     
       

]