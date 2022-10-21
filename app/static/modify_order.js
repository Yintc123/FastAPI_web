import * as url from './url_module.js';
import * as order from './order_module.js';

const submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', async ()=>{
    // 拿取輸入值
    const input_order_id = document.querySelector('#order_id').value;
    // AJAX，根據訂單編號拿取訂單資訊
    const order_info = await order.get_order(input_order_id);
    // 如果無訂單資訊獲釋返回 order_info.detail
    if(!order_info || order_info.detail){
        // 跳出錯誤訊息的警告
        alert("Error! There's no this order, order_id = " + input_order_id + " .");
        return;
    }
    // 如果有訂單資訊，跳轉至修改訂單頁面
    window.location = url.url_mode['url_order_id'] + input_order_id;
})