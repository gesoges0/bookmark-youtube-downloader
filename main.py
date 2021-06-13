from pathlib import Path
import os
import subprocess
import json
from dataclasses import dataclass

SETTING_PATH = Path('./settings.txt')

@dataclass
class YoutubeDL:
	chrome_bookmark_path: Path = ''
	
	def __post_init__(self):
		with open(SETTING_PATH, 'r') as f:
			self.chrome_bookmark_path = f.read().replace('\n', '')




if __name__ == '__main__':
	youtube_dl = YoutubeDL('')
	print(youtube_dl.chrome_bookmark_path)
