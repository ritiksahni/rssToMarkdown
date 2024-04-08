#!/usr/bin/python3
import feedparser
import markdownify
from mdutils.mdutils import MdUtils

RSS_FEED = "https://rss.beehiiv.com/feeds/MPXDihxG36.xml" # Replace this if you want to extract posts from other Beehiiv RSS feeds.
feed = feedparser.parse(RSS_FEED)

# Top Level Array with all the children objects in it.
top_level_array = feed.entries

# For tracking post IDs and naming exported markdown files.
postId = 0
for child in top_level_array:
    post_title = child.title
    content_html = child.content[0].value

    # I am converting HTML to Markdown to preserve formatting of the posts.
    content_md = markdownify.markdownify(content_html, heading_style="ATX")
    file_name = "post_" + str(postId)
    markdown_file = MdUtils(file_name=file_name)
    markdown_file.new_header(level=1, title=post_title)
    markdown_file.write(content_md)
    markdown_file.create_md_file()
    postId = postId + 1
