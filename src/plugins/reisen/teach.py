import os,json
import re
from nonebot import on_command,on_message
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import MessageEvent,MessageSegment
from . import utils

teach=on_command("teach", rule=to_me(), aliases={"教","添加关键词"}, priority=5)

@teach.handle()
async def handle(matcher: Matcher,event:MessageEvent,args: Message = CommandArg()):
    teachword=args.extract_plain_text()
    if teachword != "":
        matcher.set_arg("teachword",teachword)
        matcher.set_arg("session",event.get_session_id())
    else:
        await teach.finish("正确用法: 教 '你需要铃仙回复的词'")

@teach.got("reply","您想要铃仙回复什么呢?")
async def getreply(matcher:Matcher,reply = Arg("reply")):
    await addword(matcher.get_arg("session"),matcher.get_arg("teachword"),reply)
    await teach.finish("添加成功")
    

async def addword(sessionid,teachword,teachcontain):
    if not os.path.exists("data/reisen/teach/%s.json"%sessionid):
        with open("data/reisen/teach/%s.json"%sessionid,"w") as f:
            f.write(r"{}")
    with open("data/reisen/teach/%s.json"%sessionid,"r") as f:
        findict=json.loads(f.read())
        findict.update({teachword:str(teachcontain)})
    with open("data/reisen/teach/%s.json"%sessionid,"w") as f:
        f.write(json.dumps(findict,indent=4))

replyteach=on_message(priority=6)
@replyteach.handle()
async def msghandle(event:MessageEvent):
    sessionid=event.get_session_id()
    try:
        with open("data/reisen/teach/%s.json"%sessionid,"r") as f:
            findict=json.loads(f.read())
        if event.get_message().extract_plain_text() in findict.keys():
            fin=findict[event.get_message().extract_plain_text()]
            fin=utils.convImg(fin)
            await replyteach.finish(fin)
    except:
        pass

showword=on_command("showword", rule=to_me(), aliases={"查询关键词"}, priority=5)
@showword.handle()
async def swhandle(event:MessageEvent):
    sessionid=event.get_session_id()
    try:
        if not os.path.exists("data/reisen/teach/%s.json"%sessionid):
            await showword.finish("本会话暂无关键词")
        else:
            with open("data/reisen/teach/%s.json"%sessionid,"r") as f:
                findict=json.loads(f.read())
            if findict == {}:
                await showword.finish("本会话暂无关键词")
            else:
                await showword.finish("\n".join(findict.keys()))
    except:
        pass

delword=on_command("delword", rule=to_me(), aliases={"删除关键词"}, priority=5)
@delword.handle()
async def swhandle(event:MessageEvent,args: Message = CommandArg()):
    sessionid=event.get_session_id()
    args=args.extract_plain_text()
    try:
        if not os.path.exists("data/reisen/teach/%s.json"%sessionid):
            await delword.finish("本会话暂无关键词")
        else:
            with open("data/reisen/teach/%s.json"%sessionid,"r") as f:
                findict:dict=json.loads(f.read())
            if args in findict:
                findict.pop(args)
                with open("data/reisen/teach/%s.json"%sessionid,"w") as f:
                    f.write(json.dumps(findict,indent=4))
                await delword.finish("删除成功")
            else:
                await delword.finish("暂无此关键词")
    except:
        pass

delallword=on_command("delallword", rule=to_me(), aliases={"删除所有关键词"}, priority=5,permission=SUPERUSER)
@delallword.handle()
async def swhandle(event:MessageEvent,args: Message = CommandArg()):
    sessionid=event.get_session_id()
    args=args.extract_plain_text()
    try:
        if not os.path.exists("data/reisen/teach/%s.json"%sessionid):
            await delallword.finish("本会话暂无关键词")
        else:
            os.unlink("data/reisen/teach/%s.json"%sessionid)
            await delallword.finish("删除成功")
    except:
        pass