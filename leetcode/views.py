from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from subprocess import Popen
import subprocess
from .models import Code
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import random
import string
import re


tokens = []

PROBLEMS = [
    {
        "id": 1,
        "title": "Nth Fibonacci Sequence",
        "description": "<p>Write a program to compute nth number of a <a href=\"https://en.wikipedia.org/wiki/Fibonacci_number\">fibonacci number sequence</a>.</p><br>Starting Numbers: <code>nth_fib(1) = 0</code>, <code>nth_fib(2) = 1</code><br><br><p>Example Input & Output: </p><ul><li><code>nth_fib(2) = 1</code></li><li><code>nth_fib(6) = 5</code></li></ul><br><h4>Note:</h4><p>If you see a RecursionError, make sure you try again, the maximum number for input is 15.</p> <br><br><h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def nth_fib(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 2,
        "title": "Palindrome Checker",
        "description": "Return True if the string is a <a href='https://en.wikipedia.org/wiki/Palindrome'>palindromic string</a> (same as you read it backward as forward), given with following constraints: <ul><li>Only check  the alphanumeric part of a string,</li><li>This is case insensitive, means that RaCeCar is a palindromic string.</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"race CAR\") = True</code></li><li><code>palindrome(\"2_A3*3#A2\") = True</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "true"
    }
]

def random_str(digits=70):
    ans = ""
    for i in range(digits+1):
        ans += random.choice(string.ascii_letters + string.digits)
    return ans


def problem(request):
    return render(request, 'problems.html')

def editor(request, problem_id):
    return render(request, 'codeEditor.html', {
            "title": PROBLEMS[problem_id-1]["title"],
            "description": PROBLEMS[problem_id-1]["description"],
            "id": PROBLEMS[problem_id-1]["id"],
            "starter": PROBLEMS[problem_id-1]["starter"],
        })


import subprocess
import json

def runCode(request):
    code = request.GET.get("code", "")
    problem = int(request.GET.get("problem", 0))

    # Writing code to a temporary file
    with open("solution.py", mode="w") as solution_file:
        solution_file.write(code)

    # Running tests based on the problem
    if problem == 1:
        out = subprocess.run(["python", "-m", "unittest", "-q", "test.TestNthFibonacci"], capture_output=True, text=True)
    elif problem == 2:
        out = subprocess.run(["python", "-m", "unittest", "-q", "test.PalindromeChecker"], capture_output=True, text=True)
    else:
        return JsonResponse({"error": "Invalid problem number"})

    # Processing test results
    test_output = out.stdout.strip()
    test_errors = out.stderr.strip()


    # Constructing response
    response = {
        "stdout": {"global": test_errors},
        "error": {}  # Testcase number: error message
    }

    if test_errors:
        for line in test_errors.split("\n"):
            if "OK" in line:
                response['error'] = { 1: "passed", 2: 'passed', 3: "passed", 4: "passed", 5: "passed", 6: "passed", 7: "passed"}

            elif "FAIL" in line:
                failures_match = re.search(r'failures=(\d+)', test_errors)
                if failures_match:
                    failures = int(failures_match.group(1))
                    response["error"]["global"] = "Number of failed TestCases: " + str(failures)


            
            else:
                response["error"]["global"] = "Compilation Error: " + line
                
                
                
                
    

    response_json = json.dumps(response, indent=4)
    print("Response:", response_json)

    return JsonResponse(response)

