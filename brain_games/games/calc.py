from random import randint, choice


RULES = 'What is the result of the expression?'


def get_question_and_answer():
    sign = choice('-+*')
    first_num = randint(1, 20)
    sec_num = randint(1, 20)
    if sign == ('+'):
        result = first_num + sec_num
    elif sign == ('-'):
        result = first_num - sec_num
    elif sign == ('*'):
        result = first_num * sec_num
    question = f"{str(first_num)} {sign} {str(sec_num)}"
    return str(result), question
