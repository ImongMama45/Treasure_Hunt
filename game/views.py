from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def index(request):
    """Render the main game page"""
    return render(request, 'game/index.html')

@require_http_methods(["POST"])
def check_answer(request):
    """Check if the submitted answer is correct"""
    user_answer = request.POST.get('answer', '').strip().lower()
    correct_answer = 'gambert'
    
    is_correct = user_answer == correct_answer
    
    return JsonResponse({
        'correct': is_correct,
        'message': 'Congratulations! You unlocked the treasure!' if is_correct else 'Incorrect word. Try again!'
    })
