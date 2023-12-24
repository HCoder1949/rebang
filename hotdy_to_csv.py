import requests, csv, time, os
# -*- coding: UTF-8 -*-

# url='https://creator.douyin.com/aweme/v1/creator/data/billboard_list/?billboard_type_list=1'

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求不成功则引发异常检查响应的HTTP状态码，如果状态码表示错误，比如 404 表示资源未找到，或者 500 表示服务器内部错误，它就会引发一个HTTPError异常。
        json_data = response.json()  # 将响应内容解析为JSON格式的数据。
        #print(json_data)
        return json_data
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    time = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    year, month, day = time.split()[0].split("-")

    api_url = "https://creator.douyin.com/aweme/v1/creator/data/billboard_list/?billboard_type_list=9"  # API接口地址
    api_data = get_api_data(api_url)

    if api_data:
        '''for key in list(api_data['billboard_data']['element_list'])[0:-1]:'''
        for key in list(api_data['billboard_data']):
            print(key)
            for key2 in list(key['element_list'])[0:-1]:
                #print(key2)
                indexs = [item["rank"] for item in key['element_list']]
                titles = [item["title"] for item in key['element_list']]#
                #print('%s' % key2)
                #print(titles)
                hots = [item["value"] for item in key['element_list']]#['%s' % key2]]

                #hrefs = [item["href"] for item in key['element_list']]#['%s' % key2]]

                path = os.path.join('archives', year, month, day)
                os.makedirs(path, exist_ok=True)

                with open(os.path.join(path, '%s.csv' % time), mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(["index", "hot", "title", "href"])  # 写入标题行
                    for item1, item2, item3 in zip(indexs, hots, titles):
                        writer.writerow([item1, item2, item3])
                print("Data saved successfully!")
