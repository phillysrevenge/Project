from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    # CRUD QUESTIONs

    path('questions/', views.QuestionListView.as_view(), name="question-list"),
    # uses the questions and calls based on primary key in the DB
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(),
         name="question-detail"),

    path('questions/new/', views.QuestionCreateView.as_view(),
         name="question-create"),

    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(),
         name="question-update"),
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(),
         name="question-delete"),
    path('questions/<int:pk>/answer/', views.AddAnswerView.as_view(),
         name="question-answer"),
    path('like/<int:pk>', views.like_view, name="like_post")
]
