from django.db import models

class ExerciseType(models.Model):
	exercise_name = models.CharField(max_length=25)

	def __str__(self):
		return "{}".format(self.exercise_name)

class GoalType(models.Model):
	goal_name = models.CharField(max_length=25)

	def __str__(self):
		return "{}".format(self.goal_name)

class Exercise(models.Model):
	exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
	duration = models.IntegerField()
	datetime = models.DateTimeField()

	def __str__(self):
		return "{}: {} minutes".format(self.exercise_type.exercise_name, self.duration) 

class Goal(models.Model):
	exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
	goal_type = models.ForeignKey(GoalType, on_delete=models.CASCADE)
	goal = models.IntegerField()
	goal_set_datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "[{}] {}: {} minutes".format(self.goal_type, self.exercise_type.exercise_name, self.goal) 