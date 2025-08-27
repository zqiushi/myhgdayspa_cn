import requests
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 设置代理
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

# 配置重试策略
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount('https://', adapter)
session.mount('http://', adapter)

# 创建images文件夹（如果不存在）
os.makedirs('images', exist_ok=True)

# 需要下载的图片URL列表
image_urls = [
    'https://picsum.photos/id/64/100/100',
    'https://picsum.photos/id/91/100/100',
    'https://picsum.photos/id/55/100/100',
    'https://picsum.photos/id/22/100/100',
    'https://picsum.photos/id/65/100/100',
    'https://picsum.photos/id/92/100/100',
    'https://picsum.photos/id/21/800/600',
    'https://picsum.photos/id/26/800/500',
    'https://picsum.photos/id/96/800/500',
    'https://picsum.photos/id/177/100/100',
    'https://picsum.photos/id/1059/800/600',
    'https://picsum.photos/id/1060/800/600',
    'https://picsum.photos/id/1060/1920/1080',
    'https://picsum.photos/id/237/600/800',
    'https://picsum.photos/id/28/600/400',
    'https://picsum.photos/id/29/600/400',
    'https://picsum.photos/id/106/600/400',
    'https://picsum.photos/id/1048/800/600',
    'https://picsum.photos/id/1058/800/600',
    'https://picsum.photos/id/1031/1200/400',
    'https://picsum.photos/id/1068/800/600',
    'https://picsum.photos/id/1070/1200/675',
    'https://picsum.photos/id/1065/600/400',
    'https://picsum.photos/id/65/800/500',
    'https://picsum.photos/id/36/800/600',
    'https://picsum.photos/id/137/800/600',
    'https://picsum.photos/id/116/800/600',
    'https://picsum.photos/id/174/800/600',
    'https://picsum.photos/id/1071/1200/675',
    'https://picsum.photos/id/1076/600/400',
    'https://picsum.photos/id/1077/600/400',
    'https://picsum.photos/id/1078/600/400',
    'https://picsum.photos/id/1079/600/400',
    'https://picsum.photos/id/1080/600/400',
    'https://picsum.photos/id/1081/600/400',
    'https://picsum.photos/id/101/1200/400'
]

# 下载并保存图片
for url in image_urls:
    try:
        # 解析URL获取图片ID、宽度和高度
        parts = url.split('/id/')[1].split('/')
        if len(parts) < 3:
            print(f"跳过无效URL: {url}")
            continue
        img_id, width, height = parts[0], parts[1], parts[2]
        filename = f"picsum-{img_id}-{width}-{height}.jpg"
        filepath = os.path.join('images', filename)

        # 下载图片
        response = session.get(url, proxies=proxies, timeout=15)
        response.raise_for_status()  # 检查HTTP错误

        # 保存图片
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"已保存: {filename}")
    except Exception as e:
        print(f"下载失败 {url}: {str(e)}")

print("所有图片下载任务已完成")