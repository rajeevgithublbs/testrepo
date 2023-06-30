import json, requests
import azure.functions as func
def main():
 request_json= req.get_json()
 return func.HttpResponse(request_json)
 
