#This is defining all the skills that are associated with the specific positions

SKILL_REGISTRY = {
    "Data Analyst": {
        "python", "sql", "pandas", "powerbi", "excel", "tableau", "statistics", "reporting"
    },
    "Data Engineer": {
        "python", "sql", "etl", "data pipelines", "airflow", "docker", "data warehousing", "pandas"
    },
    "Backend Engineer": {
        "python", "java", "node.js", "express", "rest apis", "sql", "docker"
    },
    "Full Stack Engineer": {
        "javascript", "react", "node.js", "express", "sql", "html", "css"
    },
    "Frontend Engineer": {
        "javascript", "react", "html", "css", "typescript", "ui design"
    },
    "ML Engineer": {
        "python", "machine learning", "tensorflow", "pytorch", "model training", "deep learning"
    },
    "DevOps Engineer": {
        "docker", "kubernetes", "aws", "ci/cd", "linux", "terraform"
    }
}

def flatten_role_skills():
    """
    Returns a flat set of all known skills across roles.
    Useful for fast membership checks.
    """
    all_skills = set()
    for skills in SKILL_REGISTRY.values():
        all_skills.update(skills)
    return all_skills
