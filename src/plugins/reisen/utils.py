import re

def convImg(raw:str):
    from nonebot.adapters.onebot.v11 import MessageSegment,Message
    if re.search(r"\[CQ:image,file.*]",raw):
        rep=re.split(rf"\[CQ:image,file=.*?url=(.*?)]",raw)
        for reprep,index in zip(rep,range(len(rep))):
            if "https://c2cpicdw.qpic.cn/offpic_new/" in reprep:
                rep[index]=MessageSegment.image(file=reprep)
    else:
        rep=raw
    return Message(rep)