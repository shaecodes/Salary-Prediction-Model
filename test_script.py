import requests

def encode_gender(gender):
    return 0 if gender.lower() == "male" else 1 

def encode_education(education_level):
    encoding_map = {
        "Bachelor's": 0,
        "Master's": 1,
        "PhD": 2
    }
    return encoding_map.get(education_level.lower(), -1) 

job_title_encoding = {
    'Software Engineer': 0, 'Data Analyst': 1, 'Senior Manager': 2, 'Sales Associate': 3, 'Director': 4,
    'Marketing Analyst': 5, 'Product Manager': 6, 'Sales Manager': 7, 'Marketing Coordinator': 8,
    'Senior Scientist': 9, 'Software Developer': 10, 'HR Manager': 11, 'Financial Analyst': 12, 'Project Manager': 13,
    'Customer Service Rep': 14, 'Operations Manager': 15, 'Marketing Manager': 16, 'Senior Engineer': 17,
    'Data Entry Clerk': 18, 'Sales Director': 19, 'Business Analyst': 20, 'VP of Operations': 21, 'IT Support': 22,
    'Recruiter': 23, 'Financial Manager': 24, 'Social Media Specialist': 25, 'Software Manager': 26, 'Junior Developer': 27,
    'Senior Consultant': 28, 'Product Designer': 29, 'CEO': 30, 'Accountant': 31, 'Data Scientist': 32,
    'Marketing Specialist': 33, 'Technical Writer': 34, 'HR Generalist': 35, 'Project Engineer': 36, 'Customer Success Rep': 37,
    'Sales Executive': 38, 'UX Designer': 39, 'Operations Director': 40, 'Network Engineer': 41, 'Administrative Assistant': 42,
    'Strategy Consultant': 43, 'Copywriter': 44, 'Account Manager': 45, 'Director of Marketing': 46, 'Help Desk Analyst': 47,
    'Customer Service Manager': 48, 'Business Intelligence Analyst': 49, 'Event Coordinator': 50, 'VP of Finance': 51,
    'Graphic Designer': 52, 'UX Researcher': 53, 'Social Media Manager': 54, 'Director of Operations': 55, 'Senior Data Scientist': 56,
    'Junior Accountant': 57, 'Digital Marketing Manager': 58, 'IT Manager': 59, 'Customer Service Representative': 60,
    'Business Development Manager': 61, 'Senior Financial Analyst': 62, 'Web Developer': 63, 'Research Director': 64,
    'Technical Support Specialist': 65, 'Creative Director': 66, 'Senior Software Engineer': 67, 'Human Resources Director': 68,
    'Content Marketing Manager': 69, 'Technical Recruiter': 70, 'Sales Representative': 71, 'Chief Technology Officer': 72,
    'Junior Designer': 73, 'Financial Advisor': 74, 'Junior Account Manager': 75, 'Senior Project Manager': 76, 'Principal Scientist': 77,
    'Supply Chain Manager': 78, 'Senior Marketing Manager': 79, 'Training Specialist': 80, 'Research Scientist': 81,
    'Junior Software Developer': 82, 'Public Relations Manager': 83, 'Operations Analyst': 84, 'Product Marketing Manager': 85,
    'Senior HR Manager': 86, 'Junior Web Developer': 87, 'Senior Project Coordinator': 88, 'Chief Data Officer': 89,
    'Digital Content Producer': 90, 'IT Support Specialist': 91, 'Senior Marketing Analyst': 92, 'Customer Success Manager': 93,
    'Senior Graphic Designer': 94, 'Software Project Manager': 95, 'Supply Chain Analyst': 96, 'Senior Business Analyst': 97,
    'Junior Marketing Analyst': 98, 'Office Manager': 99, 'Principal Engineer': 100, 'Junior HR Generalist': 101, 'Senior Product Manager': 102,
    'Junior Operations Analyst': 103, 'Senior HR Generalist': 104, 'Sales Operations Manager': 105, 'Senior Software Developer': 106,
    'Junior Web Designer': 107, 'Senior Training Specialist': 108, 'Senior Research Scientist': 109, 'Junior Sales Representative': 110,
    'Junior Marketing Manager': 111, 'Junior Data Analyst': 112, 'Senior Product Marketing Manager': 113, 'Junior Business Analyst': 114,
    'Senior Sales Manager': 115, 'Junior Marketing Specialist': 116, 'Junior Project Manager': 117, 'Senior Accountant': 118,
    'Director of Sales': 119, 'Junior Recruiter': 120, 'Senior Business Development Manager': 121, 'Senior Product Designer': 122,
    'Junior Customer Support Specialist': 123, 'Senior IT Support Specialist': 124, 'Junior Financial Analyst': 125,
    'Senior Operations Manager': 126, 'Director of Human Resources': 127, 'Junior Software Engineer': 128, 'Senior Sales Representative': 129,
    'Director of Product Management': 130, 'Junior Copywriter': 131, 'Senior Marketing Coordinator': 132, 'Senior Human Resources Manager': 133,
    'Junior Business Development Associate': 134, 'Senior Account Manager': 135, 'Senior Researcher': 136, 'Junior HR Coordinator': 137,
    'Director of Finance': 138, 'Junior Marketing Coordinator': 139, 'Junior Data Scientist': 140, 'Senior Operations Analyst': 141,
    'Senior Human Resources Coordinator': 142, 'Senior UX Designer': 143, 'Junior Product Manager': 144, 'Senior Marketing Specialist': 145,
    'Senior IT Project Manager': 146, 'Senior Quality Assurance Analyst': 147, 'Director of Sales and Marketing': 148, 'Senior Account Executive': 149,
    'Director of Business Development': 150, 'Junior Social Media Manager': 151, 'Senior Human Resources Specialist': 152, 'Senior Data Analyst': 153,
    'Director of Human Capital': 154, 'Junior Advertising Coordinator': 155, 'Junior UX Designer': 156, 'Senior Marketing Director': 157,
    'Senior IT Consultant': 158, 'Senior Financial Advisor': 159, 'Junior Business Operations Analyst': 160, 'Junior Social Media Specialist': 161,
    'Senior Product Development Manager': 162, 'Junior Operations Manager': 163, 'Senior Software Architect': 164, 'Junior Research Scientist': 165,
    'Senior Financial Manager': 166, 'Senior HR Specialist': 167, 'Senior Data Engineer': 168, 'Junior Operations Coordinator': 169,
    'Director of HR': 170, 'Senior Operations Coordinator': 171, 'Junior Financial Advisor': 172, 'Director of Engineering': 173
}

def encode_job_title(job_title):
    return job_title_encoding.get(job_title, -1)

url = 'http://127.0.0.1:5000/predict'

age = input("Enter Age: ")
gender_input = input("Enter Gender (male or female): ")
education_input = input("Enter Education Level (Bachelor's/Master's/PhD): ")
job_title_input = input("Enter Job Title: ")
experience = float(input("Enter Years of Experience: "))


gender = encode_gender(gender_input)
education_level = encode_education(education_input)
job_title = encode_job_title(job_title_input)


features = [age, gender, education_level, job_title, experience]

data = {
    'features': features
}

response = requests.post(url, json=data)
salary = response.json().get('salary')  

if salary is not None:
    formatted_salary = f"{salary:.2f}"  
    print(f"Predicted Salary: ${formatted_salary}")
else:
    print("Error: No salary data received.")
