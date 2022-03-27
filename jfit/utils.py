import datetime
from enum import Enum
from . import string_constants

class DateHelper:

	@staticmethod
	def convert_str_to_datetime(input_str):
		return datetime.datetime.strptime(input_str, string_constants.DATE_STR_FORMAT)

	@staticmethod
	def get_earlier_date(delta):
		return datetime.date.today() - datetime.timedelta(days=delta)

	@staticmethod
	def convert_date_to_string(input_date):
		return input_date.strftime(string_constants.DATE_STR_FORMAT)


class AlertMessage(Enum):
	GE = string_constants.GOAL_ERROR_MSG
	DS = string_constants.DATA_SAVE_MSG
	DE = string_constants.DATA_ERROR_MSG

class AlertMessageHelper:

	@staticmethod
	def get_alert_string(input_str):
		if input_str == "GE":
			return AlertMessage.GE.value
		elif input_str == "DS":
			return AlertMessage.DS.value
		elif input_str == "DE":
			return AlertMessage.DE.value