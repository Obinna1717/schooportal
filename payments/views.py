from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import SchoolFee


class PaymentHistoryView(
    LoginRequiredMixin,
    ListView
):
    model = SchoolFee

    template_name = 'payments/payment_history.html'

    context_object_name = 'payments'

    def get_queryset(self):

        return SchoolFee.objects.filter(
            student=self.request.user
        )