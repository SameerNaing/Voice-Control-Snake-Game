from game import Game
from voice import VoiceControl


def main():
    game = Game()
    voice_control = VoiceControl()

    game.start()
    voice_control.stop_listening()


if __name__ == "__main__":
    main()
