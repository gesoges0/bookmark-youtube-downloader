from pathlib import Path
import os
import subprocess
import json
import subprocess
import sys

if __name__ == '__main__':

	args = sys.argv
	try:
		folder_title = args[1]
	except:
		print('フォルダ名が指定されていません')

	print(folder_title)

	output_dir = '/mnt/da1fb3ab-8bd1-4b98-983e-b45899e50c48/youtube'

	# file path
	file_path = '../../.config/google-chrome/Default/Bookmarks'
	if not os.path.exists(f'{output_dir}/{folder_title}'):
		os.mkdir(f'{output_dir}/{folder_title}')

	# chrome-bookmark-path
	with open(file_path, 'r') as f:
		bookmark_dict = json.load(f)

		# ブックマックバーの第一階層
		for bookmark in bookmark_dict['roots']['bookmark_bar']['children']:
			

			# typeは folder or url
			# ブックマークバーの第二階層
			if bookmark['type'] == 'folder' and bookmark['name'] == 'NBA':
				for bookmark_in_folder1 in bookmark['children']:
					
					# ブックマークバーの第三階層
					if bookmark_in_folder1['type'] == 'folder' and bookmark_in_folder1['name'] == folder_title:
						all_num = len(bookmark_in_folder1['children'])
						for i, bookmark_in_folder2 in enumerate(bookmark_in_folder1['children']):
							print('--'*20)
							print(f'{i+1} / {all_num}')
							movie_url = f"{bookmark_in_folder2['url']}"
							movie_title = f"{bookmark_in_folder2['name']}"
							print(movie_url, movie_title)
							subprocess.run(['youtube-dl', movie_url, '-o', f"{output_dir}/{folder_title}/{movie_title}"])
