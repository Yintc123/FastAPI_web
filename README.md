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
    <br/> * 點擊 Order_id 進入修改訂單頁面
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
    *   asyncio
    <br/>Python 的非同步處理模組，藉由 await 等待過程切換至 Event loop 執行其他 Task 。
    *   dotenv
    <br/>取用.env的資訊，避免洩漏私密資訊。
    *   sqlAlchemy
    <br/>Python 的 ORM 套件，可以避免 SQL Injection。
*   JavaScript
    *   Bootstrap
    <br/> Dom 模組建立及排版
*   Others
    *   Docker
    <br/>輕量級的虛擬化技術，跨平台部屬專案，此專案使用 dcoker-compose 將 Web app 與 MySQL 同時部署置EC2。
    *   nginx
    <br/>網頁伺服器，此專案應用其反向代理 ( Reverse Proxy ) 的功能。
    *   git
    <br/>版本控管工具。