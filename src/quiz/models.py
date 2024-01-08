from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    image = models.ImageField(upload_to="media/category/covers", null=True, blank=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return f"{self.name} - {self.id}"


class Result(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", on_delete=models.CASCADE, related_name="results")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="results")
    count_of_correct_answers = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} - {self.quiz.title}"


class Quiz(BaseModel):
    QUESTION_MAX_COUNT = 5

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MEDIUM = 1, "Medium"
        ADVANCED = 2, "Advanced"

    category = models.ForeignKey(to="quiz.Category", on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(default="media/quiz/default.png", upload_to="media/quiz/covers")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)

    class Meta:
        verbose_name_plural = "Quizzes"
        verbose_name = "Quiz"

    def __str__(self):
        return f"{self.title} - {self.id}"


class Question(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", on_delete=models.CASCADE, related_name="questions")
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_COUNT)])
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.text} - {self.order_number}"


class Choice(BaseModel):
    question = models.ForeignKey(to="quiz.Question", on_delete=models.CASCADE, related_name="choices")
    text = models.TextField(max_length=250)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.question.order_number})"
