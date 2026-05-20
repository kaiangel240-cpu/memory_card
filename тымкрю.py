from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QHBoxLayout, QVBoxLayout, QLabel, 
                             QMessageBox, QRadioButton, QGroupBox, QButtonGroup,
                             QLineEdit)
from random import shuffle
import sys

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

app = QApplication(sys.argv)

style = """
    /* Глобальные настройки */
    QWidget {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    
    /* Главное окно */
    QWidget#main_window {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                    stop:0 #f8f9fa, stop:1 #e9ecef);
    }
    
    /* Стиль для кнопок (градиентный) */
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #6366f1, stop:1 #4f46e5);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #4f46e5, stop:1 #4338ca);
        transform: scale(1.02);
    }
    
    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #4338ca, stop:1 #3730a3);
    }
    
    QPushButton:disabled {
        background: #cbd5e1;
        color: #94a3b8;
    }
    
    /* Стиль для вопроса */
    QLabel#question_label {
        background: white;
        border-radius: 20px;
        padding: 30px;
        font-size: 20px;
        font-weight: 700;
        color: #1e293b;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Стиль для групп */
    QGroupBox {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        margin-top: 16px;
        padding-top: 16px;
        font-size: 16px;
        font-weight: 600;
        color: #1e293b;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 16px;
        padding: 0 8px 0 8px;
        background: white;
        color: #6366f1;
    }
    
    /* Стиль для радио-кнопок */
    QRadioButton {
        font-size: 14px;
        padding: 10px;
        color: #334155;
        spacing: 12px;
        border-radius: 8px;
    }
    
    QRadioButton:hover {
        background-color: #f1f5f9;
        color: #6366f1;
    }
    
    QRadioButton:checked {
        color: #4f46e5;
        font-weight: 600;
    }
    
    QRadioButton::indicator {
        width: 18px;
        height: 18px;
        border-radius: 9px;
        border: 2px solid #cbd5e1;
        background: white;
    }
    
    QRadioButton::indicator:hover {
        border-color: #6366f1;
    }
    
    QRadioButton::indicator:checked {
        background: #6366f1;
        border-color: #6366f1;
    }
    
    /* Стиль для результата */
    QLabel#result_label {
        font-size: 24px;
        font-weight: 700;
        padding: 20px;
        border-radius: 16px;
    }
    
    QLabel#correct_label {
        font-size: 16px;
        font-weight: 500;
        color: #10b981;
        background: #f0fdf4;
        padding: 12px;
        border-radius: 12px;
    }
    
    /* Стиль для статистики */
    QLabel#stats_label {
        background: white;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
        color: #475569;
        border: 1px solid #e2e8f0;
    }
    
    QLabel#rating_label {
        background: white;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid #e2e8f0;
    }
    
    /* Анимация для карточек */
    QGroupBox, QLabel#question_label {
        transition: all 0.3s ease;
    }
    
    QGroupBox:hover, QLabel#question_label:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
"""

app.setStyleSheet(style)

btn_OK = QPushButton('Ответить')
btn_OK.setCursor(Qt.PointingHandCursor)  # Меняем курсор на руку

lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setObjectName("question_label")
lb_Question.setAlignment(Qt.AlignCenter)
lb_Question.setWordWrap(True)  # Перенос длинных строк

RadioGroupBox = QGroupBox(" Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# Устанавливаем курсор для радио-кнопок
for rbtn in [rbtn_1, rbtn_2, rbtn_3, rbtn_4]:
    rbtn.setCursor(Qt.PointingHandCursor)

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
layout_ans1.setSpacing(20)

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('')
lb_Result.setObjectName("result_label")
lb_Result.setAlignment(Qt.AlignCenter)
lb_Correct = QLabel('')
lb_Correct.setObjectName("correct_label")
lb_Correct.setAlignment(Qt.AlignCenter)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

lb_stats = QLabel(' Общее: 0 | Правильных: 0')
lb_stats.setObjectName("stats_label")
lb_rating = QLabel('Рейтинг: 0%')
lb_rating.setObjectName("rating_label")

top_layout = QHBoxLayout()
top_layout.addStretch()
stats_layout = QHBoxLayout()  # Горизонтальное расположение статистики
stats_layout.setSpacing(10)
stats_layout.addWidget(lb_stats, alignment=Qt.AlignRight)
stats_layout.addWidget(lb_rating, alignment=Qt.AlignRight)
top_layout.addLayout(stats_layout)

question_layout = QHBoxLayout()
question_layout.addStretch()
question_layout.addWidget(lb_Question)
question_layout.addStretch()

layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.setContentsMargins(20, 20, 20, 20)  # Отступы по краям
layout_card.addLayout(top_layout, stretch=1)
layout_card.addSpacing(20)
layout_card.addLayout(question_layout, stretch=2)
layout_card.addSpacing(20)
layout_card.addLayout(layout_line2, stretch=3)
layout_card.addSpacing(20)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(15)

current_question_index = 0
total_questions = len(question_list)
test_completed = False

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('➡️ Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('✨ Ответить')
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
    lb_Correct.setText(f"✓ {q.right_answer}")
    show_question() 

def show_correct(res):
    if res == 'Правильно!':
        lb_Result.setText("✅ " + res)
        lb_Result.setStyleSheet("color: #10b981; font-size: 24px; font-weight: 700;")
    else:
        lb_Result.setText("❌ " + res)
        lb_Result.setStyleSheet("color: #ef4444; font-size: 24px; font-weight: 700;")
    show_result()

def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    
    if not test_completed:
        window.total += 1
        update_stats()

def update_stats():
    lb_stats.setText(f' Общее: {window.total} | Правильных: {window.score}')
    rating_percent = (window.score / window.total) * 100 if window.total > 0 else 0
    lb_rating.setText(f'⭐ Рейтинг: {rating_percent:.1f}%')
    
    # Меняем цвет рейтинга
    if rating_percent >= 70:
        lb_rating.setStyleSheet("color: #10b981; font-size: 13px; font-weight: 600;")
    elif rating_percent >= 40:
        lb_rating.setStyleSheet("color: #f59e0b; font-size: 13px; font-weight: 600;")
    else:
        lb_rating.setStyleSheet("color: #ef4444; font-size: 13px; font-weight: 600;")

def next_question():
    global current_question_index, test_completed
    
    if test_completed:
        return
    
    if current_question_index < total_questions:
        q = question_list[current_question_index]
        current_question_index += 1
        ask(q)
    else:
        test_completed = True
        lb_Question.setText("🏆 Тест завершён! 🏆")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        lb_Result.setText("Итоговый результат!")
        lb_Result.setStyleSheet("color: #6366f1; font-size: 28px; font-weight: 700;")
        lb_Correct.setText(f"Правильных ответов: {window.score} из {total_questions}\n\n Отличная работа!")
        lb_Correct.setStyleSheet("font-size: 18px; padding: 20px;")
        btn_OK.setEnabled(False)

def check_okey():
    if btn_OK.text() == '✨ Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setObjectName("main_window")
window.setLayout(layout_card)
window.setWindowTitle('🎓 Memo Card - Тестовая викторина')
window.score = 0
window.total = 0

btn_OK.clicked.connect(check_okey)

current_question_index = 0
next_question()

window.resize(650, 600)
window.show()
app.exec()