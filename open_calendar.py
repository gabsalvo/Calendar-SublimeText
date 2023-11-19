import sublime
import sublime_plugin
import calendar
from datetime import datetime

class OpenCalendarCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get current year and month
        now = datetime.now()
        year = now.year
        month = now.month

        # Generate a month's calendar
        cal = calendar.monthcalendar(year, month)
        cal_str = calendar.month_name[month] + " " + str(year) + "\n\n"
        cal_str += "Mo Tu We Th Fr Sa Su\n"

        for week in cal:
            for day in week:
                # Add day number or space padding
                cal_str += "{:2} ".format(day) if day != 0 else "   "
            cal_str += "\n"

        # Open a new tab and insert the calendar
        new_view = self.window.new_file()
        new_view.set_scratch(True)
        new_view.set_name("Calendar")
        new_view.run_command('append', {'characters': cal_str})
