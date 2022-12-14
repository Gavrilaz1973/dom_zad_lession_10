from flask import Flask
from utils import load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)

@app.route("/")
def page_index():
    candidates = load_candidates()
    candidates_list = "<br>"
    for i in candidates:
        candidates_list += "Имя кандидата - " + i['name'] + '<br>'
        candidates_list += "Позиция кандидата - " + i['position'] + '<br>'
        candidates_list += "Навыки кандидата - " + i['skills'] + '<br>' + '<br>'
    return f'<pre> {candidates_list} </pre>'


@app.route("/candidates/<int:x>")
def page_index_pk(x):
    candidate_pk = get_by_pk(x)
    candidate_pk_list = "<bk>"
    candidate_pk_list += "Имя кандидата - " + candidate_pk['name'] + '<br>'
    candidate_pk_list += "Позиция кандидата - " + candidate_pk['position'] + '<br>'
    candidate_pk_list += "Навыки кандидата - " + candidate_pk['skills'] + '<br>'
    url = candidate_pk['picture']
    return f"<img src='{url}'> <pre> {candidate_pk_list} </pre>"


@app.route("/skills/<x>")
def page_index_skills(x):
    candidate_skill = get_by_skill(x)
    candidate_skill_list = ""
    for i in candidate_skill:
        candidate_skill_list += "Имя кандидата - " + i['name'] + '<br>'
        candidate_skill_list += "Позиция кандидата - " + i['position'] + '<br>'
        candidate_skill_list += "Навыки кандидата - " + i['skills'] + '<br>' + '<br>'
    return f'<pre> {candidate_skill_list} </pre>'


app.run(debug=True)