import re
import sys

def main():

    html_input = input("HTML: ")

    print(parse(html_input))


def parse(s):

    pattern = r'src="(https?://(www\.)?(youtube\.com/embed/|youtu\.be/)([A-Za-z0-9_-]+))"'


    match = re.search(pattern, s)

    if match:

        video_id = match.group(4)
        return f"https://youtu.be/{video_id}"


    return None


if __name__ == "__main__":
    main()
