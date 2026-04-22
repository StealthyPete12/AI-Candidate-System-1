import re
from skill_registry import SKILL_REGISTRY, flatten_role_skills

#This is extracting the specific skills from the cv and lists the matched skills
#It then flattens all the known skills so that we can work with a simple list of skills and avoid weighting towards to specific position which improves the accuracy

def extract_skills_from_text(text: str) -> list[str]:
    """
    Extracts known technical skills from CV text using
    a centralized skill registry.

    Returns a sorted list of matched skills.
    """
    text = text.lower()

    # Flatten all known skills from the registry
    all_skills = flatten_role_skills()

    found_skills = set()

    for skill in all_skills:
        # Escape special characters and match whole skill phrases
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)