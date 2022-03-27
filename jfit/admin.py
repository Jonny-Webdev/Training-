from django.contrib import admin
from .models import ExerciseType, GoalType, Exercise, Goal

admin.site.register(ExerciseType)
admin.site.register(GoalType)
admin.site.register(Exercise)
admin.site.register(Goal)