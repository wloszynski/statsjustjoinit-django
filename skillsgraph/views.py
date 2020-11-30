from django.shortcuts import render, redirect
import sqlite3
import datetime


def home(request):
    return redirect('/skills/all')

def all(request):
    return redirect('/skills/all')

def dataPrint(request, category):
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
    

    return render(request, 'skillsgraph/dataInsert.html', {'rows':rows, 'category':category})

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
    
    
    return render(request, 'skillsgraph/jobs.html', {'rows':rows})
