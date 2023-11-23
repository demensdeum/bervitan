from os import system, chdir, path, getcwd
from re import sub
from pydub import AudioSegment

class Engine:    
    def tts2wav(
            self, 
            text: str, 
            output_filepath: str, 
            is_russian: bool, 
            emotion: str = "Neutral", 
            speed: float = 2,
            pitch: int = 0,
            need_to_apply_coqui: bool = False,
            coqui_path: str = r"C:\Users\Demensdeum\Documents\Sources\3rdParty\RVC1006Nvidia",
            coqui_model_name: str = "goblin.pth",
            coqui_index_path: str = r"C:\Users\Demensdeum\Documents\Sources\3rdParty\RVC1006Nvidia\logs\goblin\added_IVF2148_Flat_nprobe_1_goblin_v2.index",
            coqui_is_half: bool = False,
            coqui_run_debug: bool = False,
            convert_to_mp3 = False
            ):
        if is_russian:
            import pyttsx3
            engine = pyttsx3.init()
            rate = speed * 80
            engine.setProperty('rate', rate)
            engine.setProperty('voice', "Microsoft Irina Desktop")    
            engine.save_to_file(text, output_filepath)
            engine.runAndWait()
        else:
            import torch
            from TTS.api import TTS            
            model_name = "tts_models/en/ljspeech/vits"
            tts = TTS(model_name=model_name, progress_bar=True, gpu=True)
            tts.tts_to_file(text=text, file_path=output_filepath, emotion=emotion, speed=speed)

        if need_to_apply_coqui:
            input_filepath = output_filepath
            absolute_input_filepath = path.abspath(input_filepath)
            absolutile_output_filepath = f"{absolute_input_filepath}.coqui.wav"            
            f0method = "pm"
            output_filepath = f"{input_filepath}.coqui.wav"
            model_name = coqui_model_name
            index_path = coqui_index_path
            f0up_key = pitch

            command = f"python bervitan\\apply_coqui.py \
                {coqui_path} \
                {absolute_input_filepath} \
                {index_path} \
                {f0method} \
                {absolutile_output_filepath} \
                {model_name} \
                {coqui_is_half} \
                {f0up_key} \
                "
            command = sub(' +', ' ', command)
            if coqui_run_debug:
                print(command)
            exit_code = system(command)

            if exit_code == 0 and convert_to_mp3:
                audio = AudioSegment.from_wav(output_filepath)
                mp3_path = output_filepath + ".mp3"
                audio.export(mp3_path, format="mp3")                

            return exit_code == 0
        else:
            return True