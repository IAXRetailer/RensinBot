from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.log import logger

op=on_command("op",rule=to_me(),aliases={"管理员","op"},priority=5,permission=SUPERUSER)

@op.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    print(args[0])