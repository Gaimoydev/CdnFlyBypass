import json
import base64
import time
import requests
from PIL import Image
from io import BytesIO
import os
import pyocr
import pyocr.builders
import fuckrequest

headers = {
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Site": "none",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Sec-Fetch-Mode": "navigate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate"
}

def gethuadongdata():
    current_time_ms = int(time.time() * 1000)  # 获取当前时间的毫秒级时间戳
    data = {
        "move": [
            {"timestamp": current_time_ms, "x": 45, "y": 259},
            {"timestamp": current_time_ms, "x": 461, "y": 254},
            {"timestamp": current_time_ms + 1000, "x": 462, "y": 254},
            {"timestamp": current_time_ms + 1000, "x": 464, "y": 254},
            {"timestamp": current_time_ms + 1000, "x": 467, "y": 254}
        ],
        "btn": 52,
        "slider": 472,
        "page_width": 504,
        "page_height": 991
    }
    return data

def getclickdata():
    data = {
        'x': 80,
        'y': 255,
        'a': 337
    }
    return data

def base64_encode(input_str):
    # Python的base64编码
    encoded_bytes = base64.b64encode(input_str.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def jiami(input_data, guard):
    _0x842f67 = {
        'aSIEL': lambda x, y: x + y,
        'NCdZx': "PTNo2n3Ev5",
        'XuCZX': lambda x, y: x < y,
        'lRJRD': lambda x, y: x ^ y,
        'BVTmo': lambda x, y: x % y
    }

    _0x393591 = _0x842f67['aSIEL'](guard, _0x842f67['NCdZx'])

    output = ''
    for _0x5a73f4 in range(len(input_data)):
        char_code = _0x842f67['lRJRD'](ord(input_data[_0x5a73f4]), ord(_0x393591[_0x842f67['BVTmo'](_0x5a73f4, len(_0x393591))]))
        output += chr(char_code)

    return base64_encode(output)


def get_captcha(session, url):
    # 设置 Tesseract OCR 的路径
    TESSERACT_PATH = r'F:\TesseractOCR\tesseract.exe'
    os.environ['TESSDATA_PREFIX'] = r'F:\TesseractOCR'

    # 获取可用的 OCR 工具
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        exit(1)
    ocr_tool = tools[0]

    # 指定 Tesseract OCR 路径
    ocr_tool.set_path(TESSERACT_PATH)

    # 获取验证码图片
    captcha_url = f"{url}/_guard/captcha.png?"
    response = session.get(captcha_url, headers=headers)
    image = Image.open(BytesIO(response.content))
    image.save('captcha.png')
    print("Image downloaded and saved as 'captcha.png'.")

    # OCR 识别
    captcha = ocr_tool.image_to_string(
        image,
        builder=pyocr.builders.TextBuilder()
    )
    print(f"Recognized CAPTCHA text: {captcha.strip()}")

    # 获取 cookies
    cookies = response.cookies.get_dict()
    guard = cookies.get('guard', '')
    capt = cookies.get('capt', '')

    return guard, captcha.strip(), capt

def get_data(session, url):
    response = session.get(url, headers=headers)
    content = response.text
    if 'captcha_html' in content:
        return "captcha12345", content
    cookies = response.cookies.get_dict()
    guard = cookies.get('guard', '')
    return guard, content

def determine_type(content):
    if 'click_html' in content:
        print("类型为点击验证")
        return 2
    elif 'slider_html' in content:
        print("类型为滑块验证")
        return 1
    elif 'delay_jump' in content:
        print("类型为五秒盾验证")
        return 3
    elif 'auto.js' in content:
        print("类型为JS验证")
        return 4
    elif 'captcha_html' in content:
        print("类型为验证码验证")
        return 5
    else:
        return None

def jiami2(input_data, guard):
    _0x842f67 = {
        'aSIEL': lambda x, y: x + y,
        'NCdZx': "PTNo2n3Ev5",
        'XuCZX': lambda x, y: x < y,
        'lRJRD': lambda x, y: x ^ y,
        'BVTmo': lambda x, y: x % y
    }

    _0x393591 = _0x842f67['aSIEL'](guard, _0x842f67['NCdZx'])

    input_data_str = str(input_data)
    output = ''
    for _0x5a73f4 in range(len(input_data_str)):
        char_code = _0x842f67['lRJRD'](ord(input_data_str[_0x5a73f4]), ord(_0x393591[_0x842f67['BVTmo'](_0x5a73f4, len(_0x393591))]))
        output += chr(char_code)

    return base64_encode(output)

def jiami_wrapper(input_data, guard):
    jiamidata = jiami(json.dumps(input_data), guard)
    return jiamidata

def jiami_wrapper2(input_data, guard):
    jiamidata = jiami2(input_data, guard)
    return jiamidata

# 定义主函数
def delay_value(time_num_plain):
    if isinstance(time_num_plain, str):
        time_num_plain = int(time_num_plain)
    result1 = time_num_plain - 2
    result2 = result1 + 17
    _0x552e00 = result2 + time_num_plain

    return _0x552e00

def js_value(time_num_plain):
    if isinstance(time_num_plain, str):
        time_num_plain = int(time_num_plain)
    result1 = time_num_plain - 2
    result2 = result1 + 18
    _0x552e00 = result2 + time_num_plain

    return _0x552e00

url = input("请输入请求的URL: ")

def unicode_representation(s):
    return ''.join(f'\\u{ord(c):04x}' for c in s)

with requests.session() as session:
    capt = None
    guard, content = get_data(session, url)
    if not guard:
        print("无法从cookie中获取guard值")
    else:
        guard_prefix = guard[:8]
        guard_suffix = guard[-2:]
        xuanxiang = determine_type(content)

        if xuanxiang == 1:
            input_data = gethuadongdata()
            encrypted_data = jiami_wrapper(input_data, guard_prefix)
            guardret = encrypted_data.strip()
            print(f"guard={guard}")
            print(f"guardret={guardret}")
        elif xuanxiang == 2:
            input_data = getclickdata()
            encrypted_data = jiami_wrapper(input_data, guard_prefix)
            guardret = encrypted_data.strip()
            print(f"guard={guard}")
            print(f"guardret={guardret}")
        elif xuanxiang == 3:
            guard_num = delay_value(guard_suffix)
            print(f"guard={guard}")
            print(f"guard_num={guard_num}")
            encrypted_data = jiami_wrapper2(guard_num, guard_prefix)
            guardret = encrypted_data.strip()
            print(f"guardret={guardret}")
        elif xuanxiang == 4:
            guard_num = js_value(guard_suffix)
            print(f"guard={guard}")
            print(f"guard_num={guard_num}")
            encrypted_data = jiami_wrapper2(guard_num, guard_prefix)
            guardret = encrypted_data.strip()
            print(f"guardret={guardret}")
        elif xuanxiang == 5:
            guard, captcha, capt = get_captcha(session, url)
            print(f"guard={guard}")
            guardret = captcha.strip()
            print(f"guardret={captcha}")
        else:
            print("返回内容无法匹配到已知的类型")
            exit()

        guardok = fuckrequest.request(url, guard, guardret, capt)
        if not guardok:
            print("没有绕过成功")
        else:
            print(f"guardok={guardok}") #对于5秒盾和JS验证是无效的 请自行http发请求查看
