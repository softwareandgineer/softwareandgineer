def get_yesno(prompt):
    while True:
        answer = input(prompt + "yes or no:")
        if answer.lower() in ['yes', 'no']:
            return answer
        else:
            print("type in yes or no")