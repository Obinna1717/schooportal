from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Result


class ResultListView(
    LoginRequiredMixin,
    ListView
):
    model = Result

    template_name = 'results/result_list.html'

    context_object_name = 'results'

    def get_queryset(self):

        return Result.objects.filter(
            student=self.request.user
        )