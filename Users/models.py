"""
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from django.conf import settings
# MongoDB connection setup
from urllib.parse import quote_plus
# Your username and password
username = "wanjos"
password = "0903620Wanjos@#$"  # Special characters like @ must be escaped

# Escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)
MONGO_URI =f"mongodb+srv://{escaped_username}:{escaped_password}@newagedatabase.40ybp.mongodb.net/?retryWrites=true&w=majority&appName=newagedatabase"
client = MongoClient(MONGO_URI)
db = client['newagedatabase']

# User Collection
class User:
    collection = db['users']

    @staticmethod
    def create_user(data):
        data['date_joined'] = datetime.now()
        return User.collection.insert_one(data).inserted_id

    @staticmethod
    def find_user_by_id(user_id):
        return User.collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def find_user_by_username(username):
        return User.collection.find_one({"username": username})

# Available Courses Collection
class AvailableCourses:
    collection = db['available_courses']

    @staticmethod
    def add_course(data):
        return AvailableCourses.collection.insert_one(data).inserted_id

    @staticmethod
    def get_course(course_id):
        return AvailableCourses.collection.find_one({"_id": ObjectId(course_id)})

# Course Module Collection
class CourseModule:
    collection = db['course_modules']

    @staticmethod
    def add_module(data):
        return CourseModule.collection.insert_one(data).inserted_id

    @staticmethod
    def get_modules_by_course(course_id):
        return CourseModule.collection.find({"course_id": ObjectId(course_id)})

# Live Classes Collection
class LiveClass:
    collection = db['live_classes']

    @staticmethod
    def add_live_class(data):
        return LiveClass.collection.insert_one(data).inserted_id

# Student Attendance Collection
class StudentAttendance:
    collection = db['student_attendance']

    @staticmethod
    def mark_attendance(data):
        data['entry_time'] = datetime.now()
        return StudentAttendance.collection.insert_one(data).inserted_id

# Registered Courses for Students Collection
class RegisteredCourses:
    collection = db['registered_courses']

    @staticmethod
    def register_student(data):
        data['date'] = datetime.now()
        return RegisteredCourses.collection.insert_one(data).inserted_id

# Announcements Collection
class Announcement:
    collection = db['announcements']

    @staticmethod
    def create_announcement(data):
        data['date'] = datetime.now()
        return Announcement.collection.insert_one(data).inserted_id

# Assignments Collection
class Assignment:
    collection = db['assignments']

    @staticmethod
    def create_assignment(data):
        data['date'] = datetime.now()
        return Assignment.collection.insert_one(data).inserted_id

# Course Timetables Collection
class CourseTimetable:
    collection = db['course_timetables']

    @staticmethod
    def add_timetable(data):
        return CourseTimetable.collection.insert_one(data).inserted_id

# Exam Timetables Collection
class ExamTimetable:
    collection = db['exam_timetables']

    @staticmethod
    def add_exam(data):
        return ExamTimetable.collection.insert_one(data).inserted_id

# Transactions Collection
class Transaction:
    collection = db['transactions']

    @staticmethod
    def create_transaction(data):
        data['date_created'] = datetime.now()
        return Transaction.collection.insert_one(data).inserted_id

# Referrals Collection
class Referral:
    collection = db['referrals']

    @staticmethod
    def create_referral(data):
        data['create_at'] = datetime.now()
        return Referral.collection.insert_one(data).inserted_id

# Referral Tracker Collection
class ReferralTracker:
    collection = db['referral_trackers']

    @staticmethod
    def create_tracker(data):
        data['created_at'] = datetime.now()
        return ReferralTracker.collection.insert_one(data).inserted_id

# Promoted Courses Collection
class PromotedCourses:
    collection = db['promoted_courses']

    @staticmethod
    def promote_course(data):
        data['create_at'] = datetime.now()
        return PromotedCourses.collection.insert_one(data).inserted_id
"""