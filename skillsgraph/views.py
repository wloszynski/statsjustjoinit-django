from django.shortcuts import render, redirect
import sqlite3
import datetime


def home(request):
    return redirect('/all/all')

def all(request):
    return redirect('/all/all')

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
    rows = cur.fetchall()


    return render(request, 'skillsgraph/dataInsert.html', {'rows':rows, 'category':category})