from flask import Flask,request,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField

FAI=Flask(__name__)


@FAI.route('/html_forms',methods=['GET','POST'])
def html_forms():

    if request.method=='POST':
        fd=request.form
        return fd['un']
    return render_template('html_forms.html')


class NameForm(Form):
    name=StringField()
    submit=SubmitField()


@FAI.route('/web_forms',methods=['GET','POST'])
def web_forms():
    NFO=NameForm()

    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.name.data
    return render_template('web_forms.html',NFO=NFO)




if __name__=='__main__':
    FAI.run(debug=True)
