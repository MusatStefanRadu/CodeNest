from django.contrib import admin
from .models import (
    CustomUser, Category, Course, CourseEnrollment, 
    Review, Test, Question, Answer
)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'ranking_position', 'XP', 'email_confirm', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('email_confirm', 'ranking_position', 'is_staff', 'is_superuser')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'price', 'is_free')
    list_filter = ('difficulty', 'is_free', 'category')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'purchase_date', 'status', 'completion_date', 'payment_method')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'course__title')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'posted_date')
    list_filter = ('rating',)
    search_fields = ('user__username', 'course__title')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'number_of_questions')
    list_filter = ('difficulty', 'category')
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'test', 'points')
    search_fields = ('text',)
    list_filter = ('test',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_label', 'text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text', 'question__text')
