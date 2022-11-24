import csv
import random

MAX_QUESTIONS = 10


def create_questions(name):
    questions = {}
    fname = "{}.csv".format(name)
    with open(fname, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            questions[row[]]
    
