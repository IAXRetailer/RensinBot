from nonebot import get_driver
from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)
import os
if not os.path.exists("data/reisen"):
    os.mkdir("data/reisen")
if not os.path.exists("data/reisen/cache"):
    os.mkdir("data/reisen/cache")
if not os.path.exists("data/reisen/teach"):
    os.mkdir("data/reisen/teach")

from . import hello,op,helpboard,teach,touhou,setu

'''
weather = on_command("weather", rule=to_me(), aliases={"天气", "天气预报"}, priority=5)

@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    if city_name not in ["北京", "上海"]:  # 如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        await weather.reject(city.template("你想查询的城市 {city} 暂不支持，请重新输入！"))

    city_weather = await get_weather(city_name)
    await weather.finish(city_weather)


# 在这里编写获取天气信息的函数
async def get_weather(city: str) -> str:
    return f"{city}的天气是..."
'''