# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import face

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'videos',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        #return redirect(url_for('/'))
    return render_template('upload.html')

@app.route('/query', methods=['POST', 'GET'])
def query_files():
  path = os.getcwd()
  responsetext = ''
  count = 0
  for files in os.walk(path + "\\videos"):
    for each in files[2]:
      count += 1
      responsetext += '<tr><td>' + str(count) + '</td><td>' + each + '</td><td></td>' + '<td><button type="submit" class="btn btn-default btn-sm" onclick="face_recognize(\'' + each + '\')">识别</button></td>'  
  return responsetext

@app.route('/faceRecognize/<filename>')
def face_recognize(filename):
  print(filename)
  return face.face_recognize(filename)
   

if __name__ == '__main__':
    app.run(debug=True)