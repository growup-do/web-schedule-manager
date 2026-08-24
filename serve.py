import os, sys
os.chdir("/Users/kaz_iMac_2020/Documents/claude/アプリ/スケジュール")
from http.server import HTTPServer, SimpleHTTPRequestHandler
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8081
HTTPServer(("", port), SimpleHTTPRequestHandler).serve_forever()
