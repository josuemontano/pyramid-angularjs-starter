import os

from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow

from ..models import User, Role
from .token_factory import TokenFactory


class RootFactory(object):
    """Permission definitions"""
    __acl__ = [(Allow, Role.USER, 'view'),
               (Allow, Role.ADMIN, ('admin', 'view'))]

    def __init__(self, request):
        self.request = request


def groupfinder(userid, request):
    user = request.user
    if user is not None:
        return [user.role]
    return None


def get_current_user(request):
    userid = request.unauthenticated_userid
    user = request.dbsession.query(User).get(userid)
    if user.deleted_at is None:
        return user
    return None


def includeme(config):
    config.include('pyramid_jwt')

    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(os.environ.get('JWT_SECRET', 'secret'), callback=groupfinder)

    config.add_request_method(get_current_user, name='user', reify=True)
