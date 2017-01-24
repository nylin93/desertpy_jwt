# Flask REST API secured with JWT                                                                                                                                                                           
The repository for Nathan's Desertpy talk on January 25, 2017. 


### pyenv
It is written in Python 3.4.1. There should not be any major difference between differing 3.X.X versions, but I have included a pyenv .python-version file, so, if you have pyenv installed and 3.4.1 installed through pyenv, you are good to go. 

If you don't have pyenv installed, [go download it](https://github.com/yyuu/pyenv), follow its instructions, then run `pyenv install 3.4.1`.

### virtualenv
It does not come with a virtualenv directory, instead it comes with a requirements.txt file, so you can just `virtualenv venv` and then `pip3 install -r requirements.txt`. This way is better in the event you are running a different 3.X.X version. 

### MongoDB
It runs on MongoDB for the backend, you can [download it here](https://www.mongodb.com/download-center#community)

### Branches
`Master` is the _uncompleted_ version. If we have time we will walk through and fill in the missing pieces together. The `completed` branch has all the endpoints protected from CSRF and requires the JWT for authentication. 
