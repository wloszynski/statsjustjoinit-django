from django.shortcuts import render, redirect
import sqlite3
import datetime

categories = [
    'all',
    'javascript',
    'html',
    'php',
    'ruby',
    'python',
    'java',
    'net',
    'scala',
    'c',
    'mobile',
    'testing',
    'devops',
    'ux',
    'pm',
    'game',
    'analytics',
    'security',
    'data',
    'go',
    'sap',
    'support',
    'other',
    ]
categories_menu = [
    'All',
    'JS',
    'HTML',
    'PHP',
    'Ruby',
    'Python',
    'Java',
    '.Net',
    'Scala',
    'C',
    'Mobile',
    'Testing',
    'DevOps',
    'UX/UI',
    'PM',
    'Game',
    'Analytics',
    'Security',
    'Data',
    'Go',
    'SAP',
    'Support',
    'Other',
    ]



def home(request):
    return redirect('/skills/all')


def all(request):
    return redirect('/skills/all')


def dataPrint(request, category):

    # now_date = str(datetime.datetime.now()).split(' ')[0]

    conn = sqlite3.connect('skill_counter.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT id FROM language WHERE name like ?', (category,
                ))
    cat_id = cur.fetchone()[0]

    cur.execute('''
        SELECT skill.name, overtime_skills.counter
        FROM overtime_skills
        INNER JOIN skill ON skill.id=overtime_skills.skill_id
        WHERE overtime_skills.language_id like ? AND date_created like "2021-01-05"
    ''',
                (cat_id, ))

    rows = dict(cur.fetchall())
    rows = sorted(rows.items(), key=lambda x: x[1], reverse=True)
    all_rows = rows.copy()

    if len(rows) > 35:
        rest_rows = rows[36:]
        rows = rows[:36]
        sum_rest_rows = 0
        for row in rest_rows:
            sum_rest_rows += row[1]
        rows.append(('other', sum_rest_rows))

    return render(request, 'skillsgraph/skills.html', {
        'categories': categories,
        'rows': rows,
        'category_selected': category,
        'all_rows': all_rows,
        'categories_zipped': list(zip(categories, categories_menu)),
        })


def jobs(request):

    now_date = str(datetime.datetime.now()).split(' ')[0]
    conn = sqlite3.connect('skill_counter.sqlite')
    cur = conn.cursor()

    cur.execute('''
        SELECT language.name, overtime_jobs.counter
        FROM overtime_jobs
        INNER JOIN language ON language.id=overtime_jobs.language_id
        WHERE date_created like "2021-01-05"
    ''')

    rows = dict(cur.fetchall()[1:])
    rows = sorted(rows.items(), key=lambda x: x[1], reverse=True)
    all_rows = rows.copy()

    if len(rows) > 15:
        rest_rows = rows[16:]
        rows = rows[:16]
        sum_rest_rows = 0
        for row in rest_rows:
            sum_rest_rows += row[1]
        rows.append(('other', sum_rest_rows))

    return render(request, 'skillsgraph/skills.html', {
        'rows': rows,
        'categories': categories,
        'categories_zipped': list(zip(categories, categories_menu)),
        'all_rows': all_rows,
        'category_selected': 'all jobs',
        })



