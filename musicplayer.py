from playsound import playsound
import random
from multiprocessing import Process
import thread

#list of music available:
music_library = {
    'Life is a Highway': 'cars.mp3',
    'Down to Earth': 'downtoearth.mp3',
    'Infinity and Beyond': 'infinityandbeyond.mp3',
    'Le Festin': 'lefestin.mp3',
    'McQueen and Sally': 'mcqueenandsally.mp3',
    "If I didn't have you": 'monsters.mp3',
    'Nemo Egg': 'nemoegg.mp3',
    'Our Town': 'ourtown.mp3',
    'Real Gone': 'realgone.mp3',
    'Suite': 'suite.mp3',
    'I see the light': 'tangled.mp3',
    'The Cleaner': 'thecleaner.mp3',
    'The Filk Machine': 'thefilkmachine.mp3',
    'The time of your life': 'thetimeofyourlife.mp3',
    'Up': 'up.mp3',
    'Wall Rat': 'wallrat.mp3',
    'When she loved me': 'whenshelovedme.mp3',
}

music_list = list(music_library)

def handle_selection(selection):
    if selection == 0:
        for music in music_list:
            print("Now playing: " + music)
            playsound("music/" + music_library[music])

    elif selection == 1:
        while True:
            music_random = random.choice(music_list)
            print("Now playing: " + music_random)
            playsound("music/" + music_library[music_random])

    elif selection == 2:
        for music in music_list:
            print(music)

    else:
        print("Now playing: " + selection)
        playsound("music/" + music_library[selection])

def wait_for_input():
    back_to_menu = raw_input(": ")
    while back_to_menu != 'p':
        back_to_menu = raw_input(": ")
    thread.interrupt_main()

print("""Hello and welcome to my music player.
Please select an option or type a title:
""")
menu_options = ['0. Play All', '1. Shuffle', '2. Choose music from Library']

while True:
    print(menu_options)
    menu_selection = raw_input(": ")
    while menu_selection not in music_list:
        menu_selection = int(menu_selection)
        if menu_selection < 0 or menu_selection >= len(menu_options):
            print("Please select a valid option, and enter the number.")
            menu_selection = raw_input(": ")
        else:
            break
    print("""To go back to main menu, hit 'return' and enter 'p' and hit 'return' again.
""")

    music_process = Process(target=handle_selection, args=(menu_selection,))
    music_process.start()

    thread.start_new_thread(wait_for_input, ())

    try:
        while music_process.is_alive():
            pass
    except KeyboardInterrupt:
        pass
    music_process.terminate()
