import urllib, re 

def main():

	start_title = raw_input('Title of Wikipedia Article (start): ')
	target_title = raw_input('Title of Wikipedia Article (target): ')

	print clickfinder(start_title, target_title)

def linkify(title):
	return 'https://en.wikipedia.org/wiki/{}'.format(title.replace(' ','_'))

def clickfinder(start_title, target_title):
	''' returns the minimum number of clicks needed to get from one wikipedia
	article to another. '''

	new_title_list = [start_title]

	clicks = 1
	while True:
		temp_list = []

		for base_title in new_title_list:
	
			titles = title_list(base_title)

			for title in titles:
				
				if title.lower().replace(' ','_') == target_title.lower().replace(' ','_'): # ww have found the title
					print base_title
					return clicks

				temp_list.append(title)

		new_title_list = temp_list

		clicks += 1



		

	return -1

def title_list(title):
	''' returns a list of titles that can be accessed using the title passed.
	Ex. if title was A and there were Wiki links to B and C, title_list(A) = [B,C].

	Since many Wikipedia articles are technical and do not link to other Wikipedia articles
	(i.e. Wikipedia:User_agreement), articles with ":" are omitted.
	'''
	start_text = title_text(title)

	regex = '<a href="/wiki/(.+?)"' # regex patterns. Matches wikipedia titles in underscore form.

	pattern = re.compile(regex)

	titles = re.findall(pattern, start_text) # finds all titles.

	
	titles = filter(lambda x: (':' in x) == False, titles) # filters out all of the bad links (:)
	return titles
	

def title_text(title):
	''' returns the HTML text of a Wikipedia URL. "title" can be any Wikipedia page title.'''

	title = title.replace(' ','_')
	url = linkify(title)

	f = urllib.urlopen(url)

	text = f.read()
	f.close() # close the file before return.

	return text



if __name__ == '__main__':
	main()
