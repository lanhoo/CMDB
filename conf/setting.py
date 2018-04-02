import importlib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 采集资产的方式：agent,salt,ssh
MODE = 'agent'

