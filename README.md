# Yandex Music Analyzer AI 🎵✨

Yandex Music Analyzer AI — это инструмент, который использует машинное обучение для анализа плейлистов из Яндекс.Музыки и создания психологического портрета владельца. Просто вставьте ссылку на свой плейлист, и получите уникальный анализ характера, интересов и привычек!
Особенности проекта 🧠

  -🔗 Анализ плейлиста по ссылке: Сервис принимает ссылку на плейлист Яндекс.Музыки.
  -🤖 Искусственный интеллект: Используется модель для интерпретации данных о музыкальных предпочтениях.
  -✨ Эстетичный интерфейс: Проект оформлен в тёмной теме с неоновым свечением для полей ввода.
  -📊 Психологический портрет: Получите развернутое описание личности, привычек и интересов владельца плейлиста.

---

## Как это работает? 🚀

 - Пользователь вводит ссылку на плейлист Яндекс.Музыки.
 - Парсинг плейлиста извлекает данные о треках, таких как жанры, темп, текст, популярность.
 - Модель машинного обучения анализирует данные и формирует психологический портрет.
 - Результат выводится в формате диалогового окна с подсветкой.

---

<img src="https://github.com/user-attachments/assets/e29be07e-9085-4ed5-bca3-4191ea73c7d7">

---

## Установка и запуск 🛠️
### 1. Клонирование репозитория

```
git clone https://github.com/Vova2808/Yandex_Music_Analyzer_AI.git
cd Yandex_Music_Analyzer_AI
```

### 2. Установка зависимостей

Создайте виртуальное окружение (рекомендуется) и установите зависимости:

```
pip install -r requirements.txt
```

### 3 Установка LLaMA 

Переходим на сайт <a href="https://ollama.com/download/"> LLaMA </a> cкачиваем и апускаем OllamaSetup.exe

```
ollama run llama3.1
```


### 4. Запуск

Запустите локальный сервер:

```
python app.py
```

Откройте браузер и перейдите по адресу:

http://127.0.0.1:5000/

## Используемые технологии 🛠️

- Backend: Python (Flask)
- Frontend: HTML, CSS (тёмная тема с неоновым свечением)
- Парсинг данных: Yandex Music API
- Машинное обучение: Natural Language Processing (NLP)


### Спасибо, что заглянули 📋

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
</p>
