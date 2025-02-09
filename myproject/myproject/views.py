from django.shortcuts import render

def index(req):
        # Фиктивные данные для демонстрации
    top_users = [
        {'username': 'Иван Иванов', 'courses_completed': 15},
        {'username': 'Анна Петрова', 'courses_completed': 12},
        {'username': 'Сергей Сидоров', 'courses_completed': 9},
        {'username': 'Елена Васильева', 'courses_completed': 7},
        {'username': 'Дмитрий Кузнецов', 'courses_completed': 6},
    ]
    context = {
        'top_users': top_users
    }
    return render(req, 'home.html', context)

def about(req):
    return render(req, 'about.html')