The BigPanda Backend Exercise challenge
by: Dudi Spivak
email: dudisp@gmail.com

This project was written in python 3 on a windows environment.
It should run on any OS but the generator is windows-specific so if you need to replace it,
it's in `src/consumer/generator-windows-amd64.exe` and update the const with the name in src/consumer/Consumer.py:9

Running is running the main method in src/main.py

Server port is 8080.

3 things I would a improve:
    1. I'm not too happy about the http server and how I referenced to the statistics manager.
    2. Exception catching in Validator is too broad and catches all exceptions.
    3. I hate the name StatisticsManager but couldn't think of anything else.
