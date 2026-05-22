# Импорт модулей для работы с графическим интерфейсом
from PyQt5.QtCore import Qt  # Основные возможности Qt (константы, флаги)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,  # Импорт виджетов
                             QHBoxLayout, QVBoxLayout, QLabel, 
                             QMessageBox, QRadioButton, QGroupBox, QButtonGroup,
                             QLineEdit)
from random import shuffle  # Функция для перемешивания списка
import sys  # Системные функции (для запуска приложения)

# Класс для хранения одного вопроса и вариантов ответов
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question  # Текст вопроса
        self.right_answer = right_answer  # Правильный ответ
        self.wrong1 = wrong1  # Первый неправильный вариант
        self.wrong2 = wrong2  # Второй неправильный вариант
        self.wrong3 = wrong3  # Третий неправильный вариант

# Создание списка вопросов
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')) 
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'белый', 'синий', 'красный'))
question_list.append(Question('Национальная хижина якутов', 'ураса', 'юрта', 'иглу', 'хата'))

# Создание экземпляра приложения
app = QApplication(sys.argv)

# CSS стили для оформления интерфейса
style = """
    /* Глобальные настройки */
    QWidget {
        background-color: #f8f9fa;  # Светло-серый фон по умолчанию
        font-family: 'Segoe UI', 'Arial', sans-serif;  # Шрифт
    }
    
    /* Главное окно */
    QWidget#main_window {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,  # Градиентный фон
                                    stop:0 #f8f9fa, stop:1 #e9ecef);
    }
    
    /* Стиль для кнопок (градиентный) */
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,  # Вертикальный градиент
                                    stop:0 #6366f1, stop:1 #4f46e5);  # Фиолетовые оттенки
        color: white;  # Белый текст
        border: none;  # Убираем рамку
        border-radius: 12px;  # Скругление углов
        padding: 12px 24px;  # Внутренние отступы
        font-size: 14px;  # Размер шрифта
        font-weight: 600;  # Жирность шрифта
        letter-spacing: 0.5px;  # Межбуквенное расстояние
    }
    
    QPushButton:hover {  # Стиль при наведении мыши
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #4f46e5, stop:1 #4338ca);
        transform: scale(1.02);  # Небольшое увеличение
    }
    
    QPushButton:pressed {  # Стиль при нажатии
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 #4338ca, stop:1 #3730a3);
    }
    
    QPushButton:disabled {  # Стиль для неактивной кнопки
        background: #cbd5e1;
        color: #94a3b8;
    }
    
    /* Стиль для вопроса */
    QLabel#question_label {
        background: white;  # Белый фон
        border-radius: 20px;  # Скругление углов
        padding: 30px;  # Внутренние отступы
        font-size: 20px;  # Размер шрифта
        font-weight: 700;  # Жирный шрифт
        color: #1e293b;  # Цвет текста
        border: 1px solid #e2e8f0;  # Серая рамка
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);  # Тень
    }
    
    /* Стиль для групп */
    QGroupBox {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        margin-top: 16px;  # Отступ сверху
        padding-top: 16px;
        font-size: 16px;
        font-weight: 600;
        color: #1e293b;
    }
    
    QGroupBox::title {  # Стиль заголовка группы
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
        spacing: 12px;  # Расстояние между индикатором и текстом
        border-radius: 8px;
    }
    
    QRadioButton:hover {
        background-color: #f1f5f9;  # Фон при наведении
        color: #6366f1;
    }
    
    QRadioButton:checked {  # Стиль выбранной кнопки
        color: #4f46e5;
        font-weight: 600;
    }
    
    QRadioButton::indicator {  # Стиль круглого индикатора
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
        transition: all 0.3s ease;  # Плавные переходы
    }
    
    QGroupBox:hover, QLabel#question_label:hover {
        transform: translateY(-2px);  # Подъем при наведении
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);  # Увеличенная тень
    }
"""

# Применяем стили к приложению
app.setStyleSheet(style)

# Создание кнопки "Ответить"
btn_OK = QPushButton('Ответить')
btn_OK.setCursor(Qt.PointingHandCursor)  # Меняем курсор на руку при наведении

# Создание метки для вопроса
lb_Question = QLabel('Самый сложный вопрос в мире!')
lb_Question.setObjectName("question_label")  # Устанавливаем имя для стилизации
lb_Question.setAlignment(Qt.AlignCenter)  # Выравнивание по центру
lb_Question.setWordWrap(True)  # Перенос длинных строк

# Создание группы для вариантов ответов
RadioGroupBox = QGroupBox(" Варианты ответов")
# Создание радио-кнопок для вариантов
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

# Устанавливаем курсор для всех радио-кнопок
for rbtn in [rbtn_1, rbtn_2, rbtn_3, rbtn_4]:
    rbtn.setCursor(Qt.PointingHandCursor)

# Создание группы кнопок для управления выбором
RadioGroup = QButtonGroup()
# Добавляем кнопки в группу
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# Создание горизонтального макета для кнопок
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()  # Вертикальный макет для левой колонки
layout_ans3 = QVBoxLayout()  # Вертикальный макет для правой колонки
layout_ans2.addWidget(rbtn_1)  # Добавляем первую кнопку в левую колонку
layout_ans2.addWidget(rbtn_2)  # Добавляем вторую кнопку в левую колонку
layout_ans3.addWidget(rbtn_3)  # Добавляем третью кнопку в правую колонку
layout_ans3.addWidget(rbtn_4)  # Добавляем четвертую кнопку в правую колонку

# Объединяем левую и правую колонки в горизонтальный макет
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
layout_ans1.setSpacing(20)  # Расстояние между колонками

# Устанавливаем макет в группу радио-кнопок
RadioGroupBox.setLayout(layout_ans1) 

# Создание группы для отображения результата
AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('')  # Метка для результата (правильно/неправильно)
lb_Result.setObjectName("result_label")
lb_Result.setAlignment(Qt.AlignCenter)
lb_Correct = QLabel('')  # Метка для правильного ответа
lb_Correct.setObjectName("correct_label")
lb_Correct.setAlignment(Qt.AlignCenter)

# Вертикальный макет для группы результата
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))  # Выравнивание влево-вверх
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)  # По центру горизонтали
AnsGroupBox.setLayout(layout_res)

# Создание меток для статистики
lb_stats = QLabel(' Общее: 0 | Правильных: 0')
lb_stats.setObjectName("stats_label")
lb_rating = QLabel('Рейтинг: 0%')
lb_rating.setObjectName("rating_label")

# Верхний макет для статистики
top_layout = QHBoxLayout()
top_layout.addStretch()  # Добавляем растягивающийся элемент справа
stats_layout = QHBoxLayout()  # Горизонтальное расположение статистики
stats_layout.setSpacing(10)
stats_layout.addWidget(lb_stats, alignment=Qt.AlignRight)  # Выравнивание вправо
stats_layout.addWidget(lb_rating, alignment=Qt.AlignRight)
top_layout.addLayout(stats_layout)

# Макет для вопроса
question_layout = QHBoxLayout()
question_layout.addStretch()
question_layout.addWidget(lb_Question)
question_layout.addStretch()

# Основной макет для групп (варианты и результат)
layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()  # Скрываем группу результата в начале

# Макет для кнопки
layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

# Главный макет окна
layout_card = QVBoxLayout()
layout_card.setContentsMargins(20, 20, 20, 20)  # Отступы по краям
layout_card.addLayout(top_layout, stretch=1)
layout_card.addSpacing(20)  # Добавляем отступ
layout_card.addLayout(question_layout, stretch=2)
layout_card.addSpacing(20)
layout_card.addLayout(layout_line2, stretch=3)
layout_card.addSpacing(20)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(15)  # Расстояние между элементами

# Переменные для отслеживания состояния теста
current_question_index = 0  # Индекс текущего вопроса
total_questions = len(question_list)  # Общее количество вопросов
test_completed = False  # Флаг завершения теста

# Функция показа результата
def show_result():
    RadioGroupBox.hide()  # Скрываем варианты ответов
    AnsGroupBox.show()  # Показываем результат
    btn_OK.setText('➡️ Следующий вопрос')  # Меняем текст кнопки

# Функция показа вопроса
def show_question():
    RadioGroupBox.show()  # Показываем варианты ответов
    AnsGroupBox.hide()  # Скрываем результат
    btn_OK.setText('✨ Ответить')  # Меняем текст кнопки
    RadioGroup.setExclusive(False)  # Временно отключаем исключительность выбора
    # Сбрасываем все выбранные кнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # Включаем исключительность обратно

# Список радио-кнопок
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Функция задавания вопроса
def ask(q: Question):
    shuffle(answers)  # Перемешиваем варианты ответов
    # Устанавливаем текст для каждой кнопки
    answers[0].setText(q.right_answer)  # Правильный ответ
    answers[1].setText(q.wrong1)  # Неправильный вариант 1
    answers[2].setText(q.wrong2)  # Неправильный вариант 2
    answers[3].setText(q.wrong3)  # Неправильный вариант 3
    lb_Question.setText(q.question)  # Устанавливаем текст вопроса
    lb_Correct.setText(f"✓ {q.right_answer}")  # Запоминаем правильный ответ
    show_question()  # Показываем форму вопроса

# Функция показа правильности ответа
def show_correct(res):
    if res == 'Правильно!':
        lb_Result.setText("✅ " + res)
        lb_Result.setStyleSheet("color: #10b981; font-size: 24px; font-weight: 700;")  # Зеленый цвет
    else:
        lb_Result.setText("❌ " + res)
        lb_Result.setStyleSheet("color: #ef4444; font-size: 24px; font-weight: 700;")  # Красный цвет
    show_result()  # Показываем результат

# Функция проверки ответа
def check_answer():
    if answers[0].isChecked():  # Если выбран правильный ответ (первый после перемешивания)
        window.score += 1  # Увеличиваем счетчик правильных ответов
        show_correct('Правильно!')
    else:
        # Если выбран любой неправильный вариант
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    
    if not test_completed:
        window.total += 1  # Увеличиваем счетчик всех ответов
        update_stats()  # Обновляем статистику

# Функция обновления статистики
def update_stats():
    lb_stats.setText(f' Общее: {window.total} | Правильных: {window.score}')
    # Расчет процента правильных ответов
    rating_percent = (window.score / window.total) * 100 if window.total > 0 else 0
    lb_rating.setText(f'⭐ Рейтинг: {rating_percent:.1f}%')
    
    # Меняем цвет рейтинга в зависимости от процента
    if rating_percent >= 70:
        lb_rating.setStyleSheet("color: #10b981; font-size: 13px; font-weight: 600;")  # Зеленый
    elif rating_percent >= 40:
        lb_rating.setStyleSheet("color: #f59e0b; font-size: 13px; font-weight: 600;")  # Оранжевый
    else:
        lb_rating.setStyleSheet("color: #ef4444; font-size: 13px; font-weight: 600;")  # Красный

# Функция перехода к следующему вопросу
def next_question():
    global current_question_index, test_completed  # Используем глобальные переменные
    
    if test_completed:
        return  # Если тест завершен, выходим
    
    if current_question_index < total_questions:
        q = question_list[current_question_index]  # Получаем текущий вопрос
        current_question_index += 1  # Увеличиваем индекс для следующего раза
        ask(q)  # Задаем вопрос
    else:
        test_completed = True  # Устанавливаем флаг завершения
        lb_Question.setText("🏆 Тест завершён! 🏆")  # Показываем сообщение
        RadioGroupBox.hide()  # Скрываем варианты ответов
        AnsGroupBox.show()  # Показываем результат
        lb_Result.setText("Итоговый результат!")
        lb_Result.setStyleSheet("color: #6366f1; font-size: 28px; font-weight: 700;")
        lb_Correct.setText(f"Правильных ответов: {window.score} из {total_questions}\n\n Отличная работа!")
        lb_Correct.setStyleSheet("font-size: 18px; padding: 20px;")
        btn_OK.setEnabled(False)  # Отключаем кнопку

# Обработчик нажатия кнопки
def check_okey():
    if btn_OK.text() == '✨ Ответить':  # Если кнопка в режиме "Ответить"
        check_answer()  # Проверяем ответ
    else:  # Если кнопка в режиме "Следующий вопрос"
        next_question()  # Переходим к следующему вопросу

# Создание главного окна
window = QWidget()
window.setObjectName("main_window")  # Устанавливаем имя для стилизации
window.setLayout(layout_card)  # Устанавливаем главный макет
window.setWindowTitle('🎓 Memo Card - Тестовая викторина')  # Заголовок окна
# Инициализация счетчиков как атрибутов окна
window.score = 0  # Количество правильных ответов
window.total = 0  # Общее количество отвеченных вопросов

# Подключаем обработчик нажатия кнопки
btn_OK.clicked.connect(check_okey)

# Начинаем тест с первого вопроса
current_question_index = 0
next_question()

# Устанавливаем размер окна и показываем его
window.resize(650, 600)
window.show()

# Запуск главного цикла приложения
app.exec()