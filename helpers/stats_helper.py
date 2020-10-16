from helpers.database_helper import Database
import math


class StatsHelper():

    def __init__(self):
        self.database = Database()
        print("Stats Helping initialising!")

    def caculate_ave_overall_rating(self):
        result = self.database.fetch_one(
            "SELECT ROUND(AVG(review_overall), 1) FROM reviews")
        return result[0]

    # HINT: You can define more queries here, along with some python logic to calculate!
    def calculate_another_stat(self):
        # all_rows = self.database.fetch_all("")
        return None

    def top_five_highest_rated(self):
       result = self.database.fetch_all("SELECT beer_name, review_taste FROM reviews ORDER BY review_taste DESC LIMIT 5")
       return result

    def lowest_rating(self):
        result = self.database.fetch_all("SELECT beer_name, review_taste FROM reviews ORDER BY (select AVG(review_overall) from reviews) ASC LIMIT 5")
        return result

