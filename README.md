# Order Project 簡易訂單系統

## 網址
https://orders.yin888.info/

## 簡介
訂單系統可以新增、查詢及修改訂單。

## 功能
*  訪客
    *   列表選單（左上角）
    <br/>![list](README_pictures/list.jpg)
    *   新增訂單
    <br/>![Add_an_order](README_pictures/Add_an_order.jpg)
    *   訂單總攬
    <br/>![Check_orders](README_pictures/Check_orders.jpg)
    *   查詢訂單
    <br/>![Query_an_order](README_pictures/Query_an_order.jpg)


## 網頁架構
![pic_web_framework](README_pictures/fastapi.png)

## 使用工具
*   AWS
    *   EC2
    <br/>可擴展的運算容量，部署網頁應用程式。
*   Python
    *   FastAPI
    <br/>開發網頁應用框架。
    *   concurrent.futures
    <br/>Python 的平行處理模組，同時執行多個任務 ( tasks ) 。
    *   dotenv
    <br/>取用.env的資訊，避免洩漏私密資訊。
    *   mysql.connector.pooling
    <br/>使用連線池，有效利用資料庫資源。
*   JavaScript
    *   Bootstrap
    <br/> Dom 模組建立及排版
*   Others
    *   Docker
    <br/>輕量級的虛擬化技術，跨平台部屬專案。
    *   nginx
    <br/>網頁伺服器，此專案應用其反向代理 ( Reverse Proxy ) 的功能。
    *   git
    <br/>版本控管工具。