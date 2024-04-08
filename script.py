#!/usr/bin/python3
import feedparser
import markdownify
from dateutil import parser

RSS_FEED = "https://rss.beehiiv.com/feeds/MPXDihxG36.xml" # Replace this if you want to extract posts from other Beehiiv RSS feeds.
feed = feedparser.parse(RSS_FEED)

# Top Level Array with all the children objects in it.
top_level_array = feed.entries

# For tracking post IDs and naming exported markdown files.
postId = 0

frontmatter_format = """---
title: '{0}'
publishDate: '{1}'
tags:
    - Essay
---
"""
for child in top_level_array:
    post_title = child.title
    post_published_date = child.published
    dt = parser.parse(post_published_date)
    formatted_date = dt.strftime('%B %d %Y')
    content_html = child.content[0].value

    # I am converting HTML to Markdown to preserve formatting of the posts.
    content_md = markdownify.markdownify(content_html, heading_style="ATX")
    file_name = "post-" + str(postId) + ".md"

    # Write the Markdown content to the file
    with open(file_name, 'w', encoding='utf-8') as md_file:
        # Write the frontmatter
        md_file.write(frontmatter_format.format(post_title, formatted_date))
        
        # Write the post content
        md_file.write(content_md) 

    postId += 1

