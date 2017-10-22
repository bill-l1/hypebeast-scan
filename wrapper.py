import web

import io
import os

from google.cloud import vision
from google.cloud.vision import types

from scan import *

from web import form

render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)
imageUrl = form.Form(
    form.Textbox('fileName', form.notnull, class_="textEntry")
)
class index:
    def GET(self, URL):
        print URL
        data = web.input()
        if data:
            if data.fileName:
                scoreList = scanImg(data.fileName)
                if scoreList:
                    return render.scoreScreen(scoreList, data.fileName)
                else:
                    return render.fourohfour()
            else:
                newForm = imageUrl()
                return render.index(newForm)
        else:
            newForm = imageUrl()
            return render.index(newForm)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
