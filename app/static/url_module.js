const url={
    "dev":{
        "url_api_create_order":"http://127.0.0.1:6060/api/order/add",
        "url_api_modify_order":"http://127.0.0.1:6060/api/order/modify",
    },
    "prod":{
        "url_api_create_order":"http://127.0.0.1:6060/api/order/add",
        "url_api_modify_order":"http://127.0.0.1:6060/api/order/modify",
    }
}

// const env="prod";
const env="dev";

export const url_mode=url[env];
export default url_mode;