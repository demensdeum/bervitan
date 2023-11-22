import sys
from pathlib import Path
sys.path.append(str(Path(sys.argv[0]).resolve().parent.parent))
import bervitan

text2tts = bervitan.Engine()

for i in range(0, 2):
    apply_coqui = i == 1
    if text2tts.tts2wav(
        text="OK! THAT IS IT! THIS IS THE FINAL STRAAAAAAAW! I’VE HAD IT WITH ALL YOU FRICKIN’\
            TROLLS AND ALL YOU FRICKIN’ HATERS AND ALL YOU FRICKIN SONIC FAN FRICKS.\
                YOU GUYS ARE THE ONES THAT RUINED SONIC FOR EVERYONE! CAN'T YOU SEE THAT?\
                    WHAT THE FRICK ARE YOU GUYS DOING! ASKING FOR ALL THIS FRICKING GARBAGE- WHY DO WE NEED SONIC ADVENTURE 3?\
                        WHY DO WE NEED SONIC HEROES 2? WHY DO WE NEED ANOTHER BOOST TO WIN TITLE?\
                            WHY DO WE NEED A SONIC 2006 SEQUEL? WHY DO WE NEED ALL THAT? ",
        output_filepath="./build/output.en.wav",
        is_russian=False,
        apply_coqui=apply_coqui
    ):
        print(f"TTS Russian -> Wav success! coqui_applied: {apply_coqui}")
    else:
        print(f"Can't use tts for english, check params!  coqui_applied: {apply_coqui}")
        exit(1)

    if text2tts.tts2wav(
        text="Здраствуйте. Я, Кирилл. Хотел бы чтобы вы сделали игру, \
            3Д-экшон суть такова... Пользователь может играть лесными эльфами,\
                охраной дворца и злодеем. И если пользователь играет эльфами\
                    то эльфы в лесу, домики деревяные набигают солдаты дворца и злодеи. \
                        Можно грабить корованы...", 
        output_filepath="./build/output.ru.wav", 
        is_russian=True,
        apply_coqui=apply_coqui
    ):
        print(f"TTS Russian -> Wav success! coqui_applied: {apply_coqui}")
    else:
        print(f"Can't use tts for russian, check params! coqui_applied: {apply_coqui}")
        exit(1)        

exit(0)