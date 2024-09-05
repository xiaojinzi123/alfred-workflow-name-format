import sys
import json


def format(
    name: str | None = None,
):
    
    if name is None:
        return

    
    singleWordList: list[str] = []
    tempSingleWord = ""
    for char in name:
        if char.isupper():
            if tempSingleWord != "":
                singleWordList.append(tempSingleWord)
                tempSingleWord = ""
            tempSingleWord += char.lower()
        elif char == "-" or char == "_" or char == " ":
            singleWordList.append(tempSingleWord)
            tempSingleWord = ""
        else:
            tempSingleWord += char.lower()

    if tempSingleWord != "":
        singleWordList.append(tempSingleWord)

    if len(singleWordList) == 0:
        return

    resultDict = {
        "items": [],
    }

    # 驼峰的, 第一个单词首字母小写
    itemName = ""
    itemName = singleWordList[0]
    itemName += "".join([word.capitalize() for word in singleWordList[1:]])
    resultDict["items"].append(
        {
            "title": f"驼峰：{itemName}",
            "arg": itemName,
        },
    )
    itemName = "".join([word.capitalize() for word in singleWordList])
    resultDict["items"].append(
        {
            "title": f"驼峰：{itemName}",
            "arg": itemName,
        },
    )
    # _ 连接的, 全部小写
    itemName = "_".join(singleWordList)
    resultDict["items"].append(
        {
            "title": f"下划线：{itemName}",
            "arg": itemName,
        },
    )
    # _ 连接的, 首字母大写
    itemName = "_".join([word.title() for word in singleWordList])
    resultDict["items"].append(
        {
            "title": f"下划线：{itemName}",
            "arg": itemName,
        },
    )
    # _ 连接的, 全部大写
    itemName = "_".join([word.upper() for word in singleWordList])
    resultDict["items"].append(
        {
            "title": f"下划线：{itemName}",
            "arg": itemName,
        },
    )
    # - 连接的, 全部小写
    itemName = "-".join(singleWordList)
    resultDict["items"].append(
        {
            "title": f"中划线：{itemName}",
            "arg": itemName,
        },
    )
    # - 连接的, 首字母大写
    itemName = "-".join([word.title() for word in singleWordList])
    resultDict["items"].append(
        {
            "title": f"中划线：{itemName}",
            "arg": itemName,
        },
    )
    # - 连接的, 全部大写
    itemName = "-".join([word.upper() for word in singleWordList])
    resultDict["items"].append(
        {
            "title": f"中划线：{itemName}",
            "arg": itemName,
        },
    )

    resultJson = json.dumps(resultDict)
    print(resultJson)


if __name__ == "__main__":
    argList = sys.argv[1:]
    # 连接参数, 空格分隔
    name = " ".join(argList)
    format(
        name=name,
    )
