from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def janken():
    match = {}
    if request.method == 'POST':
        client_hand = request.form['hand']
        match["client_hand"] = client_hand
        janken_result = pc_choice(client_hand, match)

        return render_template('result.html', client_hand=match["client_hand"],
                               pc_hand=match["pc_hand"], janken_result=match["result"])

    return render_template('index.html')


def pc_choice(client_hand, match):
    client_hand = client_hand
    pc_choices = ["グー", "チョキ", "パー"]
    pc_hand = random.choice(pc_choices)
    match["pc_hand"] = pc_hand

    draw = '引き分けでした。'
    win = 'あなたの勝ちです！'
    lose = 'あなたの負けです...'

    if client_hand == pc_hand:
        match["result"] = draw
        return match
    else:
        if client_hand == "グー":
            if pc_hand == "チョキ":
                match["result"] = win
                return match
            else:
                match["result"] = lose
                return match

        elif client_hand == "チョキ":
            if pc_hand == "パー":
                match["result"] = win
                return match
            else:
                match["result"] = lose
                return match

        else:
            if pc_hand == "グー":
                match["result"] = win
                return match
            else:
                match["result"] = lose
                return match


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
