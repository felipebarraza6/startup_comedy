# Django
from django.contrib import admin

# Register your models here.

# Models
from api.models import (User, Course, Video, Resource, QuestionCourse,
AlternativeQuestion, ResultContest, Test, QuestionTest,
AlternativeQuestionTest, AnswerTest, ResultTest, ProfileUser, PreRequisite,
AnswerQuestion, Module, Blog, Comment, ViewVideo)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email',)

@admin.register(ViewVideo)
class ViewVideo(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(PreRequisite)
class PreRequisiteAdmin(admin.ModelAdmin):
    list_display = ('course', 'pre_requisite',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'url',)

@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_re',)

@admin.register(QuestionCourse)
class QuestionCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title')

@admin.register(AlternativeQuestion)
class AlternativeQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title', 'is_correct')

@admin.register(ResultContest)
class ResultContestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(QuestionTest)
class QuestionTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'test')

@admin.register(AlternativeQuestionTest)
class AlternativeQuestionTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title','points',)

@admin.register(AnswerTest)
class AnswerTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer')

@admin.register(ResultTest)
class ResultTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'is_complete')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id",)
