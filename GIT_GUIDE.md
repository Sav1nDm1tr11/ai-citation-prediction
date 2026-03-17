# Пошаговая инструкция: как залить проект на GitHub

## Шаг 0. Установка Git (если ещё не установлен)

### Windows
Скачай установщик с https://git-scm.com/download/win и запусти его.
Все настройки при установке можно оставить по умолчанию.

После установки у тебя появится программа **Git Bash** — это терминал, в котором мы будем работать. Открывай именно его (не обычную командную строку cmd).

### macOS
Открой Terminal и введи:
```bash
git --version
```
Если Git не установлен, система сама предложит установить — соглашайся.

### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install git
```

## Шаг 1. Настрой Git (один раз навсегда)

Открой терминал (Git Bash на Windows) и выполни две команды, подставив свои данные:

```bash
git config --global user.name "Dmitrij Savin"
git config --global user.email "savindmitrij29@gmail.com"
```

Это имя и email будут подписывать каждый твой коммит. Email должен совпадать с тем, на который зарегистрирован аккаунт GitHub.

## Шаг 2. Создай репозиторий на GitHub

1. Зайди на https://github.com и авторизуйся (или создай аккаунт)
2. Нажми зелёную кнопку **"New"** (или иди на https://github.com/new)
3. Заполни:
   - **Repository name**: `ai-citation-prediction`
   - **Description**: `Predicting AI citation probability for P&G product pages`
   - **Public** (чтобы все могли видеть — для портфолио это важно)
   - **НЕ** ставь галочки на "Add a README", "Add .gitignore", "Choose a license" — всё это уже есть в архиве
4. Нажми **"Create repository"**

GitHub покажет страницу с инструкциями — она тебе и нужна для следующего шага.

## Шаг 3. Распакуй архив

Распакуй скачанный `ai-citation-prediction.zip` в удобное место на компьютере.
Например, в `C:\Projects\ai-citation-prediction` (Windows) или `~/Projects/ai-citation-prediction` (macOS/Linux).

Проверь, что внутри папки лежат файлы напрямую (README.md, requirements.txt и т.д.), а не ещё одна вложенная папка.

## Шаг 4. Инициализируй Git и сделай первый коммит

Открой терминал (Git Bash на Windows) и перейди в папку проекта:

```bash
# Windows (Git Bash) — пример:
cd /c/Projects/ai-citation-prediction

# macOS / Linux — пример:
cd ~/Projects/ai-citation-prediction
```

Теперь выполни команды по очереди:

```bash
# 1. Инициализировать Git в этой папке
git init
```
Эта команда создаёт скрытую папку .git — теперь Git следит за изменениями в проекте.

```bash
# 2. Добавить ВСЕ файлы в «область подготовки» (staging area)
git add .
```
Точка означает «всё в текущей папке». Git теперь знает, какие файлы войдут в коммит.

```bash
# 3. Проверить, что Git «увидел» все файлы (необязательно, но полезно)
git status
```
Должны быть зелёным цветом перечислены все файлы: README.md, notebooks/, data/, plots/ и т.д.

```bash
# 4. Создать первый коммит
git commit -m "Initial commit: AI citation prediction model for P&G"
```
Коммит — это «снимок» проекта. Флаг `-m` задаёт сообщение коммита.

```bash
# 5. Переименовать ветку в main (стандарт GitHub)
git branch -M main
```

```bash
# 6. Привязать локальный репозиторий к GitHub
#    ЗАМЕНИ <your-username> на свой логин GitHub!
git remote add origin https://github.com/<your-username>/ai-citation-prediction.git
```

```bash
# 7. Отправить код на GitHub
git push -u origin main
```

При первом пуше GitHub попросит авторизацию. Откроется окно браузера — залогинься и разреши доступ.

## Шаг 5. Проверь результат

Зайди на `https://github.com/<your-username>/ai-citation-prediction` — ты увидишь:
- Все файлы проекта
- Красиво отрендеренный README с графиками
- Возможность скачать проект для любого, кто зайдёт на страницу

## Бонус: как вносить изменения в будущем

Если ты что-то поменял в проекте (например, улучшил модель), вот как обновить репозиторий:

```bash
# 1. Посмотреть, что изменилось
git status

# 2. Добавить изменённые файлы
git add .

# 3. Создать коммит с описанием изменений
git commit -m "Improve model: add new features, AUC 0.77 -> 0.80"

# 4. Отправить на GitHub
git push
```

## Частые проблемы и решения

**"fatal: not a git repository"**
Ты не в той папке. Убедись, что выполняешь команды внутри папки проекта (`cd` в неё).

**"error: failed to push some refs"**
Скорее всего, ты поставил галочку на "Add a README" при создании репозитория на GitHub, и теперь там есть файл, которого нет у тебя локально. Решение:
```bash
git pull origin main --allow-unrelated-histories
```
Потом снова `git push`.

**"Permission denied" или просит пароль**
GitHub больше не принимает пароли через HTTPS. Варианты:
1. Используй авторизацию через браузер (Git Credential Manager — обычно ставится вместе с Git на Windows)
2. Или создай Personal Access Token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token. Используй его вместо пароля.

**Большие файлы (> 100 МБ)**
GitHub не принимает файлы больше 100 МБ. Если датасет вырастет, используй Git LFS:
```bash
git lfs install
git lfs track "*.xlsx"
git add .gitattributes
```
