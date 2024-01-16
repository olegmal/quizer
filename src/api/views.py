from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import (CustomerSerializer, QuestionSerializer,
                             QuizSerializer)
from core.permissions import IsSuperuser
from quiz.models import Question, Quiz


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class QuestionDetailView(RetrieveAPIView):
    # permission_classes = [AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()

    def get_object(self):
        return Question.objects.filter(quiz__pk=self.kwargs.get("pk"), order_number=self.kwargs.get("order")).first()


class QuizListView(ListAPIView):
    permission_classes = [IsSuperuser]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
