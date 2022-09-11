from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger

helpboard=on_command("help",rule=to_me(),aliases={"帮助"})

@helpboard.handle()
async def handle(matcher: Matcher, args: Message = CommandArg()):
    args=args.extract_plain_text()
    if args == "":
        await helpboard.finish("正确用法 '帮助 模块',比如 '帮助 帮助'")
    elif args == "帮助":
        await helpboard.finish(
            '''0.帮助
1.教
2.其他功能
3.管理员

使用 '帮助 模块' 来查询吧!'''
        )
    elif args == "教":
        await helpboard.finish(
            '''1.查询关键词
2.添加关键词
3.删除关键词
4.删除所有关键词(超管)'''
        )
    elif args == "管理员":
        await helpboard.finish(
            '''1.exec'''
        )
    elif args == "其他功能":
        await helpboard.finish(
            '''1.搜图（外置插件nonebot_plugin_picsearcher）
2.说'''
        )