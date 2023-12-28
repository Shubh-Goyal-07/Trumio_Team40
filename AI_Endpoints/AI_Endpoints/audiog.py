# Imports used through the rest of the notebook.
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F


import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

def tts_aud(text, output_file_name, voice="daniel"):
    voice = voice
    voice_samples, conditioning_latents = load_voice(voice)
    print('Converting.....')
    tts = TextToSpeech().cuda()
    gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset='fast')
    torchaudio.save('generated.wav', gen.squeeze(0).cpu(), 24000)
    IPython.display.Audio(f'{output_file_name}.wav')