from django import forms
from .models import Exercise, Goal

class ExerciseForm(forms.ModelForm):

	class Meta:
		model = Exercise
		fields = ('exercise_type', 'duration', 'datetime')

class GoalForm(forms.ModelForm):

	class Meta:
		model = Goal
		fields = ('exercise_type', 'goal_type', 'goal')