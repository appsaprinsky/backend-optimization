from django.shortcuts import render
from django.http import HttpResponse
import subprocess


def index(request):
    return HttpResponse("Hello, world. Welcome to optimization website!")

def solve_knapsack(request):
    executable_path = "./branch-and-bound.out"
    try:
        result = subprocess.run(executable_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output of the executable:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the executable:")
        print(e.stderr)
    return HttpResponse(result.stdout)


