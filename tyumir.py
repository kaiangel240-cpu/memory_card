from PyQt5.QtCore import Qt  # Импорт ядра Qt (константы выравнивания и т.д.)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,  # Импорт виджетов PyQt5
                             QHBoxLayout, QVBoxLayout, QLabel, 
                             QMessageBox, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle  # Импорт функции для случайного перемешивания

# Класс для хранения данных вопроса
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):  # Конструктор
        self.question = question  # Текст вопроса
        self.right_answer = right_answer  # Правильный ответ
        self.wrong1 = wrong1  # Первый неправильный вариант
        self.wrong2 = wrong2  # Второй неправильный вариант
        self.wrong3 = wrong3  # Третий неправильный вариант

# Список вопросов
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')) 
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'белый', 'синий', 'красный'))
question_list.append(Question('Национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))

# Создание приложения
app = QApplication([])

# Кнопка "Ответить/Следующий вопрос"
btn_OK = QPushButton('Ответить') 

# Метка с вопросом (по центру, крупный жирный шрифт)
lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setAlignment(Qt.AlignCenter)
lb_Question.setStyleSheet("font-size: 14pt; font-weight: bold;")

# Группа для вариантов ответов
RadioGroupBox = QGroupBox("Варианты ответов") 

# Четыре радио-кнопки
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# Группа для логической связки радио-кнопок
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Layout для кнопок (2 колонки по 2 кнопки)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()   # Левая колонка
layout_ans3 = QVBoxLayout()   # Правая колонка
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
RadioGroupBox.setLayout(layout_ans1) 

# Группа для отображения результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')  # "Правильно/Неверно"
lb_Correct = QLabel('ответ будет тут!')  # Правильный ответ

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# Статистика
lb_stats = QLabel('Общее: 0 | Правильных: 0')
lb_rating = QLabel('Рейтинг: 0%')
lb_stats.setStyleSheet("font-size: 10pt; font-weight: bold; color: blue;")
lb_rating.setStyleSheet("font-size: 10pt; font-weight: bold; color: green;")

# Верхняя панель со статистикой (прижата к правому краю)
top_layout = QHBoxLayout()
top_layout.addStretch()  # Растяжка слева
stats_layout = QVBoxLayout()
stats_layout.addWidget(lb_stats, alignment=Qt.AlignRight)
stats_layout.addWidget(lb_rating, alignment=Qt.AlignRight)
top_layout.addLayout(stats_layout)

# Центрирование вопроса
question_layout = QHBoxLayout()
question_layout.addStretch()
question_layout.addWidget(lb_Question)
question_layout.addStretch()

# Блок с вариантами ответов и результатом
layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  # Скрываем результат, показываем варианты

# Кнопка по центру
layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

# Главный вертикальный layout
layout_card = QVBoxLayout()
layout_card.addLayout(top_layout, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(question_layout, stretch=1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2, stretch=3)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(10)

# Глобальные переменные
current_question_index = 0  # Индекс текущего вопроса
total_questions = len(question_list)  # Всего вопросов
test_completed = False  # Флаг завершения теста (важно!)

def show_result():
    """Переключение в режим показа результата"""
    RadioGroupBox.hide()  # Скрываем варианты
    AnsGroupBox.show()    # Показываем результат
    btn_OK.setText('Следующий вопрос')  # Меняем текст кнопки

def show_question():
    """Переключение в режим вопроса"""
    RadioGroupBox.show()   # Показываем варианты
    AnsGroupBox.hide()     # Скрываем результат
    btn_OK.setText('Ответить')  # Меняем текст кнопки
    RadioGroup.setExclusive(False)  # Отключаем эксклюзивность
    rbtn_1.setChecked(False)  # Снимаем все выделения
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # Включаем обратно

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]  # Список кнопок для удобства

def ask(q: Question):
    """Отображение вопроса"""
    shuffle(answers)  # Перемешиваем порядок ответов
    answers[0].setText(q.right_answer)  # Правильный ответ на случайное место
    answers[1].setText(q.wrong1)  # Неправильные ответы
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)  # Текст вопроса
    lb_Correct.setText(q.right_answer)  # Сохраняем правильный ответ
    show_question()  # Показываем режим вопроса

def show_correct(res):
    """Показ результата (Правильно/Неверно)"""
    lb_Result.setText(res)
    show_result()

def check_answer():
    """Проверка выбранного ответа"""
    if answers[0].isChecked():  # Если выбран правильный ответ
        window.score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    
    # Увеличиваем счётчик отвеченных вопросов ТОЛЬКО если тест не завершён
    if not test_completed:
        window.total += 1
        update_stats()

def update_stats():
    """Обновление статистики"""
    lb_stats.setText(f'Общее: {window.total} | Правильных: {window.score}')
    rating_percent = (window.score / window.total) * 100 if window.total > 0 else 0
    lb_rating.setText(f'Рейтинг: {rating_percent:.1f}%')

def next_question():
    """Переход к следующему вопросу"""
    global current_question_index, test_completed
    
    # Если тест уже завершён, ничего не делаем (важно!)
    if test_completed:
        return
    
    # Если есть ещё вопросы
    if current_question_index < total_questions:
        q = question_list[current_question_index]
        current_question_index += 1
        ask(q)
    else:
        # Тест завершён - НЕ увеличиваем счётчик, НЕ загружаем новый вопрос
        test_completed = True
        lb_Question.setText("Тест завершён!")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        lb_Result.setText(f"Итоговый результат!")
        lb_Correct.setText(f"Правильных ответов: {window.score} из {total_questions}")
        btn_OK.setEnabled(False)  # Отключаем кнопку

def check_okey():
    """Обработка нажатия кнопки"""
    if btn_OK.text() == 'Ответить':
        check_answer()  # Режим ответа
    else:
        next_question()  # Режим следующего вопроса

# Создание главного окна
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0  # Счёт правильных ответов
window.total = 0  # Всего отвеченных вопросов

btn_OK.clicked.connect(check_okey)  # Подключаем обработчик

# Запуск первого вопроса
current_question_index = 0
next_question()

window.resize(500, 450)
window.show()
app.exec()  # Запуск главного цикла приложения