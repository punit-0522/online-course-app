from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course, Lesson, Question, Choice, Submission


def index(request):
    return render(request, 'index.html')


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Get selected answers
    selected_choices = request.POST.getlist('choice')

    # Create submission
    submission = Submission.objects.create()

    # Calculate score
    total_score = 0
    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=int(choice_id))
        if choice.is_correct:
            total_score += 1

    # Save score in session (simple approach)
    request.session['total_score'] = total_score
    request.session['course_id'] = course.id

    return redirect('show_exam_result')


def show_exam_result(request):
    total_score = request.session.get('total_score', 0)
    course_id = request.session.get('course_id')

    course = get_object_or_404(Course, pk=course_id)

    # Calculate possible score
    questions = Question.objects.filter(lesson__course=course)
    possible_score = questions.count()

    context = {
        'course': course,
        'total_score': total_score,
        'possible_score': possible_score,
    }

    return render(request, 'result.html', context)