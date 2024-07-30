from django.db import models
from django.utils import timezone
import pytz

class Event(models.Model):
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    timezone = models.CharField(max_length=63, choices=TIMEZONE_CHOICES, default='Africa/Lusaka')

    def get_start_time_in_timezone(self, target_timezone):
        target_tz = pytz.timezone(target_timezone)
        start_time = self.start_time.astimezone(pytz.timezone(self.timezone))
        return start_time.astimezone(target_tz)

    def time_until_event(self):
        now = timezone.now()
        return self.start_time - now

    def get_end_time(self):
        return self.start_time + self.duration

    def format_event(self, target_timezone='UTC'):
        start_time_tz = self.get_start_time_in_timezone(target_timezone)
        end_time_tz = start_time_tz + self.duration
        return f"{self.name}: {start_time_tz.strftime('%Y-%m-%d %H:%M:%S')} to {end_time_tz.strftime('%Y-%m-%d %H:%M:%S')} {target_timezone}"

    def __str__(self):
        return self.name
