import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .forms import ExerciseForm, GoalForm
from .models import Exercise, Goal, GoalType, ExerciseType
from .utils import DateHelper, AlertMessage, AlertMessageHelper

'''
This default date offset is being used to show the exercise chart.
e.g. Value=1 represents, it shows the data from yesterday.
'''
DEFAULT_DATE_OFFSET = 1

'''
This default exercise type is being used to show progress information.
e.g. Value=1 represents, it shows the data for ExerciseType 1.
'''
DEFAULT_EXE_TYPE = 1

'''
This default goal type is being used to show progress information for specific goal.
e.g. Value=1 represents, it shows the data for GoalType 1.
'''
DEFAULT_GOAL_TYPE = 1

class HomeView(View):

	exercise_form = ExerciseForm
	goal_form = GoalForm
	alert_msg = AlertMessage.DE.name

	def get(self, request, alert_msg=None):

		# Form instances
		exercise_form_obj = self.exercise_form()
		goal_form_obj = self.goal_form()

		# Fetch data for datewise exercises to show in exercises-chart
		selected_date = DateHelper.get_earlier_date(DEFAULT_DATE_OFFSET)
		if "selected_date" in request.GET:
			selected_date = DateHelper.convert_str_to_datetime(request.GET["selected_date"])
		all_exercises = Exercise.objects.filter(datetime=selected_date)
		datewise_exercises = {}
		datewise_total_exercises = 0
		for exercise in all_exercises:
			exe_name = exercise.exercise_type.exercise_name
			if exe_name in datewise_exercises:
				datewise_exercises[exe_name] += exercise.duration
			else:
				datewise_exercises[exe_name] = exercise.duration
			datewise_total_exercises += 1
		
		# Calculating Progress for default exercise type
		selected_goal = DEFAULT_GOAL_TYPE
		if "selected_goal" in request.GET:
			selected_goal = int(request.GET["selected_goal"])
		goal_name = GoalType.objects.get(id=selected_goal).goal_name
		goal_value = Goal.objects.values_list('goal', flat=True).filter(exercise_type=DEFAULT_EXE_TYPE).filter(goal_type=selected_goal)
		exercise_name = ExerciseType.objects.get(id=DEFAULT_EXE_TYPE).exercise_name
		if len(goal_value) > 0:
			accomplished_goal_value = sum(Exercise.objects.values_list('duration', flat=True).filter(exercise_type=DEFAULT_EXE_TYPE))
			progress_percentage = (100*accomplished_goal_value)/goal_value[0]
		else:
			progress_percentage = AlertMessage.GE.value

		# Alert Message
		if alert_msg is not None:
			alert_msg = AlertMessageHelper.get_alert_string(alert_msg)

		# Create context for Template
		context = {
			"exercise_form": exercise_form_obj,
			"goal_form": goal_form_obj,
			"datewise_exercises": datewise_exercises,
			"total_exercises": datewise_total_exercises,
			"progress_perc": progress_percentage,
			"exercise_name": exercise_name,
			"goal_type": goal_name,
			"selected_date": DateHelper.convert_date_to_string(selected_date),
			"goal_types": GoalType.objects.all(),
			"selected_goal": selected_goal,
			"alert_msg": alert_msg
		}
		return render(request, "jfit/index.html", context)

	def post(self, request, alert_msg=None):
		if "exercise_form" in request.POST:
			form_obj = self.exercise_form(request.POST)	
			if form_obj.is_valid():
				form_obj.save()
				self.alert_msg = AlertMessage.DS.name
		elif "goal_form" in request.POST:
			form_obj = self.goal_form(request.POST)
			if form_obj.is_valid():
				form_obj.save()
				self.alert_msg = AlertMessage.DS.name
		return HttpResponseRedirect(reverse('jfit:home', args=(self.alert_msg,)))










