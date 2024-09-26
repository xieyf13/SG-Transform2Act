import os
import subprocess


for ckpt in range(1, 130):
    command = f"python display.py --cfg config/test-robo-sumo-sgant-ant-v0.yaml --ckpt {ckpt} --ckpt_dir tmp/models_ants"
    os.system(command)
