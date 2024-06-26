#! /usr/bin/python3
# Thanks to pshanmu3 user on github
import requests
import os
import sys

proxies = {}
if len(sys.argv) == 3:
    proxies = {
                'http' : sys.argv[2],
                'https' : sys.argv[2]
              }

na = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
def grab(id):
    headers={
        "User-Agent": "Equidia/6036 CFNetwork/1220.1 Darwin/20.3.0",
        "Referer": "https://fr.equidia.app/"
    }
    try:
        m3u = s.get('https://api.equidia.fr/api/public/racing/equidia-mobileapp-ios-1/equidia-'+id, headers=headers, proxies=proxies).json()['primary']
    except Exception as e:
        m3u = na
    finally:
        # print(m3u)
        print('#EXT-X-STREAM-INF:BANDWIDTH=2820400,RESOLUTION=1920x1080')
        print(m3u.replace("playlist.m3u8", "eqd" + id + "_fre_0.m3u8"))
        print('#EXT-X-STREAM-INF:BANDWIDTH=2270400,RESOLUTION=1280x720')
        print(m3u.replace("playlist.m3u8", "eqd" + id + "_fre_1.m3u8"))
        print('#EXT-X-STREAM-INF:BANDWIDTH=1390400,RESOLUTION=1024x576')
        print(m3u.replace("playlist.m3u8", "eqd" + id + "_fre_2.m3u8"))
        print('#EXT-X-STREAM-INF:BANDWIDTH=730400,RESOLUTION=640x360')
        print(m3u.replace("playlist.m3u8", "eqd" + id + "_fre_3.m3u8"))
        print('#EXT-X-STREAM-INF:BANDWIDTH=400400,RESOLUTION=256x144')
        print(m3u.replace("playlist.m3u8", "eqd" + id + "_fre_4.m3u8"))
 


print('#EXTM3U')
print('#EXT-X-VERSION:3')
s = requests.Session()

if (sys.argv[1] == 'equidia'):
    id = 'live2'
elif (sys.argv[1] == 'trot'):
    id = 'racingtrot'
elif (sys.argv[1] == 'galop'):
    id = 'racinggalop'
elif (sys.argv[1] == 'mag'):
    id = 'racingmag'
elif (sys.argv[1] == 'racing1'):
    id = 'racing1'
elif (sys.argv[1] == 'racing2'):
    id = 'racing2'
elif (sys.argv[1] == 'racing3'):
    id = 'racing3'
elif (sys.argv[1] == 'racing4'):
    id = 'racing4'
elif (sys.argv[1] == 'racing5'):
    id = 'racing5'
else:
    sys.exit(1)

grab(id)
