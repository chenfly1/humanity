import requests
import logging
import json

# URL 地址
URL_CLAIM = "https://testnet.humanity.org/api/claim/dailyRewards"
URL_REWARDS_PAGE = "https://testnet.humanity.org/dashboard"

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 请求头，初始没有 token
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-HK,zh;q=0.9",
    "authorization": "",
    "content-length": "0",
    "origin": "https://testnet.humanity.org",
    "priority": "u=1, i",
    "referer": "https://testnet.humanity.org/dashboard",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

def load_tokens_from_file(file_path="ck.json"):
    """从 JSON 文件中加载多个 token"""
    try:
        # 尝试以 UTF-8 编码打开文件
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()  # 读取文件内容

            # 解析 JSON 数据
            tokens = json.loads(content)  

            # 确保文件中有 "tokens" 键且值为列表
            if tokens and isinstance(tokens, dict) and "tokens" in tokens:
                logging.info(f"✅ 成功加载 {len(tokens['tokens'])} 个 token。")
                return tokens["tokens"]  # 返回 tokens 列表
            else:
                logging.warning("⚠️ JSON 数据格式错误，未找到有效的 tokens 列表。")
                return []
    except FileNotFoundError:
        logging.error(f"❌ 文件 {file_path} 未找到。")
        return []
    except json.JSONDecodeError:
        logging.error(f"❌ 加载 JSON 数据时发生错误。")
        return []
    except Exception as e:
        logging.error(f"❌ 加载 tokens 时发生未知错误: {e}")
        return []

def claim_daily_rewards(token):
    """发送签到请求并获取交易哈希"""
    # 更新请求头中的 token
    HEADERS["token"] = token

    try:
        logging.info(f"正在为 token {token} 发送签到请求...")
        response = requests.post(URL_CLAIM, headers=HEADERS)
        response.raise_for_status()  # 检查 HTTP 状态码是否为 200

        # 解析响应 JSON
        data = response.json()
        if data.get("code") == "0" and "data" in data:
            txhash = data["data"].get("txhash")
            if txhash:
                logging.info(f"✅ 签到成功！交易哈希: {txhash}")
            else:
                logging.warning(f"⚠️ 签到成功，但未返回交易哈希，token: {token}")
        else:
            logging.error(f"❌ 签到失败: {data.get('msg', '未知错误')}，token: {token}")

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ 请求失败: {e}，token: {token}")

    except ValueError:
        logging.error(f"❌ 无法解析响应的 JSON 数据，token: {token}")

if __name__ == "__main__":
    # 从 JSON 文件加载多个 tokens
    tokens = load_tokens_from_file()

    # 如果加载了 tokens，则依次执行签到操作
    if tokens:
        for token in tokens:
            claim_daily_rewards(token)  # 每个 token 执行一次签到
    else:
        logging.error("未加载到有效的 tokens，无法执行签到。")
