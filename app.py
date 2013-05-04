import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

def main():
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    main()