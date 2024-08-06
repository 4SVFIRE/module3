def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    email = ['.ru', '.com', '.net']
    if not recipient.count('@') or not sender.count('@'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if not any(i in recipient for i in email) or not any(i in sender for i in email):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')








