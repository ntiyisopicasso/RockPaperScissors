from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Choices available in the game
choices = ['rock', 'paper', 'scissors']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    # Get player choice from the request
    player_choice = request.json['choice']
    
    # Get computer's random choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
