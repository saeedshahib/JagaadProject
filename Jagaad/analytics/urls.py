from django.urls import path

from . import views as analytics_views

urlpatterns = [
    path("create-message/", analytics_views.MessageCreateView.as_view()),
    path("retrieve-stats/", analytics_views.MessageStatsView.as_view()),
]
