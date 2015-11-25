from django.contrib import admin
from .models import Category, Question, Choice
# Register your models here.
#CategoryAdmin, QuestionAdmin, ChoiceAdmin are for forms filling and Choice, Category, Question are tables  
class CategoryAdmin(admin.ModelAdmin):
	fields = ['category_name']
	list_display = ('id','category_name')
admin.site.register(Category, CategoryAdmin)

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['category']}), ('Question information',{'fields':['question_text','correct_choice','marks']}),('Author information', {'fields':['author']})]
    inlines = [ChoiceInline]
    list_display = ('id','category','question_text','correct_choice', 'pub_date', 'author','was_published_recently')
    list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
	fields = ['question', 'choice_text', 'correctness']
	list_display = ('id','question', 'choice_text', 'correctness')
admin.site.register(Choice, ChoiceAdmin)
