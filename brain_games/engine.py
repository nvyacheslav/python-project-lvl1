import prompt


def start(game):
    quantity_of_rounds = 3
    number_of_round = 1
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    welcome = f'Hello, {name}'
    print('\n' + welcome)
    print(game.RULES + '\n')
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
