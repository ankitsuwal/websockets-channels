from rest_framework import permissions
from rest_framework.response import Response

def custom_render_data(status=None, message=None, response_status=None, token =None, data={}):
    if isinstance(data,bool):
        """
        This specific condition is written if Fronuser want data empty list
        """
        return  Response({"status": status, "data": [], "message": message}, status=response_status)
    
    if len(data) >= 1 or data == [] :
        if token:
            response =   Response({"status": status,  "data": data, "message": message, "token":token}, status=response_status)
        else :
            response = Response({"status": status, "data": data, "message": message}, status=response_status)
    else:
        if token:
            response = Response({"status": status, "message": message, "token":token}, status=response_status)
        else:
            response =  Response({"status": status,  "message": message}, status=response_status)

    if token:
        response['Authorization'] = 'Token ' + token

    return response


class SkipAuth(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return True