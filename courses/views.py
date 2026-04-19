from django.shortcuts import render, get_object_or_404
from .models import Course, Choice, Submission

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')

        submission = Submission.objects.create()

        correct = 0
        total = 0

        for choice_id in selected_choices:
            choice = Choice.objects.get(id=choice_id)
            submission.choices.add(choice)

            if choice.is_correct:
                correct += 1
            total += 1

        score = int((correct / total) * 100) if total > 0 else 0

        return render(request, 'courses/exam_result.html', {
            'score': score
        })

    return render(request, 'courses/course_detail.html', {'course': course})