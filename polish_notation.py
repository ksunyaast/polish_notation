def polish_notation():
  try:
    allowable_values = ['+', '-', '*', '/']
    data = list(input('Введите выражение: '))
    assert data[0] in allowable_values, 'Первый символ введен некорректно!'
    assert len(data) == 3, 'Всего должно быть введено 3 символа!'
    if data[0] == '+':
      answer = int(data[1]) + int(data[2])
      print('Ответ:', answer)
    elif data[0] == '-':
      answer = int(data[1]) - int(data[2])
      print('Ответ:', answer)
    elif data[0] == '*':
      answer = int(data[1]) * int(data[2])
      print('Ответ:', answer)
    elif data[0] == '/':
      answer = int(data[1]) / int(data[2])
      print('Ответ:', answer)
  except ZeroDivisionError:
    print('Деление на ноль запрещено!')
  except ValueError:
    print('Второй и третий символы должны быть цифрами!')
  except AssertionError:
    print('Всего должно быть введено 3 символа без пробелов!')
  except IndexError:
    print('Необходимо ввести данные!')
    print()
    polish_notation()
polish_notation()