import json


def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as f:
        candidates = json.load(f)
        return candidates


def get_all():
    get_all_candidates = load_candidates()
    for i in get_all_candidates:
        print(i)


def get_by_pk(pk):
    get_pk_candidates = load_candidates()
    for i in get_pk_candidates:
        if i['pk'] == pk:
            return i


def get_by_skill(skill_name):
    get_skill_candidates = load_candidates()
    candidates_skills = []
    for i in get_skill_candidates:
        skills_list = i['skills'].lower().split(', ')
        if skill_name in skills_list:
            candidates_skills.append(i)
    return candidates_skills


















