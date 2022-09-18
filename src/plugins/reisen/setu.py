from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger
#import pixivpy_async

#API=

setu=on_command("setu", rule=to_me(), aliases={"色图",}, priority=5)
#pixivpy_async.


@setu.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    await setu.finish("没有,只有龙图(")