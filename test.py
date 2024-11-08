from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

class FootballGame:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0

    def simulate_game(self):
        results = []
        for minute in range(1, 91):
            time.sleep(0.1)  # Simulate the passage of time
            result = self.simulate_minute(minute)
            if result:
                results.append(result)
        return results

    def simulate_minute(self, minute):
        if random.random() < 0.05:  # 5% chance of a goal each minute
            if random.random() < 0.5:
                self.score1 += 1
                return f"Minute {minute}: GOAL! {self.team1} scores! Current score: {self.team1} {self.score1} - {self.team2} {self.score2}"
            else:
                self.score2 += 1
                return f"Minute {minute}: GOAL! {self.team2} scores! Current score: {self.team1} {self.score1} - {self.team2} {self.score2}"
        return None

@app.route('/simulate_game', methods=['GET'])
def simulate_game():
    game = FootballGame("Team A", "Team B")
    results = game.simulate_game()
    final_score = f"Final score: {game.team1} {game.score1} - {game.team2} {game.score2}"
    return jsonify({'results': results, 'final_score': final_score})

if __name__ == '__main__':
    app.run(debug=True)