from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # HTML Parser - Part 2 in Python - Hacker Rank Solution START
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
    # HTML Parser - Part 2 in Python - Hacker Rank Solution END
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()