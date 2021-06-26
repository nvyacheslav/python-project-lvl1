import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def start(game):
    name = welcome_user()
    print(game.RULES + '\n')    
    quantity_of_rounds = 3
    number_of_round = 1
    
    while number_of_round <= quantity_of_rounds:
        result, question, = game.get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            number_of_round += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{result}".'
            )
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')
