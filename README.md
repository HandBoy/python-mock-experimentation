## About Mock

Basically we can replace the object which is specified as a first argument for “mock.patch” with MagicMock instance or any object you specified as a second argument. This is very useful when you write unit test to control other module behavior the module tested depends on.


## To install

Create a venv and install requirements:
``` shell
$ sudo pip install virtualenv
$ which python3
$ virtualenv --python='path showed with which command' env
$ source env/bin/activate
$ pip install -r requirements.txt

```


## To Run  
pytest test_mock.py


## Git

…or create a new repository on the command line
``` shell
echo "# python-mock-experimentation" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/HandBoy/python-mock-experimentation.git
git push -u origin master
```   

…or push an existing repository from the command line
``` shell
git remote add origin https://github.com/HandBoy/python-mock-experimentation.git
git push -u origin master
```



## References
- https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais
- https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1
- https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code

- https://medium.com/uckey/how-mock-patch-decorator-works-in-python-37acd8b78ae
- https://realpython.com/testing-third-party-apis-with-mocks/
- https://realpython.com/python-mock-library/