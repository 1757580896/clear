import re
import requests

def 提取频道名称():
    url = "https://raw.githubusercontent.com/bharing19/List1/main/1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # 更精确的正则表达式，匹配 #EXTINF:-1, 后面的频道名称
        # 直到行尾或遇到 \n 换行符
        模式 = r'#EXTINF:-1,(.*?)(?:\n|$)'
        匹配结果 = re.findall(模式, response.text)
        
        if not 匹配结果:
            print("警告：没有找到任何匹配的频道名称")
            return []
        
        # 清理数据：去除前后空白字符并去重
        清理后的结果 = [匹配项.strip() for 匹配项 in 匹配结果 if 匹配项.strip()]
        去重后的结果 = list(set(清理后的结果))
        
        # 按字母顺序排序
        去重后的结果.sort()
        
        # 打印结果
        print(f"共找到 {len(去重后的结果)} 个唯一频道名称：")
        for 频道 in 去重后的结果:
            print(频道)
            
        # 将结果保存到文件
        with open('频道列表.txt', 'w', encoding='utf-8') as 文件:
            文件.write('\n'.join(去重后的结果))
            
        return 去重后的结果
        
    except Exception as 错误:
        print(f"发生错误: {错误}")
        return []

if __name__ == "__main__":
    提取频道名称()
