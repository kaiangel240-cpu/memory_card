from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QHBoxLayout, QVBoxLayout, QLabel, 
                             QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')) 
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'белый', 'синий', 'красный'))
question_list.append(Question('Национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))

app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setAlignment(Qt.AlignCenter)  # Выравнивание вопроса по центру
lb_Question.setStyleSheet("font-size: 14pt; font-weight: bold;")

RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Виджеты для статистики
lb_stats = QLabel('Общее: 0 | Правильных: 0')
lb_rating = QLabel('Рейтинг: 0%')
lb_stats.setStyleSheet("font-size: 10pt; font-weight: bold; color: blue;")
lb_rating.setStyleSheet("font-size: 10pt; font-weight: bold; color: green;")

# Создаём верхнюю панель со статистикой справа
top_layout = QHBoxLayout()
top_layout.addStretch()  # Растяжение слева, чтобы прижать статистику к правому краю
stats_layout = QVBoxLayout()
stats_layout.addWidget(lb_stats, alignment=Qt.AlignRight)
stats_layout.addWidget(lb_rating, alignment=Qt.AlignRight)
top_layout.addLayout(stats_layout)

# Основной layout для вопроса (по центру)
question_layout = QHBoxLayout()
question_layout.addStretch()
question_layout.addWidget(lb_Question)
question_layout.addStretch()

# Layout для вариантов ответов
layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

# Layout для кнопки
layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

# Основной вертикальный layout
layout_card = QVBoxLayout()
layout_card.addLayout(top_layout, stretch=1)  # Статистика сверху справа
layout_card.addStretch(1)  # Отступ
layout_card.addLayout(question_layout, stretch=1)  # Вопрос по центру
layout_card.addStretch(1)  # Отступ
layout_card.addLayout(layout_line2, stretch=3)  # Варианты ответов
layout_card.addStretch(1)  # Отступ
layout_card.addLayout(layout_line3, stretch=1)  # Кнопка
layout_card.addStretch(1)  # Отступ снизу
layout_card.setSpacing(10)

# Переменные для отслеживания текущего вопроса
current_question_index = 0
total_questions = len(question_list)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    
    # Обновляем статистику
    update_stats()

def update_stats():
    lb_stats.setText(f'Общее: {window.total} | Правильных: {window.score}')
    rating_percent = (window.score / window.total) * 100 if window.total > 0 else 0
    lb_rating.setText(f'Рейтинг: {rating_percent:.1f}%')

def next_question():
    global current_question_index
    
    # Увеличиваем счётчик отвеченных вопросов только если это не первый запуск
    if hasattr(window, 'question_answered'):
        window.total += 1
    else:
        window.total = 1
        window.question_answered = True
    
    update_stats()
    
    # Переходим к следующему вопросу по порядку
    if current_question_index < total_questions:
        q = question_list[current_question_index]
        current_question_index += 1
        ask(q)
    else:
        # Все вопросы закончились
        lb_Question.setText("Тест завершён!")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        lb_Result.setText(f"Итоговый результат!")
        lb_Correct.setText(f"Правильных ответов: {window.score} из {total_questions}")
        btn_OK.setEnabled(False)

def check_okey():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0

btn_OK.clicked.connect(check_okey)

# Запускаем первый вопрос
current_question_index = 0
next_question()

window.resize(500, 450)
window.show()
app.exec()