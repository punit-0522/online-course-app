from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # REQUIRED: submit route
    path('course/<int:course_id>/submit/', views.submit, name='submit'),

    # REQUIRED: exam result route
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]