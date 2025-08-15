
#!/usr/bin/env python3
\"\"\"CodeQuest - Interactive Coding Skill Trainer (Q1 prototype)

This console program is a beginner-friendly but modular trainer that covers:
- Variables
- Conditionals
- Loops
- Functions

It demonstrates functions, control flow, loops, basic file I/O, and simple data persistence.
It logs attempts in attempts.csv and student profiles in students.json.

Run: python codequest.py
\"\"\"

import json
import csv
import os
import uuid
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
ATTEMPTS_FILE = os.path.join(DATA_DIR, 'attempts.csv')

TOPICS = ['Variables', 'Conditionals', 'Loops', 'Functions']

# Simple question bank: each question has id, topic, difficulty (1-3 here), prompt, answer, explanation, type
QUESTION_BANK = [
    # Variables (difficulty 1-2)
    {'id':'V1','topic':'Variables','difficulty':1,'type':'predict','prompt':'What will this print?\\n\\nx = 3\\nprint(x)','answer':'3','explanation':'print(x) prints the value of x.'},
    {'id':'V2','topic':'Variables','difficulty':2,'type':'fill','prompt':'Fill the blank to assign 10 to variable a: a = __','answer':'10','explanation':'Use a = 10 to store the number 10 in a.'},

    # Conditionals
    {'id':'C1','topic':'Conditionals','difficulty':1,'type':'predict','prompt':'What will this print?\\n\\nif 5 > 2:\\n    print(\"Yes\")\\nelse:\\n    print(\"No\")','answer':'Yes','explanation':'5 is greater than 2, so the if branch runs.'},
    {'id':'C2','topic':'Conditionals','difficulty':2,'type':'fix','prompt':'Fix the code to print \"Equal\" when x == y:\\n\\nx = 3\\ny = 3\\nif x = y:\\nprint(\"Equal\")','answer':'if x == y:\\n    print(\"Equal\")','explanation':'Use == for comparison and indent the print.'},

    # Loops
    {'id':'L1','topic':'Loops','difficulty':1,'type':'predict','prompt':'What will this print?\\n\\nfor i in range(3):\\n    print(i)','answer':'0\\n1\\n2','explanation':'range(3) yields 0,1,2 so each is printed on its own line.'},
    {'id':'L2','topic':'Loops','difficulty':2,'type':'predict','prompt':'What will this print?\\n\\ncount = 0\\nwhile count < 2:\\n    print(\"Hi\")\\n    count += 1','answer':'Hi\\nHi','explanation':'The while loop runs twice.'},

    # Functions
    {'id':'F1','topic':'Functions','difficulty':1,'type':'predict','prompt':'What will this print?\\n\\ndef add(a, b):\\n    return a + b\\nprint(add(2,3))','answer':'5','explanation':'add returns the sum 2 + 3.'},
    {'id':'F2','topic':'Functions','difficulty':2,'type':'fill','prompt':'Fill the blank to define a function that returns 10:\\ndef ten():\\n    __','answer':'return 10','explanation':'Functions use return to send back values.'},
]

# Utilities for file handling and initialization
def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE,'w',encoding='utf-8') as f:
            json.dump({}, f, indent=2)
    if not os.path.exists(ATTEMPTS_FILE):
        with open(ATTEMPTS_FILE,'w',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['attempt_id','student_id','topic','question_id','difficulty','correct','timestamp'])

def load_students():
    with open(STUDENTS_FILE,'r',encoding='utf-8') as f:
        return json.load(f)

def save_students(data):
    with open(STUDENTS_FILE,'w',encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def log_attempt(student_id, topic, question_id, difficulty, correct):
    attempt_id = str(uuid.uuid4())[:8]
    ts = datetime.now().isoformat(timespec='seconds')
    with open(ATTEMPTS_FILE,'a',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([attempt_id, student_id, topic, question_id, difficulty, int(correct), ts])

# Student profile helpers
def create_student(name):
    students = load_students()
    sid = 'S' + str(len(students)+1).zfill(3)
    students[sid] = {
        'id': sid,
        'name': name,
        'created_at': datetime.now().isoformat(timespec='seconds'),
        'stats': {t:{'attempts':0,'correct':0,'difficulty':1} for t in TOPICS}
    }
    save_students(students)
    return students[sid]

def select_student():
    students = load_students()
    if not students:
        print('No students found. Please create a profile.')
        return None
    print('Choose a student:')
    for sid, s in students.items():
        print(f'{sid}: {s["name"]}')
    choice = input('Enter student ID (or type "new"): ').strip()
    if choice.lower() == 'new':
        name = input('Enter student name: ').strip()
        return create_student(name)
    if choice in students:
        return students[choice]
    print('Invalid choice. Try again.')
    return None

# Very short micro-lessons (kept simple and kid-friendly)
def micro_lesson(topic):
    lessons = {
        'Variables': 'Variables store values. Example: x = 5 assigns 5 to x.',
        'Conditionals': 'Conditionals let code make decisions. Example: if x > 0: print(\"pos\")',
        'Loops': 'Loops repeat actions. Example: for i in range(3): print(i)',
        'Functions': 'Functions are reusable code blocks. Example: def f():\\n    return 1'
    }
    print('\\nLesson:')
    print(lessons.get(topic,'Short lesson coming soon.'))
    print()

def pick_question(topic, difficulty):
    # choose first matching question with difficulty <= current difficulty (simple selection)
    candidates = [q for q in QUESTION_BANK if q['topic']==topic and q['difficulty']<=difficulty]
    if not candidates:
        # fallback to any question in topic
        candidates = [q for q in QUESTION_BANK if q['topic']==topic]
    # pick question by simple deterministic method (rotate by timestamp for predictability)
    return candidates[0]

def present_question(q):
    print('Question:')
    print(q['prompt'])
    ans = input('\\nYour answer: ').strip()
    # Normalize answers for predict type that might have newlines
    if q['type']=='predict':
        expected = q['answer'].strip().replace('\\r','').replace('\\n','\\n')
        # normalize both by removing extra spaces and lowercasing when appropriate
        user = ans.strip()
        # For multi-line answers, allow different line endings by splitting and rejoining with \\n
        user_norm = '\\n'.join([line.strip() for line in user.splitlines()])
        correct = user_norm == expected
    else:
        correct = ans.strip() == q['answer'].strip()
    print('\\n' + ('Correct!' if correct else 'Not quite.'))
    print('Explanation:', q.get('explanation','No explanation available.'))
    return correct

def update_student_stats(student_id, topic, correct):
    students = load_students()
    s = students[student_id]
    s['stats'][topic]['attempts'] += 1
    if correct:
        s['stats'][topic]['correct'] += 1
        # raise difficulty slowly
        s['stats'][topic]['difficulty'] = min(3, s['stats'][topic]['difficulty'] + 0.2)
    else:
        # lower difficulty slowly, min 1
        s['stats'][topic]['difficulty'] = max(1, s['stats'][topic]['difficulty'] - 0.2)
    save_students(students)

def show_progress(student):
    print('\\nProgress overview:')
    for topic, d in student['stats'].items():
        attempts = d['attempts']
        correct = d['correct']
        pct = int((correct/attempts)*100) if attempts>0 else 0
        print(f'- {topic}: {pct}% ({correct}/{attempts}) | difficulty {d["difficulty"]:.1f}')

def generate_teacher_reports():
    # Read attempts and compute per-student and class aggregates
    if not os.path.exists(ATTEMPTS_FILE):
        print('No attempts found yet.')
        return
    # aggregate per student-topic
    per_student = {}
    per_topic = {t: {'correct':0,'attempts':0,'common':{}} for t in TOPICS}
    with open(ATTEMPTS_FILE,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row['student_id']
            topic = row['topic']
            correct = int(row['correct'])
            per_student.setdefault(sid,{})
            per_student[sid].setdefault(topic,{'correct':0,'attempts':0})
            per_student[sid][topic]['attempts'] += 1
            per_student[sid][topic]['correct'] += correct
            per_topic[topic]['attempts'] += 1
            per_topic[topic]['correct'] += correct
            # track simple common mistake counter (when incorrect)
            if not correct:
                per_topic[topic]['common'].setdefault('Incorrect answers',0)
                per_topic[topic]['common']['Incorrect answers'] += 1

    # Write detailed per-student report
    report_txt = os.path.join(DATA_DIR,'teacher_report.txt')
    summary_csv = os.path.join(DATA_DIR,'teacher_report_summary.csv')
    students = load_students()
    with open(report_txt,'w',encoding='utf-8') as rt:
        rt.write('Teacher Report - Detailed\\n')
        rt.write('Generated: ' + datetime.now().isoformat(timespec='seconds') + '\\n\\n')
        for sid, topics in per_student.items():
            name = students.get(sid,{}).get('name','Unknown')
            rt.write(f'STUDENT: {name} (ID: {sid})\\n')
            rt.write('-'*40 + '\\n')
            for topic in TOPICS:
                tdata = topics.get(topic,{'correct':0,'attempts':0})
                attempts = tdata['attempts']
                correct = tdata['correct']
                pct = int((correct/attempts)*100) if attempts>0 else 0
                status = 'No Data' if attempts==0 else ('Strong' if pct>=85 else ('Needs Improvement' if pct<65 else 'Stable'))
                rt.write(f'- {topic}: {pct}% ({correct}/{attempts}) -> {status}\\n')
            # simple overall trend (compare sum of recent attempts if available) - placeholder
            rt.write('\\nRecommendation: Focus on topics with percentage < 70%\\n\\n')

    # Write summary CSV for class view
    with open(summary_csv,'w',encoding='utf-8',newline='') as sc:
        writer = csv.writer(sc)
        writer.writerow(['topic','average_mastery','class_trend','common_mistake'])
        for topic, vals in per_topic.items():
            attempts = vals['attempts']
            correct = vals['correct']
            avg = int((correct/attempts)*100) if attempts>0 else 0
            trend = 'Declining' if avg < 65 else ('Improving' if avg >= 80 else 'Stable')
            common = ''
            if vals['common']:
                # pick most common issue label
                common = max(vals['common'].items(), key=lambda x: x[1])[0]
            writer.writerow([topic, f'{avg}%', trend, common])

    print('Teacher reports generated in data/ (teacher_report.txt and teacher_report_summary.csv)')

# Main interactive loop
def main_menu():
    ensure_data_files()
    print('Welcome to CodeQuest (Q1 prototype)')
    students = load_students()
    while True:
        print('\\nMain Menu:')
        print('1) Login / Select Student')
        print('2) Create Student Profile')
        print('3) Generate Teacher Reports')
        print('4) Quit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            student = select_student()
            if student:
                student_session(student)
        elif choice == '2':
            name = input('Enter student name: ').strip()
            student = create_student(name)
            print(f'Created student {student["name"]} with ID {student["id"]}')
        elif choice == '3':
            generate_teacher_reports()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, try again.')

def student_session(student):
    sid = student['id']
    while True:
        print('\\nStudent Menu:')
        print('1) Show progress')
        print('2) Select topic')
        print('3) Back to main menu')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            show_progress(student)
        elif choice == '2':
            print('\\nTopics:')
            for i,t in enumerate(TOPICS, start=1):
                print(f'{i}) {t}')
            ti = input('Select topic number: ').strip()
            if not ti.isdigit() or not (1 <= int(ti) <= len(TOPICS)):
                print('Invalid selection.')
                continue
            topic = TOPICS[int(ti)-1]
            micro_lesson(topic)
            # pick question based on stored difficulty
            students = load_students()
            diff = int(round(students[sid]['stats'][topic]['difficulty']))
            q = pick_question(topic, diff)
            correct = present_question(q)
            log_attempt(sid, topic, q['id'], q['difficulty'], correct)
            update_student_stats(sid, topic, correct)
            # reload student
            student = load_students()[sid]
        elif choice == '3':
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main_menu()
