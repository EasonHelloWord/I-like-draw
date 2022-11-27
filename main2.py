import os,json,time,random
def start():
    if not os.path.exists('player.json'):
        basic = {"players":["a","b","c","d"],
        "tasks":["a","b","c","d"]}
        json.dump(basic,open('player.json','w'),indent=4)
        time.sleep(0.3)
        print("配置文件生成完毕，请前往'player.json'完成设置~")

def read():
    data = json.load(open('player.json', 'r',encoding="utf-8"))
    return(data)

if __name__ == "__main__":
    start()
    data = read()
    tasks = data['tasks'][:]
    random.shuffle(tasks)
    for player in data["players"][:]:
        task = tasks.pop()
        print(f"小组成员：{player}的任务为：{task}")
    os.system("pause")

