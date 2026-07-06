from django.urls import path
from .views import (
    AttendanceListView,
    DashboardView,
    DeleteSubmissionView,
    EditSubmissionView,
    LecturerDashboardView,
    MySubmittedAssignmentsView,
    PostAssignmentView,
    SelectAttendanceCourseView,
    StudentAssignmentListView,
    StudentAttendanceSummaryView,
    TakeAttendanceView,
    UploadMaterialView,
    SubmitAssignmentView,
    ViewPostAnnouncementView,
    ViewSubmissionsView,
    MarkAttendanceView,
    PostAnnouncementView,
    EditMaterialView,
    DeleteMaterialView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    
    path("lecturer-dashboard/", LecturerDashboardView.as_view(), name="lecturer_dashboard"),
    
    path("upload-material/", UploadMaterialView.as_view(), name="upload_material"),
    
    path("view-submissions/", ViewSubmissionsView.as_view(), name="view_submissions"),
    
    path("view-posted-assignments/", ViewPostAnnouncementView.as_view(), name="view_posted_assignments"),
    
    path("mark-attendance/", MarkAttendanceView.as_view(), name="mark_attendance"),
    
    path("post-announcement/", PostAnnouncementView.as_view(), name="post_announcement"),
    
    path("post-assignment/", PostAssignmentView.as_view(), name="post_assignment"),
    
    path("material/<int:pk>/edit/", EditMaterialView.as_view(), name="edit_material"),
    
    path("material/<int:pk>/delete/", DeleteMaterialView.as_view(), name="delete_material"),
    
    path("student/assignments/", StudentAssignmentListView.as_view(), name="student_assignments"),
    
    path("submit-assignment/<int:pk>/", SubmitAssignmentView.as_view(), name="submit_assignment"),
    
    path("submission/<int:pk>/edit/", EditSubmissionView.as_view(), name="edit_submission"),
    
    path("submission/<int:pk>/delete/", DeleteSubmissionView.as_view(), name="delete_submission"),
    
    path("my-submitted-assignments/", MySubmittedAssignmentsView.as_view(), name="my_submitted_assignment"),
    
    path("attendance/", SelectAttendanceCourseView.as_view(), name="select_attendance_course"),
    
    path("attendance/<int:pk>/", TakeAttendanceView.as_view(), name="take_attendance"),
    
    path("attendance-records/", AttendanceListView.as_view(), name="attendance_records"),
    
    path("my-attendance/", StudentAttendanceSummaryView.as_view(), name="student_attendance"),
]