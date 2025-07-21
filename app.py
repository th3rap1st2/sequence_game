from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

inc_score = 0
dec_score = 0



def check_sequence(number, piece_length):
    new_list = []
    i = 0
    while i < len(number):
        new_list.append(number[i: piece_length + i])
        i = piece_length + i

    return new_list


def increasing_sequence(sequence):
    i = 1
    prev = int(sequence[0])

    while i < len(sequence):
        if prev >= int(sequence[i]):
            return False

        prev = int(sequence[i])
        i += 1

    return True


def decreasing_sequence(sequence):
    i = 1
    prev = int(sequence[0])

    while i < len(sequence):
        if prev <= int(sequence[i]):
            return False

        prev = int(sequence[i])
        i += 1

    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/check', methods=['POST'])

def check():
    global inc_score, dec_score

    number = request.form.get('number')
    pieces = request.form.get('piece_length')

    if not number or not number.isdigit() or int(number) <= 0:
        return jsonify({"error": "Invalid input. Please enter a positive whole number."})

    try:
        pieces = int(pieces)
        if pieces <= 0 or len(number) % pieces != 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": f"Invalid input. Make sure piece length is a divisor of {len(number)}."})
    
    sequence = check_sequence(number, pieces)


    if increasing_sequence(sequence):
        result = "increasing"
        inc_score += 1
    elif decreasing_sequence(sequence):
        result = "decreasing"
        dec_score += 1
    else:
        result = "neutral"

    return jsonify({
    "pieces": sequence,
    "order": result,
    "increasingScore": inc_score,
    "decreasingScore": dec_score
    })

if __name__ == "__main__":
    app.run(debug=True)

