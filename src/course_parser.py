import json

def get_courses():
    course_info = dict()
    with open("course_info.json", "r") as f:
        course_info = json.load(f)

    return course_info['courses']

'''
if __name__ == "__main__":
    c = get_courses()
    print(json.dumps(c, indent = 4, sort_keys=True))
'''