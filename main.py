
def classify(message):
    if "退款" in message:
        return "refund"
    elif "订单" in message:
        return "order"
    elif "物流" in message or "发货" in message:
        return "shipping"
    elif "你好" in message:
        return "greet"
    return "other"

def reply(intent):
    responses = {
        "refund": "您可以在订单页面申请退款。",
        "order": "请提供订单号，我帮您查询。",
        "shipping": "一般1-3天内发货，请耐心等待。",
        "greet": "您好！我是AI客服。",
        "other": "抱歉，我还在学习中。"
    }
    return responses[intent]

def main():
    print("AI客服系统启动（输入 exit 退出）")
    while True:
        msg = input("你：")
        if msg.lower() == "exit":
            print("再见！")
            break
        intent = classify(msg)
        print("AI：", reply(intent))

if __name__ == "__main__":
    main()
