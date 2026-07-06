from django.contrib import admin
from .models import (
    Assignment,
    AssignmentSubmission,
    Attendance,
    Announcement,
    PostAssignment
)

admin.site.register(Assignment)
admin.site.register(PostAssignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Attendance)
admin.site.register(Announcement)