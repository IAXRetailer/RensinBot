from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger

say=on_command("say", rule=to_me(), aliases={"说",}, priority=5)

@say.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    contain=args.extract_plain_text()
    if contain == "":
        await say.finish("请输入 \"说 你要BOT说的话\"")
    else:
        await say.finish(contain)

