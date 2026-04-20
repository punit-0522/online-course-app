from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission


# COURSE PAGE
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'questions': questions
    })


# REQUIRED: SUBMIT VIEW
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    if request.method == 'POST':
        score = 0
        total = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(str(question.id))

            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                if choice.is_correct:
                    score += 1

        submission = Submission.objects.create(
            course=course,
            score=score
        )

        return redirect('show_exam_result',
                        course_id=course.id,
                        submission_id=submission.id)

    return redirect('course_detail', course_id=course.id)


# REQUIRED: RESULT VIEW
def show_exam_result(request, course_id, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    return render(request, 'courses/exam_result.html', {
        'submission': submission,
        'score': submission.score
    })