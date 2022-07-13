import requests, os, threading, datetime
from rich import print


def exists(url, username):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(f"[+][green] {username} exists on {url.split('/')[2]}[/]")
        else:
            print(f"[-][red] {username} does not exist on {url.split('/')[2]}[/]")
    except Exception as e:
        print(e)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(F"""
███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝ - Search users over 37 popular sites
██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗ - Version 1.0
██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║ - Written by @jwestern1337
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
    username = input('Username: ')
    print(f"[+] Searching for {username} on 37 sites...")
    before = datetime.datetime.now().strftime('%H:%M:%S')
    socials = [
        f"https://www.picuki.com/profile/{username}", # instagram
        f"https://www.facebook.com/{username}",
        f"https://www.twitter.com/{username}", # twitter
        f"https://www.youtube.com/channel/{username}",
        f"https://www.t.me/{username}", # telegram
        f"https://www.linkedin.com/{username}",
        f"https://www.github.com/{username}",
        f"https://www.reddit.com/user/{username}",
        f"https://www.tinder.com/@{username}",
        f"https://www.pinterest.com/{username}",
        f"https://www.tumblr.com/{username}",
        f"https://www.flickr.com/{username}",
        f"https://www.quora.com/{username}",
        f"https://www.digg.com/{username}",
        f"https://www.stumbleupon.com/{username}",
        f"https://www.tiktok.com/@{username}",
        f"https://www.twitch.tv/{username}",
        f"https://www.vk.com/{username}",
        f"https://www.wechat.com/{username}",
        f"https://www.xing.com/{username}",
        f"https://www.yelp.com/{username}",
        f"https://www.soundcloud.com/{username}",
        f"https://www.steamcommunity.com/id/{username}",
        f"https://www.linktr.ee/{username}",
        f"https://www.pornhub.com/users/{username}",
        f"https://www.vimeo.com/{username}",
        f"https://www.imdb.com/{username}",
        f"https://www.pastebin.com/u/{username}",
        f"https://www.allmylinks.com/{username}",
        f"https://www.buzzfeed.com/{username}",
        f"https://www.sourceforge.net/u/{username}/profile",
        f"https://www.deviantart.com/{username}",
        f"https://www.behance.net/{username}",
        f"https://www.ebay.com/usr/{username}"
    ]
    for social in socials:
        threading.Thread(target=exists, args=(social,username,)).start()


main()
