import random
from bs4 import BeautifulSoup

all_posts = []

def draw_base_list_1():
    lilist=soup.find('div',{'class':'pb_content clearfix'});
    for x in lilist:
        postlist=x.find('div',{'class':'p_postlist'});
        if not postlist:
            break
        # print(len(postlist))
        for post in postlist:
            try:
                auth = post.find('div',{'class':'d_author'});
                if auth: 
                    authinfo = auth.find('ul',{'class':'p_author'}).find('a',{'class':'p_author_face'})
                    url = authinfo.get('href')
                    # print(url)
                    if url not in all_posts: all_posts.append(url)
            except:
                continue

def draw_base_list():
    lilist=soup.find('div',{'class':'pb_content clearfix'});
    for x in lilist:
        postlist=x.find('div',{'class':'p_postlist'});
        if not postlist:
            break
        # print(len(postlist.find('div',{'class':'p_postlist'})))
        for post in postlist.find('div',{'class':'p_postlist'}):
            try:
                auth = post.find('div',{'class':'d_author'});
                if auth: 
                    authinfo = auth.find('ul',{'class':'p_author'}).find('a',{'class':'p_author_face'})
                    url = authinfo.get('href')
                    # print(url)
                    all_posts.append(url)
            except:
                continue

soup=BeautifulSoup(open('pn{}.html'.format(1),encoding='utf-8'),features='html.parser')
draw_base_list_1()

for i in range(2, 14):
    soup=BeautifulSoup(open('pn{}.html'.format(i),encoding='utf-8'),features='html.parser')
    draw_base_list()

print("总楼层数：",len(all_posts))

all_users = list(set(all_posts[1:]))

print("有效用户数量：",len(all_users))
print("有效用户主页url：")
for url in all_users: print(" -", url)

print("中奖用户：")
index = random.randint(1, len(all_users))
print(all_users[index])