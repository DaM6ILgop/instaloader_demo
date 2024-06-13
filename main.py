import os
import instaloader
import re

def download_instagram_video(url, download_folder="downloads", username=None):
    # Создаём папку для загрузок, если она не существует
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

   
    L = instaloader.Instaloader(dirname_pattern=download_folder)

    # Войти в аккаунт, если указано имя пользователя
    if username:
        try:
            L.load_session_from_file(username)
            print(f"Успешный вход в аккаунт {username} с использованием сохраненной сессии.")
        except Exception as e:
            print(f"Не удалось загрузить сессию: {e}")
            return

    # Извлекаем идентификатор поста из URL
    match = re.search(r'instagram\.com/.+?/(.+?)/', url)
    if not match:
        print("Не удалось извлечь идентификатор поста из URL.")
        return

    shortcode = match.group(1)

    # Загрузить пост
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=download_folder)
        print(f"Видео успешно скачано в папку {download_folder}.")
    except Exception as e:
        print(f"Произошла ошибка при загрузке видео: {e}")

# Пример использования
sources = "https://www.instagram.com/p/C3aL53qtdfj/?igsh=MzRlODBiNWFlZA=="
username = "your inst username" 
download_instagram_video(sources, username=username)
