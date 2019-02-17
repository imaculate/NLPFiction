import lxml.etree
import urllib
import urllib.request
import re
import os
import argparse

anchor_pattern = "(\[\[){1}[a-zA-Z0-9_ ]*(\]\]){1}"

def scrape_wiki(title):
    params = {"format": "xml", "action": "query", "prop": "revisions", "rvprop": "timestamp|user|comment|content"}
    params["titles"] = "API|%s" % urllib.parse.quote(title.encode("utf8"))
    qs = "&".join("%s=%s" % (k, v) for k, v in params.items())
    url = "http://en.wikipedia.org/w/api.php?%s" % qs
    tree = lxml.etree.parse(urllib.request.urlopen(url))
    revs = tree.xpath('//rev')
    return revs[-1].text

def scrape_wiki_and_save(title, save_dir):
    wiki_text = scrape_wiki(title)
    if "#REDIRECT" in wiki_text:
        print(wiki_text)
        title = re.search("(\[\[){1}.*(\]\]){1}", wiki_text).group().strip('[').strip(']')
        wiki_text = scrape_wiki(title)

    filename =  "wiki_" + title + ".txt"
    with open(os.path.join(save_dir, filename), "w+", encoding="utf-8") as f:
        f.write(wiki_text)
    return wiki_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='data\\benfranklin',
                       help='directory to store scraped articles')
    parser.add_argument('--title', type=str, default='Benjamin Franklin',
                help='topic to begin scraping on')
    parser.add_argument('--combine_file', type=str, default='input.txt',
                        help='filename where articles will be written to after cleaning up')
    args = parser.parse_args()
    scrape_wikis(args)
    clean_data(args)

def scrape_wikis(args):
    wiki_text = scrape_wiki_and_save(args.title, args.save_dir)
    anchors = []
    [anchors.append(m.group().strip('[').strip(']')) for m in re.finditer(anchor_pattern, wiki_text)]

    for anchor in anchors:
        print("Scraping "+ anchor)
        scrape_wiki_and_save(anchor, args.save_dir)


def clean_data(args):
    fw = open(os.path.join(args.save_dir, args.combine_file), "w+", encoding="utf-8")
    for root, dirs, files in os.walk(args.save_dir):
        for filename in files:
            if filename.startswith("wiki_"):
                with open(os.path.join(args.save_dir, filename), "r", encoding="utf-8") as f:
                    input_text = f.read()

                # remove everything enclosed by {{ }}, links and beginning text that is not really needed
                input_text = re.sub("(\{\{){1}.*(\}\}){1}", "", input_text)
                # remove the stuff in between, get all the way to references
                try:
                    input_text = input_text[:input_text.index("==References==")]
                    print("References section found!")
                except ValueError:
                    print("Substring ==References== not found")

                # remove [[]] for texts with just letters and numbers
                input_text = re.sub(r"[^a-z0-9\.,]+", " ", input_text.lower())

                fw.write(input_text)


    fw.close()
