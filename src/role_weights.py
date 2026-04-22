#This is determining the role weights for each position 

ROLE_WEIGHTS = {
    "Data Scientist": {
        "data_libraries": 1.5,
        "machine_learning": 2.0,
        "deep_learning": 2.0,
        "statistics": 1.5,
        "programming": 1.0
    },
    "Data Analyst": {
        "analytics_libraries": 2.0,
        "databases": 1.5,
        "bi_tools": 2.0,
        "spreadsheets": 1.5,
        "programming": 1.0
    },
    "Data Engineer": {
        "data_frameworks": 2.0,
        "etl_tools": 2.0,
        "data_warehousing": 2.0,
        "streaming": 1.5,
        "programming": 1.0
    },
    "ML Engineer": {
        "ml_frameworks": 2.0,
        "deep_learning": 2.0,
        "mlops": 2.0,
        "deployment": 1.5
    },
    "DevOps Engineer": {
        "cloud": 2.5,
        "containers": 2.0,
        "orchestration": 2.5,
        "ci_cd": 2.0,
        "infrastructure_as_code": 2.5,
        "monitoring": 1.5,
        "operating_systems": 1.5,
        "networking": 1.0
    },
    "Backend Engineer": {
        "frameworks": 2.0,
        "databases": 1.5,
        "apis": 2.0,
        "programming": 1.5
    },
    "Frontend Engineer": {
        "frameworks": 2.0,
        "styling": 1.5,
        "state_management": 1.5,
        "testing": 1.0
    },
    "Full Stack Engineer": {
        "frontend": 1.5,
        "backend": 1.5,
        "databases": 1.0,
        "devops": 1.0
    }
}