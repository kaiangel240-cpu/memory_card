from PyQt5.QtCore import Qt  # Импорт модуля Qt с константами (выравнивание, курсоры и т.д.)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,  # Импорт виджетов для создания интерфейса
                             QHBoxLayout, QVBoxLayout, QLabel,  # Импорт менеджеров компоновки и меток
                             QMessageBox, QRadioButton, QGroupBox, QButtonGroup,  # Импорт диалогов, радио-кнопок, групп
                             QLineEdit)  # Импорт поля ввода текста
from random import shuffle  # Импорт функции для случайного перемешивания списка
import sys  # Импорт системного модуля для работы с аргументами командной строки

# Определение класса Question для хранения данных одного вопроса
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):  # Конструктор класса
        self.question = question  # Сохраняем текст вопроса
        self.right_answer = right_answer  # Сохраняем правильный ответ
        self.wrong1 = wrong1  # Сохраняем первый неправильный ответ
        self.wrong2 = wrong2  # Сохраняем второй неправильный ответ
        self.wrong3 = wrong3  # Сохраняем третий неправильный ответ

# Создаём пустой список для хранения всех вопросов
question_list = []
# Добавляем первый вопрос (о языке Бразилии)
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')) 
# Добавляем второй вопрос (о цветах флага России)
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'белый', 'синий', 'красный'))
# Добавляем третий вопрос (о жилище якутов)
question_list.append(Question('Национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))

# Создаём экземпляр приложения, передаём аргументы командной строки
app = QApplication(sys.argv)

# Строка со стилями для кнопок в современном веб-стиле
button_style = """
    QPushButton {  # Селектор для всех кнопок QPushButton
        background-color: #3498db;  # Синий цвет фона
        color: white;  # Белый цвет текста
        border-radius: 5px;  # Скругление углов на 5 пикселей
        padding: 10px 20px;  # Внутренние отступы: 10px сверху/снизу, 20px слева/справа
        font-size: 16px;  # Размер шрифта 16 пикселей
        font-weight: bold;  # Жирное начертание шрифта
        border: none;  # Убираем стандартную рамку
    }
    QPushButton:hover {  # Стиль при наведении курсора на кнопку
        background-color: #2980b9;  # Более тёмный синий цвет
    }
    QPushButton:pressed {  # Стиль при нажатии на кнопку
        background-color: #1a5276;  # Самый тёмный синий цвет
    }
    QPushButton:disabled {  # Стиль для отключённой кнопки
        background-color: #95a5a6;  # Серый цвет фона
        color: #ecf0f1;  # Светло-серый цвет текста
    }
"""

# Применяем глобальную стилизацию ко всему приложению
app.setStyleSheet("""
    QWidget {  # Стиль для всех виджетов
        background-color: #f8f9fa;  # Светло-серый фон
        font-family: 'Segoe UI', Arial;  # Шрифт как в современных приложениях
    }
    
    QLabel#question_label {  # Стиль для метки с именем "question_label"
        font-size: 18pt;  # Размер шрифта 18 пунктов
        font-weight: bold;  # Жирное начертание
        color: #2c3e50;  # Тёмно-синий цвет текста
        padding: 20px;  # Внутренние отступы 20 пикселей
        background: white;  # Белый фон
        border-radius: 15px;  # Скругление углов
    }
    
    QGroupBox {  # Стиль для групп (рамок с заголовком)
        font-size: 14pt;  # Размер шрифта заголовка
        font-weight: bold;  # Жирное начертание
        border: 2px solid #bdc3c7;  # Серая рамка толщиной 2px
        border-radius: 10px;  # Скругление углов рамки
        margin-top: 15px;  # Отступ сверху для заголовка
        padding-top: 15px;  # Внутренний отступ сверху
        background-color: white;  # Белый фон группы
    }
    
    QGroupBox::title {  # Стиль для заголовка группы
        subcontrol-origin: margin;  # Позиционирование относительно margin
        left: 10px;  # Отступ слева
        padding: 0 10px 0 10px;  # Горизонтальные отступы для заголовка
        color: #2c3e50;  # Цвет текста заголовка
    }
    
    QRadioButton {  # Стиль для радио-кнопок
        font-size: 12pt;  # Размер шрифта
        padding: 8px;  # Внутренние отступы
        color: #2c3e50;  # Цвет текста
        spacing: 10px;  # Расстояние между индикатором и текстом
    }
    
    QRadioButton:hover {  # Стиль радио-кнопки при наведении
        color: #3498db;  # Синий цвет текста
    }
    
    QRadioButton:checked {  # Стиль выбранной радио-кнопки
        color: #2980b9;  # Тёмно-синий цвет текста
        font-weight: bold;  # Жирное начертание
    }
""")

# Создаём кнопку "Ответить"
btn_OK = QPushButton('Ответить')
# Применяем отдельный стиль для кнопки (из переменной button_style)
btn_OK.setStyleSheet(button_style)
# Меняем курсор на руку при наведении на кнопку
btn_OK.setCursor(Qt.PointingHandCursor)

# Создаём метку для отображения вопроса
lb_Question = QLabel('Самый сложный вопрос в мире!')
# Устанавливаем уникальное имя для применения стилей
lb_Question.setObjectName("question_label")
# Выравниваем текст по центру
lb_Question.setAlignment(Qt.AlignCenter)
# Разрешаем перенос длинных строк
lb_Question.setWordWrap(True)

# Создаём группу для вариантов ответов
RadioGroupBox = QGroupBox("Варианты ответов") 
# Создаём 4 радио-кнопки для вариантов
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# Устанавливаем курсор-руку для всех радио-кнопок
for rbtn in [rbtn_1, rbtn_2, rbtn_3, rbtn_4]:
    rbtn.setCursor(Qt.PointingHandCursor)  # Меняем курсор на руку

# Создаём группу для логического объединения радио-кнопок
RadioGroup = QButtonGroup()
# Добавляем каждую кнопку в группу (чтобы можно было выбрать только одну)
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Создаём горизонтальный layout для размещения двух колонок
layout_ans1 = QHBoxLayout()   
# Создаём вертикальный layout для левой колонки
layout_ans2 = QVBoxLayout() 
# Создаём вертикальный layout для правой колонки
layout_ans3 = QVBoxLayout()
# Добавляем первые две кнопки в левую колонку
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
# Добавляем последние две кнопки в правую колонку
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

# Добавляем обе колонки в горизонтальный layout
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
# Устанавливаем расстояние между колонками
layout_ans1.setSpacing(20)

# Устанавливаем layout в группу вариантов ответов
RadioGroupBox.setLayout(layout_ans1) 

# Создаём группу для отображения результата
AnsGroupBox = QGroupBox("Результат теста")
# Создаём метку для текста "Правильно/Неверно"
lb_Result = QLabel('прав ты или нет?')
# Устанавливаем уникальное имя для стилизации
lb_Result.setObjectName("result_label")
# Выравниваем текст по центру
lb_Result.setAlignment(Qt.AlignCenter)
# Создаём метку для отображения правильного ответа
lb_Correct = QLabel('ответ будет тут!')
lb_Correct.setObjectName("correct_label")
lb_Correct.setAlignment(Qt.AlignCenter)

# Создаём вертикальный layout для группы результатов
layout_res = QVBoxLayout()
# Добавляем метку результата (выравнивание влево-вверх)
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# Добавляем метку с правильным ответом (по центру с растяжением)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
# Устанавливаем layout в группу результатов
AnsGroupBox.setLayout(layout_res)

# Создаём метку для общей статистики
lb_stats = QLabel('Общее: 0 | Правильных: 0')
lb_stats.setObjectName("stats_label")
# Создаём метку для рейтинга в процентах
lb_rating = QLabel('Рейтинг: 0%')
lb_rating.setObjectName("rating_label")

# Создаём горизонтальный layout для верхней панели
top_layout = QHBoxLayout()
# Добавляем растяжку слева (прижимает содержимое вправо)
top_layout.addStretch()
# Создаём горизонтальный layout для статистики (чтобы разместить рядом)
stats_layout = QHBoxLayout()
# Устанавливаем расстояние между элементами статистики
stats_layout.setSpacing(10)
# Добавляем метку статистики с выравниванием вправо
stats_layout.addWidget(lb_stats, alignment=Qt.AlignRight)
# Добавляем метку рейтинга с выравниванием вправо
stats_layout.addWidget(lb_rating, alignment=Qt.AlignRight)
# Добавляем layout статистики в верхнюю панель
top_layout.addLayout(stats_layout)

# Создаём горизонтальный layout для центрирования вопроса
question_layout = QHBoxLayout()
# Добавляем растяжку слева
question_layout.addStretch()
# Добавляем метку вопроса
question_layout.addWidget(lb_Question)
# Добавляем растяжку справа
question_layout.addStretch()

# Создаём горизонтальный layout для групп (варианты и результат)
layout_line2 = QHBoxLayout()
# Добавляем группу вариантов ответов
layout_line2.addWidget(RadioGroupBox)   
# Добавляем группу результатов
layout_line2.addWidget(AnsGroupBox)  
# Скрываем группу результатов (показываем только варианты ответов)
AnsGroupBox.hide() 

# Создаём горизонтальный layout для кнопки
layout_line3 = QHBoxLayout()
# Добавляем растяжку слева с весом 1
layout_line3.addStretch(1)
# Добавляем кнопку по центру с весом 2 (занимает больше места)
layout_line3.addWidget(btn_OK, stretch=2) 
# Добавляем растяжку справа с весом 1
layout_line3.addStretch(1)

# Создаём главный вертикальный layout для всего окна
layout_card = QVBoxLayout()
# Устанавливаем внешние отступы для всего содержимого
layout_card.setContentsMargins(20, 20, 20, 20)
# Добавляем верхнюю панель со статистикой (вес 1)
layout_card.addLayout(top_layout, stretch=1)
# Добавляем вертикальный отступ в 20 пикселей
layout_card.addSpacing(20)
# Добавляем блок с вопросом (вес 2 - больше места)
layout_card.addLayout(question_layout, stretch=2)
# Добавляем отступ в 20 пикселей
layout_card.addSpacing(20)
# Добавляем блок с вариантами/результатом (вес 3 - самый большой)
layout_card.addLayout(layout_line2, stretch=3)
# Добавляем отступ в 20 пикселей
layout_card.addSpacing(20)
# Добавляем блок с кнопкой (вес 1)
layout_card.addLayout(layout_line3, stretch=1)
# Устанавливаем расстояние между элементами
layout_card.setSpacing(15)

# Переменная для хранения индекса текущего вопроса
current_question_index = 0
# Общее количество вопросов в списке
total_questions = len(question_list)
# Флаг завершения теста (изначально False - тест не завершён)
test_completed = False

# Функция переключения в режим показа результата
def show_result():
    RadioGroupBox.hide()  # Скрываем группу с вариантами ответов
    AnsGroupBox.show()    # Показываем группу с результатом
    btn_OK.setText('Следующий вопрос')  # Меняем текст кнопки

# Функция переключения в режим вопроса
def show_question():
    RadioGroupBox.show()  # Показываем группу с вариантами
    AnsGroupBox.hide()    # Скрываем группу с результатом
    btn_OK.setText('Ответить')  # Меняем текст кнопки
    RadioGroup.setExclusive(False)  # Временно отключаем эксклюзивность выбора
    rbtn_1.setChecked(False)  # Снимаем выделение с 1-й кнопки
    rbtn_2.setChecked(False)  # Снимаем выделение со 2-й кнопки
    rbtn_3.setChecked(False)  # Снимаем выделение с 3-й кнопки
    rbtn_4.setChecked(False)  # Снимаем выделение с 4-й кнопки
    RadioGroup.setExclusive(True)  # Включаем эксклюзивность обратно

# Список всех радио-кнопок для удобного доступа по индексу
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Функция отображения вопроса на экране
def ask(q: Question):
    shuffle(answers)  # Перемешиваем порядок кнопок (чтобы правильный ответ был на случайном месте)
    answers[0].setText(q.right_answer)  # На 1-ю кнопку - правильный ответ
    answers[1].setText(q.wrong1)  # На 2-ю кнопку - 1-й неправильный
    answers[2].setText(q.wrong2)  # На 3-ю кнопку - 2-й неправильный
    answers[3].setText(q.wrong3)  # На 4-ю кнопку - 3-й неправильный
    lb_Question.setText(q.question)  # Устанавливаем текст вопроса
    lb_Correct.setText(q.right_answer)  # Сохраняем правильный ответ для отображения
    show_question()  # Переключаем интерфейс в режим вопроса

# Функция отображения результата (Правильно/Неверно)
def show_correct(res):
    if res == 'Правильно!':  # Если ответ правильный
        lb_Result.setText("✅ " + res)  # Добавляем зелёную галочку
        lb_Result.setStyleSheet("color: #10b981; font-size: 24px; font-weight: 700;")  # Зелёный стиль
    else:  # Если ответ неправильный
        lb_Result.setText("❌ " + res)  # Добавляем красный крестик
        lb_Result.setStyleSheet("color: #ef4444; font-size: 24px; font-weight: 700;")  # Красный стиль
    show_result()  # Переключаем интерфейс в режим результата

# Функция проверки выбранного ответа
def check_answer():
    if answers[0].isChecked():  # Если выбран правильный ответ (первая кнопка после перемешивания)
        window.score += 1  # Увеличиваем счётчик правильных ответов
        show_correct('Правильно!')  # Показываем "Правильно!"
    else:  # Если выбран любой другой вариант
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():  # Если что-то выбрано
            show_correct('Неверно!')  # Показываем "Неверно!"
    
    # Увеличиваем счётчик отвеченных вопросов только если тест не завершён
    if not test_completed:
        window.total += 1  # Увеличиваем общее количество отвеченных вопросов
        update_stats()  # Обновляем отображение статистики

# Функция обновления статистики
def update_stats():
    lb_stats.setText(f'Общее: {window.total} | Правильных: {window.score}')  # Обновляем текст статистики
    rating_percent = (window.score / window.total) * 100 if window.total > 0 else 0  # Вычисляем процент
    lb_rating.setText(f'Рейтинг: {rating_percent:.1f}%')  # Обновляем рейтинг (1 знак после запятой)
    
    # Меняем цвет рейтинга в зависимости от процента правильных ответов
    if rating_percent >= 70:  # Если 70% и выше
        lb_rating.setStyleSheet("color: #10b981; font-size: 13px; font-weight: 600;")  # Зелёный
    elif rating_percent >= 40:  # Если от 40% до 69%
        lb_rating.setStyleSheet("color: #f59e0b; font-size: 13px; font-weight: 600;")  # Оранжевый
    else:  # Если меньше 40%
        lb_rating.setStyleSheet("color: #ef4444; font-size: 13px; font-weight: 600;")  # Красный

# Функция перехода к следующему вопросу
def next_question():
    global current_question_index, test_completed  # Используем глобальные переменные
    
    if test_completed:  # Если тест уже завершён
        return  # Ничего не делаем (выход из функции)
    
    if current_question_index < total_questions:  # Если остались вопросы
        q = question_list[current_question_index]  # Берём текущий вопрос
        current_question_index += 1  # Увеличиваем индекс для следующего раза
        ask(q)  # Отображаем вопрос
    else:  # Если вопросы закончились
        test_completed = True  # Устанавливаем флаг завершения теста
        lb_Question.setText("🏆 Тест завершён! 🏆")  # Меняем текст вопроса на поздравление
        RadioGroupBox.hide()  # Скрываем варианты ответов
        AnsGroupBox.show()  # Показываем группу результата
        lb_Result.setText("📈 Итоговый результат!")  # Текст итогового результата
        lb_Result.setStyleSheet("color: #6366f1; font-size: 28px; font-weight: 700;")  # Фиолетовый стиль
        lb_Correct.setText(f"Правильных ответов: {window.score} из {total_questions}\n\n🎉 Отличная работа! 🎉")  # Финальный счёт
        lb_Correct.setStyleSheet("font-size: 18px; padding: 20px;")  # Стиль финального сообщения
        btn_OK.setEnabled(False)  # Отключаем кнопку (тест завершён)

# Функция-обработчик нажатия на кнопку
def check_okey():
    if btn_OK.text() == 'Ответить':  # Если кнопка в режиме "Ответить"
        check_answer()  # Проверяем ответ пользователя
    else:  # Если кнопка в режиме "Следующий вопрос"
        next_question()  # Переходим к следующему вопросу

# Создаём главное окно приложения
window = QWidget()
# Устанавливаем уникальное имя для стилизации
window.setObjectName("main_window")
# Устанавливаем layout для окна
window.setLayout(layout_card)
# Устанавливаем заголовок окна
window.setWindowTitle('🎓 Memo Card - Тестовая викторина')
# Добавляем атрибуты для хранения счёта
window.score = 0  # Количество правильных ответов
window.total = 0  # Общее количество отвеченных вопросов

# Подключаем сигнал нажатия кнопки к функции-обработчику
btn_OK.clicked.connect(check_okey)

# Начинаем тест: загружаем первый вопрос
current_question_index = 0  # Сбрасываем индекс (хотя он и так 0)
next_question()  # Загружаем первый вопрос

# Устанавливаем размер окна (ширина 650, высота 600)
window.resize(650, 600)
# Показываем окно пользователю
window.show()
# Запускаем главный цикл обработки событий приложения
app.exec()