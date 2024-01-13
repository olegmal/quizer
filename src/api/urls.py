from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from api.views import CustomerViewSet, QuestionDetailView, QuizListView
from django.urls import path, include

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)

# customers/ - all
# customers/1 - one
# customers/1 method delete - delete one customer
# customers/1 method put - edit one customer
# customers/1 method post - create one customer
# customers/1 method patch - edit one field of one customer


schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version='v1.0',
        description="API for passing questions",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_detail"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]