from nonebot import on_message
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger

helpboard=on_message(rule=to_me(),priority=2)

@helpboard.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    await helpboard.finish('''   
1.说
2.搜图''')