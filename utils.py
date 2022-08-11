import os
import json

from typing import List, Dict


def load_candidates_from_json() -> List[Dict]:
    """Возвращает список всех кандидатов"""
    file = os.path.join("data", "candidates.json")

    with open(file, encoding="UTF-8") as data:
        candidates = json.load(data)
    return candidates


def get_candidate(candidate_id: int) -> Dict:
    """Возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> List[Dict]:
    """Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()

    candidates_list = []
    for candidate in candidates:
        if candidate_name in candidate["name"].split():
            candidates_list.append(candidate)
    return candidates_list


def get_candidates_by_skill(skill_name: str) -> List[Dict]:
    """Возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json()

    candidates_list = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates_list.append(candidate)
    return candidates_list
