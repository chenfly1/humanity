import requests
import logging
import json

# URL 地址
URL_CLAIM = "https://testnet.humanity.org/api/claim/dailyRewards"

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 请求头，初始没有 token
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "authorization": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

def load_tokens_from_file(file_path="ck.json"):
    """从 JSON 文件中加载多个 token"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            tokens = json.loads(content)
            if tokens and isinstance(tokens, dict) and "tokens" in tokens:
                logging.info(f"✅ 成功加载 {len(tokens['tokens'])} 个 token。")
                return tokens["tokens"]
            else:
                logging.warning("⚠️ JSON 数据格式错误，未找到有效的 tokens 列表。")
                return []
    except Exception as e:
        logging.error(f"❌ 加载 tokens 时发生错误: {e}")
        return []

def get_window_label(index):
    """根据索引返回窗口标识"""
    if index == 0:
        return "主号窗口"
    if index == 12:
        return "第 13 个窗口"
    if index == 13:
        return "第 14 个窗口"
    else:
        return f"第 {index} 个窗口"

def claim_daily_rewards(token, window_label):
    """发送签到请求并获取交易哈希"""
    HEADERS["token"] = token
    try:
        logging.info(f"[{window_label}] 正在为 token 发送签到请求...")
        response = requests.post(URL_CLAIM, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data.get("code") == "0" and "data" in data:
            txhash = data["data"].get("txhash")
            if txhash:
                logging.info(f"[{window_label}] ✅ 签到成功！交易哈希: {txhash}")
            else:
                logging.warning(f"[{window_label}] ⚠️ 签到成功，但未返回交易哈希。")
        else:
            logging.error(f"[{window_label}] ❌ 签到失败: {data.get('msg', '未知错误')}")
    except requests.exceptions.RequestException as e:
        logging.error(f"[{window_label}] ❌ 请求失败: {e}")
    except ValueError:
        logging.error(f"[{window_label}] ❌ 无法解析响应的 JSON 数据")

if __name__ == "__main__":
    tokens = load_tokens_from_file()
    if tokens:
        for i, token in enumerate(tokens):
            # 计算窗口编号
            if i == 0:
                window_label = "主号窗口"
            else:
                window_label = get_window_label((i - 1) % 3 + 1)  # 循环分配窗口编号
            claim_daily_rewards(token, window_label)
    else:
        logging.error("未加载到有效的 tokens，无法执行签到。")
