from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
import pdb
# pdb.set_trace()
logger_info = logging.getLogger('info_logs')
logging.info('come here')
import pdb
# pdb.set_trace()
# Create your views here.
class IdpAPI(APIView):
    def post(self, request):
        print('come 12')
        import pdb
        # pdb.set_trace()
        try:
            input_json=request.data
            print(input_json)
            output_json = dict(zip(['Status', 'Message', 'Payload'], [200, 'Idp request data parsed successfully', input_json]))
            return Response(output_json)
        except Exception as ex:
            output_json = dict(zip(['Status', 'Message', 'Payload'], [500, f'Exception encountered: {ex}', None]))
            return output_json

