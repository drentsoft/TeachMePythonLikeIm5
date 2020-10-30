# ------------------------------------------------------------------------------------
# Tutorial: Learn how to use continue in looping operations
# ------------------------------------------------------------------------------------

# Continue is useful when you want to break out of the current iteration of a loop without breaking out of the entire loop.
# This can help save processing time and simplify nested branches within loops as it returns to the beginning of the next iteration bypassing the rest of the code in the loop.

# Data used for evaluation.
employees = [
    {'name': 'Fred', 'evaluate': True, "salary": 5},
    {'name': 'Sally', 'evaluate': False, "salary": 10},
    {'name': 'Beth', 'evaluate': True, "salary": 7},
    {'name': 'Geoff', 'evaluate': True, "salary": 8},
]

def evaluate_employee_salaries(employees):
    for employee in employees:
        if employee['evaluate'] is False:
            print("Employee not eligible for raise this time.")
            continue  # Returns the loop to the start, bypassing the code below
        give_raise(employee)
        print("Employee salary raised to " + str(employee['salary']))

def give_raise(employee):
    employee['salary'] += 1

evaluate_employee_salaries(employees)

print("Salary evaluations complete.")

# ------------------------------------------------------------------------------------
# Challenge: You are in charge of the monster of the week hunting certain uniformed
# officers from a famous space exploration organisation for they have invaded your home.
# Design a loop that will help target ONLY officers in RED uniforms who are also ALIVE
# Uniforms can be 'red', 'yellow', 'blue' or 'neutral'
# Target only alive officers
# HINT: It is probably best to continue if the uniform is not red
# You should have two checks that result in a continue. You may do this with a single
# conditional or multiple.
# Only Leuitenant Dren, Ensign Cotton and Commander Ripley should be targeted.
# ------------------------------------------------------------------------------------

monster_name = "Generic Monster S1AB7"

potential_targets = [
    {'name': 'Leuitenant Dren', 'uniform_color': 'red', 'alive': True, 'survived': True},
    {'name': 'Ensign Cotton', 'uniform_color': 'red', 'alive': True, 'survived': True},
    {'name': 'Doctor Harries', 'uniform_color': 'blue', 'alive': True, 'survived': True},
    {'name': 'Mascot Jerry', 'uniform_color': 'red', 'alive': False, 'survived': True},
    {'name': 'Councilor Jillian', 'uniform_color': 'neutral', 'alive': True, 'survived': True},
    {'name': "Science Officer O'niel", 'uniform_color': 'yellow', 'alive': True, 'survived': True},
    {'name': 'Commander Ripley', 'uniform_color': 'red', 'alive': True, 'survived': True},
    {'name': 'Zombie Officer Ben', 'uniform_color': 'neutral', 'alive': False, 'survived': True},
]

def target_acquired(target):
    target['survived'] = False
    print("Sorry " + target['name'] + " you've been got by " + monster_name)

def away_mission():
    print("\n\nAway mission has begun...")
    for p_target in potential_targets:
        # Fill in the conditional statement(s) and add continue before the next line so that only alive red uniformed officers are targeted

        target_acquired(p_target)

    print("\n\nThe away party has returned from the surface...")
    for alive_officer in potential_targets:
        if alive_officer['survived']:
            print(alive_officer['name'] + " survived the encounter with " + monster_name)

# Uncomment the line below to start the challenge
# away_mission()
