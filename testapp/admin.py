from django.contrib import admin
from testapp.models import Choice, Question, User


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text', 'image']})]
    inlines = [ChoiceInline]
    search_fields = ['question_text']


class UserAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'user_fio', 'corr_ans')


admin.site.register(Question, QuestionAdmin)
admin.site.register(User, UserAdmin)
