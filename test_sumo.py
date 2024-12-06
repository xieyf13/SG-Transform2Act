import os
import subprocess


for ckpt in range(1, 130):
    command = f"python display.py --cfg config/SG/test-robo-sumo-sgdevant-ant-v0.yaml --num_episode 50 --ckpt {ckpt} --ckpt_dir tmp/models_sgdevant_ant"
    os.system(command)
