# from selenium import  webdriver
# # browser = webdriver.Firefox()
# browser = webdriver.PhantomJS()
# browser.get("https://www.baidu.com")
# print(browser.current_url)


# import tesserocr
# # from PIL import Image
# # image = Image.open(r'E:\SpiderMan\image.png')
# # print(tesserocr.image_to_text(image))
# print(tesserocr.file_to_text('image.png'))


# import tornado.ioloop
# import tornado.web
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("hello world")
#
# def make_app():
#     return tornado.web.Application([(r"/",MainHandler),])
#
# if __name__ == '__main__':
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run()

