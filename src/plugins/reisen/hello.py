from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger

say=on_command("say", rule=to_me(), aliases={"说",}, priority=5)

@say.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    await say.finish(args)

textconv=on_command("textconv",rule=to_me(),aliases={"文本转换"},priority=5)
@textconv.handle()
async def handle(matcher:Matcher,args:Message=CommandArg()):
    await textconv.finish(str(args))