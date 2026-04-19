import os

from flask import Flask, render_template


app = Flask(__name__)


PROFILE = {
    "name": "Pragadeesh Sekar",
    "headline": "Test Automation and DevOps Engineer",
    "summary": (
        "Focused on test automation, CI/CD workflows, infrastructure enablement, and release "
        "quality across desktop applications, cloud environments, and platform systems."
    ),
    "contact_intro": (
        "Open to conversations around quality engineering, platform automation, CI/CD, and "
        "delivery operations."
    ),
    "email": "praga63@gmail.com",
    "phone": "+91 95859 28091",
    "github_url": "https://github.com/pragadeeshsekar",
    "github_label": "@pragadeeshsekar",
    "linkedin_url": "https://www.linkedin.com/in/pragadeeshsekar/",
    "linkedin_label": "/in/pragadeeshsekar",
}

FOCUS_AREAS = [
    "Automation Architecture",
    "CI/CD Pipelines",
    "Release Confidence",
    "Kubernetes Workflows",
    "Infrastructure Enablement",
    "Quality Strategy",
]

INSIGHTS = [
    {
        "title": "What I bring",
        "items": [
            "Automation frameworks that teams can extend instead of fight.",
            "Delivery workflows that reduce release risk and debugging time.",
            "Practical quality engineering across desktop apps, APIs, and platform environments.",
        ],
    },
    {
        "title": "How I work",
        "items": [
            "Start with failure patterns, not tool selection.",
            "Keep execution visible through pipelines, reporting, and repeatable environments.",
            "Prefer maintainable test systems over one-off automation wins.",
        ],
    },
]

IMPACT_AREAS = [
    {
        "title": "Automation Systems",
        "description": (
            "Building test frameworks and execution models that support regression coverage, "
            "suite organization, and long-term maintainability."
        ),
    },
    {
        "title": "Platform Delivery",
        "description": (
            "Improving Jenkins and cloud-native delivery flows so environments, deployments, "
            "and validation steps are easier to trust."
        ),
    },
    {
        "title": "Team Enablement",
        "description": (
            "Documenting workflows, clarifying execution standards, and helping teams adopt "
            "better automation practices without adding process drag."
        ),
    },
]

CAREER_CONTEXT = [
    "Worked across product companies and services teams in automation, QA, DevOps, and release engineering roles.",
    "Experience spans desktop application testing, API automation, infrastructure provisioning, and Kubernetes-based environments.",
    "Background includes Logitech, MediaKind, Cisco, Viasat, Nokia / Velocix, and HCL Technologies.",
]

EXPERIENCE_HIGHLIGHTS = [
    {
        "company": "Logitech",
        "role": "Lead Software Test Engineer - Automation",
        "period": "Sept 2022 - Present",
        "details": [
            "Frontend and backend automation of desktop applications using a Pytest framework.",
            "Evaluating automation coverage for new product and feature integrations.",
            "Troubleshooting issues in existing automation setups and documenting process changes.",
        ],
    },
    {
        "company": "MediaKind",
        "role": "Senior Technical Lead - Automation",
        "period": "May 2021 - Sept 2022",
        "details": [
            "Built test automation in Pytest and maintained the supporting test infrastructure.",
            "Created Jenkins CI jobs with declarative pipeline-as-code practices.",
            "Automated sanity environment setup with Terraform in GCP and Azure.",
        ],
    },
    {
        "company": "Cisco Systems",
        "role": "Software Engineer",
        "period": "July 2019 - May 2021",
        "details": [
            "Brought up all-in-one and multi-node Kubernetes clusters on Cisco UCS ESXi environments.",
            "Implemented UI automation with Protractor and API automation with PyATS and Python.",
            "Maintained Jenkins automation and developed Ansible scripts for customer-specific needs.",
        ],
    },
    {
        "company": "Earlier Roles",
        "role": "Viasat, Nokia / Velocix, HCL Technologies",
        "period": "2011 - 2019",
        "details": [
            "Worked on Ansible-based automation for satellite stream-split verification.",
            "Built automation with Python Behave, maintained Jenkins pipelines, and fixed Python module issues.",
            "Created test plans, debugged customer issues, and turned manual validation into automated coverage.",
        ],
    },
]

CERTIFICATIONS = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        focus_areas=FOCUS_AREAS,
        insights=INSIGHTS,
        impact_areas=IMPACT_AREAS,
        career_context=CAREER_CONTEXT,
        experience_highlights=EXPERIENCE_HIGHLIGHTS,
        certifications=CERTIFICATIONS,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
