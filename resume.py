import json

def parse_resume(resume_text):
    lines = resume_text.strip().split('\n')
    resume = {
        "name": "",
        "contact_information": {
            "email": "",
            "phone": "",
            "address": ""
        },
        "summary": "",
        "work_experience": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "projects": []
    }

    # Implement parsing logic here based on the resume structure

    return resume

if __name__ == "__main__":
    resume_text = """
    John Doe
    123 Main St, Springfield, IL 62701
    Email: john.doe@example.com
    Phone: (555) 555-5555

    Summary:
    Experienced software engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success.

    Work Experience:
    1. ABC Corp - Software Engineer
       January 2020 - Present
       - Developed web applications using JavaScript, React, and Node.js.
       - Collaborated with cross-functional teams to define project requirements and deliverables.

    2. XYZ Inc. - Junior Developer
       June 2017 - December 2019
       - Assisted in the development of internal tools using Python and Django.
       - Conducted code reviews and provided feedback to peers.

    Education:
    1. University of Illinois - Bachelor of Science in Computer Science
       August 2013 - May 2017

    Skills:
    - JavaScript
    - React
    - Node.js
    - Python
    - Django

    Certifications:
    - AWS Certified Solutions Architect

    Projects:
    1. Project Management Tool
       - Developed a project management tool using React and Node.js.
       - Integrated with third-party APIs for task automation.
    """

    parsed_resume = parse_resume(resume_text)
    print(json.dumps(parsed_resume, indent=2))
