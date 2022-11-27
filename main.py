import os,json

def read(wenjian):
    if not os.path.exists(wenjian):
        os.mkdir(wenjian)
    return(os.listdir(wenjian))


def main():
    print("小组列表：")
    groups = read("groups")
    for name in groups[:]:
        print(name[:-5],end="  ")
    config = input("\n小组：（若不存在则自动创建）")
    name = config+".json"
    os.chdir("groups")
    if not os.path.exists(name):
        basic = {"a":"0","b":"0","c":"0","d":"0"}
        json.dump(basic,open(name,'w',encoding="utf-8"),indent=4)
        print("小组文件生成完毕，请前往'groups文件夹'完成设置~")
        os.system("pause")
    data_groups = json.load(open(name,'r',encoding="utf-8"))
    os.chdir("..")

    print("任务列表：")
    groups = read("tasks")
    for name in groups[:]:
        print(name[:-5],end="  ")
    tasks = input("\n任务：（若不存在则自动创建）")
    name2 = tasks+".txt"
    os.chdir("tasks")
    if not os.path.exists(name2):
        open(name2,'w',encoding="utf-8").write("a\nb\nc\nd")
        print("任务文件生成完毕，请前往'tasks文件夹'完成设置~")
        os.system("pause")
    data_tasks = open(name2,'r',encoding="utf-8")
    data_tasks = data_tasks.read().split("\n")
    os.chdir("..")


if __name__ == "__main__":
    main()
