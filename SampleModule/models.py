from django.db import models

class SampleFollowUp(models.Model):
    name = models.CharField(max_length=255)  # Name of the follow-up
    date = models.DateField()               # Date for the follow-up
    status = models.CharField(max_length=100)  # Status of the follow-up (e.g., Pending, Completed)
    remarks = models.TextField(null=True, blank=True)  # Optional remarks

    def __str__(self):
        return f"{self.name} - {self.status}"

class SampleComment(models.Model):
    follow_up = models.ForeignKey(SampleFollowUp, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for {self.follow_up.name}"

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    reminder_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Reminder: {self.title} on {self.reminder_date}"
