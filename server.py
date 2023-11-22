from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os
import bervitan

app = Flask(__name__)

@app.route('/generateTTS', methods=['POST'])
def generate_tts():
    try:
        data = request.get_json()

        message = data.get('message', '')
        message.replace("\n", "")
        is_russian = data.get('is_russian', False)
        pitch = data.get('pitch', 0.0)

        language = 'ru' if is_russian else 'en'

        if not message:
            return jsonify({'error': 'Missing message parameter'}), 400

        text2tts = bervitan.Engine()

        server_audio_output = "./build/server.output.wav"
        server_audio_output_mp3 = "./build/server.output.wav.coqui.wav.mp3"

        text2tts.tts2wav(
                text=message, 
                output_filepath=server_audio_output, 
                is_russian=is_russian,
                apply_coqui=True,
                convert_to_mp3=True,
                pitch=pitch
            )            

        return send_file(server_audio_output_mp3, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)