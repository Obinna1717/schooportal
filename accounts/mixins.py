from django.contrib.auth.mixins import UserPassesTestMixin


class LecturerRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return (
            self.request.user.is_authenticated and
            self.request.user.role == 'lecturer'
        )
        
class StudentRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == "student"        