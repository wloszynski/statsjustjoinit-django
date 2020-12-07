from django.shortcuts import render, redirect
import sqlite3
import datetime


def home(request):
    return redirect('/skills/all')


def all(request):
    return redirect('/skills/all')

def dataPrint(request, category):
    categories = ['all', 'javascript', 'html', 'php', 'ruby', 'python', 'java', 'net', 'scala', 'c', 'mobile', 'testing', 'devops', 'ux', 'pm', 'game', 'analytics', 'security', 'data', 'go', 'sap', 'support', 'other']

    # now_date = str(datetime.datetime.now()).split(' ')[0]
    conn = sqlite3.connect('skill_counter_all.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT id FROM language WHERE name like ?',(category,))
    cat_id = cur.fetchone()[0]


    cur.execute('''
        SELECT skill.name, overtime_skills.counter
        FROM overtime_skills
        INNER JOIN skill ON skill.id=overtime_skills.skill_id
        WHERE overtime_skills.language_id like ?
    ''', (cat_id,))

    rows = dict(cur.fetchall())
    rows = sorted(rows.items(), key=lambda x: x[1], reverse=True)
    all_rows = rows.copy()
    
    if len(rows) > 35:
        rest_rows = rows[36:]
        rows = rows[:36]
        sum_rest_rows = 0
        for row in rest_rows:
            sum_rest_rows += row[1]
        rows.append(('rest', sum_rest_rows))

    return render(request, 'skillsgraph/skills.html', {'categories':categories,'rows':rows, 'category_selected':category, 'all_rows':all_rows})


def jobs(request):
    def convert(tup, di): 
        for a, b in tup: 
            di.setdefault(a, []).append(b) 
        return di 

    now_date = str(datetime.datetime.now()).split(' ')[0]
    conn = sqlite3.connect('skill_counter_all.sqlite')
    cur = conn.cursor()

    cur.execute('''
        SELECT language.name, overtime_jobs.counter
        FROM overtime_jobs 
        INNER JOIN language ON language.id=overtime_jobs.language_id
    ''')
    
    rows = dict(cur.fetchall()[1:])
    rows = sorted(rows.items(), key=lambda x: x[1], reverse=True)
    
    if len(rows) > 35:
        rest_rows = rows[36:]
        rows = rows[:36]
        sum_rest_rows = 0
        for row in rest_rows:
            sum_rest_rows += row[1]
        rows.append(('rest', sum_rest_rows))
    return render(request, 'skillsgraph/jobs.html', {'rows':rows})
