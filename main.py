from utils import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def page_index():
    """Представление списка всех кандидатов"""
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id: int):
    """Представление информации об одном кандидате"""
    candidate = get_candidate(candidate_id)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search(candidate_name: str):
    """Представление поиска кандидатов по имени"""
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count=len(candidates))


@app.route("/skill/<skill_name>")
def page_skill(skill_name: str):
    """Представление поиска кандидатов по скиллу"""
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, count=len(candidates), candidates=candidates)


if __name__ == "__main__":
    app.run()
