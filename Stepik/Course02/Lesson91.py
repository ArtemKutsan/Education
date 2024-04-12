# Импорт библиотек
import streamlit as st  # библиотека streamlit


# Создаем меню в боковой панели
menu_choice = st.sidebar.radio("Меню", ("Главная", "Настройки", "Помощь"))

# Обработка выбора из меню
if menu_choice == "Главная":
    st.title("Добро пожаловать на главную страницу!")
    # Здесь можно добавить контент для главной страницы
elif menu_choice == "Настройки":
    st.title("Страница настроек")
    # Здесь можно добавить контент для страницы настроек
elif menu_choice == "Помощь":
    st.title("Страница помощи")
    # Здесь можно добавить контент для страницы помощи


# Show celebratory balloons
st.balloons()

# Show an error message
st.error("An Error was encountered")

# Display a warning message
st.warning("Incompatible data point!")

# Display informational messages
st.info("Page is refreshed every 2 hours")

# Display success messages
st.success("Record found!")

# Display an exception in your application
exp = ValueError('This is an exception of type ValueError')