from colorama import Fore, init
import emoji

init(autoreset=True)

def show_message(mood):
    if mood == "happy":
        print(Fore.GREEN, "Привет! Надеюсь, у тебя отличный день!", emoji.emojize(":grinning_face_with_big_eyes:"))
    elif mood == "sad":
        print(Fore.RED, "Извини, что ты чувствуешь себя плохо. Не переживай, всё наладится.", emoji.emojize(":disappointed_face:"))
    elif mood == "tired":
        print(Fore.YELLOW, "Привет! Отдыхай, если можешь. Усталость сегодня вполне оправдана.", emoji.emojize(":sleeping_face:"))
    elif mood == "excited":
        print(Fore.CYAN, "Вау, у тебя отличное настроение! Держи так дальше!", emoji.emojize(":star_struck:"))
    else:
        print(Fore.WHITE, "К сожалению, я не понимаю это настроение...", emoji.emojize(":man_shrugging:"))

user_mood = input("Как ты себя сегодня чувствуешь? (happy, sad, tired, excited): ").lower()

show_message(user_mood)
