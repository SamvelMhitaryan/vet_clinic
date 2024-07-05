# 📁 Vet_Clinic

## 📖 Кратко о проекте

Учебный проект ветеринарной клиники, сделанный по скринам с фигмы, нужный 
для обучения определения моделей по внешнему виду ресурса. Сначала проект 
был нужен строго для определения моделей, однако в последствии он оброс 
сериализаторами, вьюсетами и путями (урлами). 

---

## 🧾 TODO список (основные положения)

- [x] Инициировать проект (окружение, настройки, тестовый вывод стр. и др.).
- [x] Написанить полный CRUD для представлений. 
- [x] Наличие сущностей вет-клиник, ветеринаров, пользователей, питомцев.

---

## 💻 Запуск проекта

1. Загрузка проекта и переход в директорию 

```bash
git clone git@github.com:SamvelMhitaryan/vet_clinic.git
cd vet_clinic
```

2. Создание виртуального окружения (venv): 

```bash
python3 -m venv venv
```

3. Активация виртуального окружения (venv): 

Linux / Mac
```bash
. venv/bin/activate
```

Windows
```bash
. venv\scripts\activate
```

4. Установка зависимостей: 

```bash
pip install -r requirements.txt
```

5. Запуск: 

```bash
python3 manage.py runserver
```

# замена настроек БД и ключа django под себя.

python3 manage.py collectstatic    # \
python3 manage.py makemigrations   #  Или все одной командой через &&
python3 manage.py migrate          # /

python3 manage.py runserver 8000   # либо полноценно через gunicorn, nginx и т.д.
```
