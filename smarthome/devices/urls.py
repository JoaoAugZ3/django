from django.urls import path
from .views import hello, PingView, EnvironmentsListView, EnvironmentDatailUpdateView



urlpatterns = [
    # path("admin/", admin.site.urls),
    path('hello',hello),
    path('ping', PingView.as_view()),
    path('environments', EnvironmentsListView.as_view()),
    path('environments/<int:pk>',EnvironmentDatailUpdateView.as_view())
]