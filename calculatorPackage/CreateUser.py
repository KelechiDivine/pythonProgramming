from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from faunadb.errors import BadRequest, Unauthorized

client = FaunaClient(secret="YOUR-SECRET-HERE")


def create_user(email, password):
    result = False
    try:
        result = client.query(
            q.create(
                q.collection("users"), {
                    "credentials": {"password": password},
                    "data": {"email": email}
                }
            )
        )
    except BadRequest as e:
        pass
    return result


def authenticate_user(email, password):
    result = False
    try:
        result = client.query(
            q.login(
                q.match(q.index("users_by_email"), email), {
                    "password": password}
            )
        )
    except BadRequest as e:
        pass
    return result


def get_current_user(secret_token):
    result = False
    try:
        user_client = FaunaClient(secret=secret_token)
        result = user_client.query(
            q.current_identity()
        )
    except Unauthorized as e:
        pass
    return result


def deauthenticate_user(secret_token, all_tokens=True):
    result = False
    try:
        user_client = FaunaClient(secret=secret_token)
        result = user_client.query(
            q.logout(all_tokens)
        )
    except BadRequest as e:
        pass
    return result


def change_user_password(secret_token, new_password):
    result = False
    try:
        user_info = get_current_user(secret_token)
        if user_info:
            result = client.query(
                q.update(
                    q.ref(q.collection("users"), user_info.id()), {
                        "credentials": {"password": new_password}
                    }
                )
            )
    except BadRequest as e:
        pass
    return result


def verify_user_identity(email, password, new_password):
    result = []
    try:
        user_info = client.query(
            q.get(
                q.match(q.index("users_by_email"), email)
            )
        )
        result = client.query([
            q.identify(
                q.ref(q.collection("users"), user_info["ref"].id()), password
            ),
            q.identify(
                q.ref(q.collection("users"),
                      user_info["ref"].id()), new_password
            )
        ])
    except BadRequest as e:
        pass
    return result


def delete_user(email):
    result = []
    try:
        user_info = client.query(
            q.get(
                q.match(q.index("users_by_email"), email)
            )
        )
        client.query(
            q.delete(
                q.ref(q.collection("users"), user_info["ref"].id())
            )
        )
    except BadRequest as e:
        pass
    return result


if __name__ == "__main__":
    email, password, new_password = "test@test.com", "password", "new password"
    
    # create user
    user = create_user(email, password)
    print(user)
    
    # auth user
    user_auth = authenticate_user(email, password)
    print(user_auth)
    
    # validate user token
    user_info = get_current_user(user_auth["secret"])
    print(user_info)
    
    # change user password
    user_change_pass = change_user_password(user_auth["secret"], new_password)
    print(user_change_pass)
    
    # verify password change
    user_verify_identity = verify_user_identity(email, password, new_password)
    print(user_verify_identity)
    
    # logout user
    user_deauth = deauthenticate_user(user_auth["secret"])
    print(user_deauth)
    
    # delete user profile
    user_delete = delete_user(email)
    print(user_delete)
