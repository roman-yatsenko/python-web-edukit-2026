import requests

base_url = 'http://127.0.0.1:8000/api/'
username = 'student'
password = 'qwY6hUzf6b4@qSM'

# отримаємо всі курси
r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ', '.join(course['title'] for course in courses)
print(f'Доступні курси: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll/',
                      auth=(username, password))
    if r.status_code == 200:
        # Успішний запит
        print(f'Успішно зараховано на курс {course_title}')
