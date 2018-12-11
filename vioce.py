#!/usr/bin/env python
# coding:utf-8


from pyaudio import PyAudio, paInt16
import wave
import pygame



framerate = 16000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

# 保存录音文件
def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

# 录制并保存录音文件
def my_record():
    # 开启声音输入
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1, rate=framerate, input=True, frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    # print('.')
    while count < TIME * 10:  # 控制录音时间
        # 读入NUM_SAMPLES个取样
        string_audio_data = stream.read(NUM_SAMPLES)

        my_buf.append(string_audio_data)
        count += 1

    save_wave_file('01.wav', my_buf)
    stream.close()


def say():
    pygame.mixer.init()
    track = pygame.mixer.music.load('auido.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.stop()