import random
import time

class FootballGame:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0

    def simulate_game(self):
        print(f"Starting the game between {self.team1} and {self.team2}")
        for minute in range(1, 91):
            time.sleep(0.1)  # Simulate the passage of time
            self.simulate_minute(minute)

        self.print_final_score()

    def simulate_minute(self, minute):
        if random.random() < 0.05:  # 5% chance of a goal each minute
            if random.random() < 0.5:
                self.score1 += 1
                print(f"Minute {minute}: GOAL! {self.team1} scores! Current score: {self.team1} {self.score1} - {self.team2} {self.score2}")
            else:
                self.score2 += 1
                print(f"Minute {minute}: GOAL! {self.team2} scores! Current score: {self.team1} {self.score1} - {self.team2} {self.score2}")

    def print_final_score(self):
        print(f"Final score: {self.team1} {self.score1} - {self.team2} {self.score2}")

if __name__ == "__main__":
    game = FootballGame("Team A", "Team B")
    game.simulate_game()
