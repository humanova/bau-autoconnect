import webbrowser
import course_parser
import schedule
import time

def request_join_course(course_id):
    r_url = f"https://bau.adobeconnect.com/{course_id}/?disclaimer-consent=true&proto=true"
    webbrowser.open(r_url)

if __name__ == "__main__":
    courses = course_parser.get_courses() 
    print("scheduling courses...")
    for c in courses:
        session_day =  c['session_day']
        session_hour = c['session_hour']
        url = c['url']
        print(f"course : {c['name']} - {session_day} at {session_hour}")
        getattr(schedule.every(), session_day).at(session_hour).do(request_join_course, url)

    while True:
        schedule.run_pending()
        time.sleep(10)