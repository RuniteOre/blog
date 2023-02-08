import os

# posts is a variable containing a list of all the files in posts
posts = os.listdir('posts')

# filters down posts to files which contain two entries one that ends in ".md" and one in ".meta"
post_names = [post[:-3] for post in posts if post.endswith('.md') and post[:-3] + '.meta' in posts]

# create a directory at tags if it does not already exist
if not os.path.exists('tags'):
	os.makedirs('tags')

# key is post name, value is a list [post title, post tags, date]
tagged_posts = {}
tag_dict = {}
for post in post_names:
	# opens the file in ./posts
	with open('posts/' + post + '.meta') as f:
		# reads the first line of the file
		title = f.readline().strip()
		# reads the second line of the file
		tags = f.readline().strip().lower()
		if len(tags) > 0:
			tags = tags.split(',')
		else:
			tags = []
		for tag in tags:
			if tag in tag_dict:
				tag_dict[tag].append(post)
			else:
				tag_dict[tag] = [post]
		# reads the third line of the file, the date, as a number
		try:
			date = int(f.readline().strip())
		except ValueError:
			date = 0
		# adds the post name as a key and the tuple (post title, post tags) as the value
		tagged_posts[post] = [title, tags, date]

for tag in tag_dict:
	# sort the posts by date in descending order
	tag_dict[tag].sort(key=lambda x: tagged_posts[x][2], reverse=True)
	tag_list = open('tags/' + tag + '.tag', 'w')
	tag_list.write('\n'.join(tag_dict[tag]))

# write the values of tag_dict to tags/index.tags, sorted descending by post count, format is "tag count"
with open('tags/index.tags', 'w') as f:
	for tag in sorted(tag_dict, key=lambda x: (len(tag_dict[x]), x), reverse=True):
		f.write(tag + ' ' + str(len(tag_dict[tag])) + '\n')

