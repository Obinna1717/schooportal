from django.urls import path

from .views import ResultListView

urlpatterns = [

    path(
        '',
        ResultListView.as_view(),
        name='result_list'
    ),

]