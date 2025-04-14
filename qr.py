import qrcode
# 输入网址
url = "https://ua-huang.github.io/my-resume/"
# 生成二维码
img = qrcode.make(url)
# 保存图片
img.save("website_qr.png")
print("二维码已生成！")