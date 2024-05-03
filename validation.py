from datetime import datetime
from flask import redirect, url_for, current_app

# class which validates the given date string
# to ensure that it is in the right format
class DateValidation:
    def __init__(self, date):
        self.validate_date(date)

    def validate_date(self, date):
        try: dt = datetime.strptime(date, '%Y-%b-%d')
        except ValueError: raise ValueError("error: invalid date format given")

# class which validates that the given task data
# has all the fields required
class TaskDataFormatValidation:
    def __init__(self, task):
        self.validate_task_format(task)

    def validate_task_format(self, task):
        if "Title" not in task: raise ValueError("error: title not in given task data")
        if "Priority" not in task: raise ValueError("error: priority not in given task data")
        if "Status" not in task: raise ValueError("error: status not in given task data")
        if "Date" not in task: raise ValueError("error: date not in given task data")

# class which validates that the given taskID
# exists within the database
class TaskIDValidation:
    def __init__(self, taskID):
        self.validate_taskID(taskID)

    def validate_taskID(self, taskID):
        try:
            cursor = current_app.db.connection.cursor()
            sql_query = f"""
                SELECT * FROM {current_app.config['TASK_TABLE']} WHERE
                TaskID={taskID};
            """
            cursor.execute(sql_query)
            cursor.close()
        except Exception:
            raise Exception("error: invalid taskID given")
