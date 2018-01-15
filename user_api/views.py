from cornice import Service
from pyramid.view import view_config
from pyramid.renderers import render_to_response

_USERS = {}

values = Service(name='users',
                 path='/user/',
                 description="Python Piramid API")

@view_config(route_name='user.getAll', renderer='json')
def get_users(request):
    """Get full list of users"""
    users = _USERS
    return {"name": "username", "age": 21}

# @view_config(route_name='api.value.get')
# @values.get()
# def get_value(request):
#     """Returns the value.
#     """
#     key = request.swagger_data['_id']
#     return _VALUES.get(key)


# @view_config(route_name='api.value.set')
# @values.post()
# def set_value(request):
#     """Set the value.

#     Returns *True* or *False*.
#     """
#     key = request.matchdict['value']
#     try:
#         # json_body is JSON-decoded variant of the request body
#         _VALUES[key] = request.json_body
#     except ValueError:
#         return False
#     return True