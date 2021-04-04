# Python script examples

## Requirements:
- Python installed - version agnostic
- Terminal / IDE with Terminal or WinPython Command Prompt.exe for Windows

## Folder Contents

**EulerProjectCode** - Contains a few solutions to the Project Euler Archives found [here](https://projecteuler.net/about)

**LambdaExample** - Contains an AWS Lambda Solution for Project Euler 25

**ETLexample** - Simple Extract Transform and Display(Load) example

## How to run
Clone this repository and then using your favourite terminal, open your folder/directory of choice (EulerProjectCode). Whilst in the directory you can run your chosen script in the terminal as follows:

`python <script-name>.py`

eg.

`python eulpy25.py`

All scripts are self contained and will print output to the command line without need for external input.

## To run Tests
For each script there is a corresponding test and to run the test you would use the following command in terminal:

`python <script-name>Test.py`

eg.

`python eulpy25Test.py`



## Docker (Optional)

No python, no problem... If you have Docker installed then run the following to spin the solution up in a container:

Build the image with `docker build -t proj-eul:v1.0.0 .`

Once built you can run the container with `docker run -it proj-eul:v1.0.0 eulpy25.py` 

## AWS Lambda (Optional)

You can either copy and paste the code directly from /LambdaExample/eulpy25Lambda.py or zip the folder as follows:

`zip -r /LambdaExample .`

and Upload it as a zip file in AWS Lambda with the **Upload from** button. 
OR
Use the zip file that has already been created - `LambdaExample.zip`



