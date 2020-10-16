from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper

app = Flask(__name__)
stats_helper = StatsHelper()


@app.route('/')
def homepage():
    # HINT: Pass variables through to the HTML using Flask - https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    return render_template('index.html', todays_date=datetime.now(), ave_overall_rating=get_average_overall_rating,
                           top_five_highest_rating=get_top_five_highest_rated,lowest_rating=get_lowest_rating() )

# HINT: This could be your first statistic!


def get_average_overall_rating():
    return stats_helper.caculate_ave_overall_rating()


def get_top_five_highest_rated():
    return stats_helper.top_five_highest_rated()

def get_lowest_rating():
    return stats_helper.lowest_rating()
