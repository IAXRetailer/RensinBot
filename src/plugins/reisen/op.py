from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import CommandArg,ArgPlainText,Arg
from nonebot.permission import SUPERUSER
from nonebot.log import logger
from nonebot.exception import FinishedException
import traceback
op=on_command("op",rule=to_me(),aliases={"管理员"},priority=5,permission=SUPERUSER)

@op.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    if len(args) == 0:
        await op.finish("正确用法 'op 命令'")
    else:
        keyname=args.extract_plain_text()
        if keyname == "exec":
            pass
        else:
            await op.finish("未知命令")


@op.got("text",prompt="输入执行文本")
async def texthandle(text:str=ArgPlainText("text")):
    if text != None:
        try:
            try:
                exec(text)
                await op.finish("执行成功")
            except Exception as e:
                if not isinstance(e,FinishedException):
                    await op.send("执行失败")
                    await op.finish(traceback.format_exc())
        except:
            pass
