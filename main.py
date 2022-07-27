import requests, os, threading
from time import sleep
from rich import print


def exists(url, username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print(f"[+][green] {url}[/]")
        with open(f'{username}.txt', 'a') as f:
            f.write(f"{url}\n")
        f.close()
    else:
        #print(f"[-][red] {username} does not exist on {url.split('/')[2]}[/]")
        pass

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(F"""
███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝ - Search users over 92 popular sites
██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗ - Version 1.0
██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║ - Written by @jwestern1337
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
    username = input('Username: ')
    print(f"[+] Searching for {username} on 92 sites...")
    socials = [
        f"https://www.picuki.com/profile/{username}", # instagram
        f"https://www.facebook.com/{username}",
        f"https://www.twitter.com/{username}",
        f"https://www.youtube.com/channel/{username}",
        f"https://www.t.me/{username}", # telegram
        f"https://www.linkedin.com/{username}",
        f"https://www.github.com/{username}",
        f"https://www.reddit.com/user/{username}",
        f"https://www.gotinder.com/@{username}",
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
        f"https://www.ebay.com/usr/{username}",
        f"https://www.weebly.com/{username}",
        f"https://2Dimensions.com/a/{username}",
        f"http://forum.3dnews.ru/member.php?username={username}",
        f"https://www.7cups.com/@{username}",
        f"https://www.9gag.com/u/{username}",
        f"https://about.me/{username}",
        f"https://independent.academia.edu/{username}",
        f"https://airbit.com/{username}",
        f"https://allmylinks.com/{username}",
        f"https://developer.apple.com/forums/profile/{username}",
        f"https://discussions.apple.com/profile/{username}",
        f"https://archive.org/details/@{username}",
        f"https://create.arduino.cc/projecthub/{username}",
        f"https://www.behance.net/{username}",
        f"https://bitcoinforum.com/profile/{username}",
        f"https://buymeacoff.ee/{username}",
        f"https://www.cnet.com/profiles/{username}/",
        f"https://community.cloudflare.com/u/{username}",
        f"https://www.codecademy.com/profiles/{username}",
        f"https://codepen.io/{username}",
        f"https://dev.to/{username}",
        f"https://hub.docker.com/u/{username}/",
        f"https://www.duolingo.com/profile/{username}",
        f"https://www.etsy.com/shop/{username}",
        f"https://www.fiverr.com/{username}",
        f"https://giphy.com/{username}",
        f"https://gitlab.com/{username}",
        f"https://forum.hackthebox.eu/profile/{username}",
        f"https://hackaday.io/{username}",
        f"https://hackerearth.com/@{username}",
        f"https://hackerone.com/{username}",
        f"https://hackerrank.com/{username}",
        f"https://icq.im/{username}/en",
        f"https://imgur.com/user/{username}",
        f"https://keybase.io/{username}",
        f"https://leetcode.com/{username}",
        f"https://api.mojang.com/users/profiles/minecraft/{username}",
        f"https://nightbot.tv/t/{username}/commands",
        f"https://ok.ru/{username}",
        f"https://onlyfans.com/{username}",
        f"https://opensource.com/users/{username}",
        f"https://forums.pcgamer.com/members/?username={username}",
        f"https://www.patreon.com/{username}",
        f"https://play.google.com/store/apps/developer?id={username}",
        f"https://pypi.org/user/{username}",
        f"https://quizlet.com/{username}",
        f"https://www.redbubble.com/people/{username}",
        f"https://replit.com/@{username}",
        f"https://www.roblox.com/user.aspx?username={username}",
        f"https://apps.runescape.com/runemetrics/app/overview/player/{username}",
        f"https://community.signalusers.org/u/{username}",
        f"https://tellonym.me/{username}",
        f"https://trello.com/{username}",
        f"https://tryhackme.com/p/{username}",
        f"https://data.typeracer.com/pit/profile?user={username}",
        f"https://www.virustotal.com/ui/users/{username}/trusted_users",
        f"https://www.wattpad.com/user/{username}",
        f"https://xboxgamertag.com/search/{username}"
        ]
    for social in socials:
        threading.Thread(target=exists, args=(social,username,)).start()

main()
