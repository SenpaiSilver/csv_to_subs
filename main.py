#!/usr/bin/env python3

import requests
import csv
import io
import re
import argparse

def get_subtitles(c):
    pattern = re.compile(r"(\d{2}:){1,2}\d{2}(:?[,\.]\d+)?")
    lines = []
    print("Parsing translation")
    for reader in csv.reader(io.StringIO(c), delimiter=','):
        if len(reader) > 4 and pattern.search(reader[0]) and pattern.search(reader[1]) and reader[4]!="":
            lines.append([
                reader[0],
                reader[1],
                reader[4]
            ])
    print("Got %d lines" % (len(lines)))
    return lines

def main(args=None):
    if (args.input.startswith("http")):
        print("Getting translation")
        r = requests.get(args.input)
        if r.status_code != 200:
            print("Seems it failed (%d)" % (r.status_code))
            return
        sheet = r.content.decode('utf-8')
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            sheet = "\r\n".join(f.readlines())
    print("Got translation")

    if (not args.output.endswith(".srt")):
        args.output += ".srt"
    with open(args.output, "w+", encoding="utf-8") as f:
        i = 1
        for line in get_subtitles(sheet):
            f.write("\n")
            f.write("%d\n" % (i))
            f.write("00:%s --> 00:%s\n" % (line[0], line[1]))
            f.write(line[2])
            f.write("\n")
            i += 1
    print("Subtitles written to %s" % (args.output))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a Google Sheet to an SRT file')
    parser.add_argument('input', action="store", help='Input Google Sheet CSV link or local file')
    parser.add_argument('output', action='store', help='Output SRT file')
    main(parser.parse_args())
