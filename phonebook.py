import requests
import json
import argparse
import os

def get_token(domain):
    url = "https://public.intelx.io:443/phonebook/search?k=077424c6-7a26-410e-9269-c9ac546886a4"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0",
                     "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://phonebook.cz",
                     "Dnt": "1", "Referer": "https://phonebook.cz/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors",
                     "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
    if args.email:
        json={"maxresults": 10000, "media": 0, "target": 2, "term": domain, "terminate": [None], "timeout": 20}
    if args.domain:
        json={"maxresults": 10000, "media": 0, "target": 1, "term": domain, "terminate": [None], "timeout": 20}
    if args.links:
        json={"maxresults": 10000, "media": 0, "target": 3, "term": domain, "terminate": [None], "timeout": 20}
    response = requests.post(url, headers=headers, json=json)
    key = response.text
    status = response.status_code
    if status == 402:
        exit('[-] Your IP is rate limited. Try switching your IP address then re-run.')
    else:
        return key

def make_request(key):
    key = json.loads(key)['id']
    url = f"https://public.intelx.io:443/phonebook/search/result?k=077424c6-7a26-410e-9269-c9ac546886a4&id={key}&limit=1000000"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
        "Origin": "https://phonebook.cz", "Dnt": "1", "Referer": "https://phonebook.cz/", "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
    response = requests.get(url, headers=headers)
    items = response.text
    status = response.status_code
    if status == 402:
        exit('[-] Your IP is rate limited. Try switching your IP address then re-run.')
    else:
        return items

def parse_items(items):
    file = open(args.phonebook_cz + '_cz.txt', 'a')
    items = json.loads(items)['selectors']
    for item in items:
        item = item['selectorvalue']
        print(item)
        file.write(item)
        file.write('\n')
    if args.phonebook_cz:
        print(f'\n[+] Done! Saved to to ' + args.phonebook_cz + '_cz.txt')
    else: print(f'\n[+] Done!')

def argparser():
    parser = argparse.ArgumentParser(description="Phonebook.cz scraper")
    parser.add_argument("-e", "--email", help="Search all emails for this domain.")
    parser.add_argument("-d", "--domain", help="Search all subdomains for this domain.")
    parser.add_argument("-l", "--links", help="Search all links for this domain.")
    parser.add_argument('-o', action='store', dest='phonebook_cz', nargs='?', const='phonebook', default='phonebook',
                        help='Stores all items in file *_cz.txt')
    return parser.parse_args()

if __name__ == '__main__':
    print('[+] Running phonebook.cz scraper!\n')
    args = argparser()
    if args.email:
        key = get_token(args.email)
    if args.domain:
        key = get_token(args.domain)
    if args.links:
        key = get_token(args.links)
    emails = make_request(key)
    parse_items(emails)
