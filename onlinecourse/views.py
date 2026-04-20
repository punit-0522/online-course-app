from django.http import HttpResponse

def index(request):
    return HttpResponse("Course App Running")

def submit(request):
    return HttpResponse("Submit Page")

def show_exam_result(request):
    return HttpResponse("Result Page")