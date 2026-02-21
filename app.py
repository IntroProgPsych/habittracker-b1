import sys

def interpret_score(total_score):

    if total_score >= 12:
        return "High"
    elif 6 <= total_score <= 11:
        return "Moderate"
    else:
        return "Low"

def get_valid_input(question_text):

    while True:
        try:
            user_input = input(f"{question_text} ")
            value = int(user_input)
            if 0 <= value <= 7:
                return value
            else:
                print("Error: Please enter a number between 0 and 7.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")
        finally:
            print ("------------")

def get_questions():

    return [
        # SleepRoutine
        {"text": "How many days per week do you go to bed at a consistent hour?", "habit": "SleepRoutine"},
        {"text": "How many days per week do you get at least 7 hours of sleep?", "habit": "SleepRoutine"},
        {"text": "How many days per week do you avoid screens before bed?", "habit": "SleepRoutine"},
        
        # PhysicalActivity
        {"text": "How many days per week do you exercise for at least 20 minutes?", "habit": "PhysicalActivity"},
        {"text": "How many days per week do you stretch or do mobility work?", "habit": "PhysicalActivity"},
        {"text": "How many days per week do you reach your step count goal?", "habit": "PhysicalActivity"},

        # HealthyEating
        {"text": "How many days per week do you eat at least one healthy meal?", "habit": "HealthyEating"},
        {"text": "How many days per week do you drink at least 2 liters of water?", "habit": "HealthyEating"},
        {"text": "How many days per week do you avoid processed sugars?", "habit": "HealthyEating"},

        # Mindfulness
        {"text": "How many days per week do you practice mindfulness or meditation?", "habit": "Mindfulness"},
        {"text": "How many days per week do you spend time in nature?", "habit": "Mindfulness"},
        {"text": "How many days per week do you take a moment to be grateful?", "habit": "Mindfulness"},

        # SocialConnection
        {"text": "How many days per week do you spend meaningful time with friends/family?", "habit": "SocialConnection"},
        {"text": "How many days per week do you engage in a social hobby?", "habit": "SocialConnection"},
        {"text": "How many days per week do you call or text a loved one?", "habit": "SocialConnection"},
    ]

def run_tracker():
    # start
    print("--- Healthy Habit Tracker ---")
    user_name = input("State your name:\n")
    print("Answer the following questions with the number of days per week (0-7).\n")

    questions = get_questions()
    # uniquely filtering categories, initializing scores
    categories = set(q['habit'] for q in questions)
    scores = {}
    for category in categories:
        scores[category] = 0
    # validating and adding question score to habbit sum
    for item in questions:
        days = get_valid_input(item['text'])
        scores[item['habit']] += days

    print("\n--- Habit Adherence Results ---")
    
    output_text = ""
    # looping through the index and the value of the dictionaries got through .items()
    # concating output
    for category, total in scores.items():
        interpretation = interpret_score(total)
        output_text += f"{category}: Score {total} → {interpretation}\n"
    print(output_text)
    log(user_name,output_text)

# saving the data into a log file
def log(name,output_text):
    from datetime import datetime
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(f"logs/{name}-{time_string}.log", 'w', encoding='utf-8') as outfile:
        outfile.write(output_text)
        
if __name__ == "__main__":
    run_tracker()