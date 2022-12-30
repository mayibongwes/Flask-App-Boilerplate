An example of a FlaskApp directory:

```python
    /yourapp   
        /config.py  
        /app  
            /__init__.py
            /routes.py  
            /models.py  
            /static/  
                /main.css
            /templates/  
                /base.html  
        /requirements.txt  
        /yourappenv
```
  
`config.py` - stores configurations for your app.  
`__init__.py` - initializes your application creating a Flask app instance.  
`routes.py` - this is where `routes` are defined.  
`models.py` - this is where you define models for your application.  
`static` - contains static files i.e. CSS, Javascript, images  
`templates` - this is where you store your `html` templates i.e. `index.html`, `layout.html`  
`requirements.txt` - this is where you store your package dependancies, you can use `pip`  
`.env` - your virtual environment for development

---
`Reference`
[Common File Structure in Flask](https://stackoverflow.com/questions/14415500/common-folder-file-structure-in-flask-app)

## How to run

``` bash
export FLASK_APP=app
flask run
```