import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
import bervitan
import os

text2tts = bervitan.Engine()

for i in range(0, 3):
    need_to_apply_coqui = i > 1
    convert_to_mp3 = i == 2
    if text2tts.tts2wav(
        text="OK! THAT IS IT! THIS IS THE FINAL STRAAAAAAAW! I’VE HAD IT WITH ALL YOU FRICKIN’\
            TROLLS AND ALL YOU FRICKIN’ HATERS AND ALL YOU FRICKIN SONIC FAN FRICKS.\
                YOU GUYS ARE THE ONES THAT RUINED SONIC FOR EVERYONE! CAN'T YOU SEE THAT?\
                    WHAT THE FRICK ARE YOU GUYS DOING! ASKING FOR ALL THIS FRICKING GARBAGE- WHY DO WE NEED SONIC ADVENTURE 3?\
                        WHY DO WE NEED SONIC HEROES 2? WHY DO WE NEED ANOTHER BOOST TO WIN TITLE?\
                            WHY DO WE NEED A SONIC 2006 SEQUEL? WHY DO WE NEED ALL THAT? ",
        output_filepath="./build/output.en.wav",
        is_russian=False,
        need_to_apply_coqui=need_to_apply_coqui,
        convert_to_mp3=convert_to_mp3
    ):
        print(f"TTS Russian -> Wav success! need_to_apply_coqui: {need_to_apply_coqui}, convert_to_mp3: {convert_to_mp3}")
    else:
        print(f"Can't use tts for english, check params!  coqui_applied: {need_to_apply_coqui}, convert_to_mp3: {convert_to_mp3}")
        exit(1)

    if text2tts.tts2wav(
        text="Здраствуйте. Я, Кирилл. Хотел бы чтобы вы сделали игру, \
            3Д-экшон суть такова... Пользователь может играть лесными эльфами,\
                охраной дворца и злодеем. И если пользователь играет эльфами\
                    то эльфы в лесу, домики деревяные набигают солдаты дворца и злодеи. \
                        Можно грабить корованы...", 
        output_filepath="./build/output.ru.wav", 
        is_russian=True,
        need_to_apply_coqui=need_to_apply_coqui,
        convert_to_mp3=convert_to_mp3
    ):
        print(f"TTS Russian -> Wav success! need_to_apply_coqui: {need_to_apply_coqui}, convert_to_mp3: {convert_to_mp3}")
    else:
        print(f"Can't use tts for russian, check params! need_to_apply_coqui: {need_to_apply_coqui}, convert_to_mp3: {convert_to_mp3}")
        exit(1)

exit(0)