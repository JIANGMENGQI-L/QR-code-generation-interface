# python二维码生成接口
##接口概要：

###接口地址：http://127.0.0.1/qr/（可替换为服务器域名）
###支持协议：http，https
###图片格式：PNG
###请求方式：GET
###请求示例：http://127.0.0.1/qr/?text=测试
http://127.0.0.1/qr/?text=测试&box_size=500
###接口备注：接口支持跨域请求，可以用于前端跨域应用

##请求参数：

| 参数名 | 类型   | 默认值 | 是否必须 | 说明                     |
| ------ | ------ | ------ | -------- | ----------------------- |
| text   | String | 无     | 是       | 需要生成的二维码的文本，值建议urlEncode处理 |
| box_size | Number | 10    | 否       | 二维码的尺寸，单位像素块，1box_size = 33px |

##使用限制：
本API可用于个人或商业用途，仅限用于合法场景，请勿用于任意不合法用途。
作者：江梦琦

#QR Code API Documentation
Python QR Code Generation API
##Overview:
This API provides the functionality to generate QR codes in Python.

###API Address:
http://127.0.0.1/qr/ (Replace with server domain name)

###Supported Protocols:
http, https

###Image Format:
PNG

###Request Method:
GET

###Request Example:
http://127.0.0.1/qr/?text=测试
http://127.0.0.1/qr/?text=测试&box_size=500

###API Notes:
The API supports cross-origin requests and can be used for frontend cross-origin applications.

##Request Parameters:
| Parameter Name | Type  | Default | Required | Description                     |
| ------ | ------ | ------ | -------- | ----------------------- |
| text   | String | Null     | yes       | The text to be generated into the QR code. It is recommended to urlEncode the value. |
| box_size | Int | 10    | no      | box_size	Number	10	No	The size of the QR code in pixel blocks. 1 box_size = 33px |

##Usage Restrictions:
This API can be used for personal or commercial purposes only and is limited to legal scenarios. Please do not use it for any unauthorized purposes.

Author:Mengqi Jiang
