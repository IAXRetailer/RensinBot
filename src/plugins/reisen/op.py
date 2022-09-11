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
        if keyname != "exec":
            op.set_arg(matcher,"exec",None)
        if keyname != "eval":
            op.set_arg(matcher,"eval",None)
        if keyname not in ["exec","eval"]:
            await op.finish("未知命令")

@op.got("exec",prompt="输入执行文本")
async def exechandle(text:str=ArgPlainText("exec")):
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
@op.got("eval",prompt="输入执行文本")
async def evalhandle(text:str=ArgPlainText("eval")):
    if text != None:
        try:
            try:
                result=eval(text)
                await op.send("执行结果为 %s %s" % (result,type(result)))
                await op.finish("执行成功")
            except Exception as e:
                if not isinstance(e,FinishedException):
                    await op.send("执行失败")
                    await op.finish(traceback.format_exc())
        except:
            pass