import re
import requests

def 提取并去重():
    # 目标URL
    url = "https://raw.githubusercontent.com/bharing19/List1/main/1"
    
    try:
        # 获取内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 使用正则表达式提取 #EXTINF:-1, 和 http 之间的文本
        模式 = r'#EXTINF:-1,(.*?)http'
        匹配结果 = re.findall(模式, response.text, re.MULTILINE)
        
        # 清理数据：去除前后空白字符并去重
        清理后的结果 = [匹配项.strip() for 匹配项 in 匹配结果]
        去重后的结果 = list(set(清理后的结果))
        
        # 按字母顺序排序
        去重后的结果.sort()
        
        # 打印结果
        print("提取到的唯一项目：")
        for 项目 in 去重后的结果:
            print(项目)
            
        # 将结果保存到文件
        with open('提取结果.txt', 'w', encoding='utf-8') as 文件:
            文件.write('\n'.join(去重后的结果))
            
        return 去重后的结果
        
    except Exception as 错误:
        print(f"发生错误: {错误}")
        return []

if __name__ == "__main__":
    提取并去重()
