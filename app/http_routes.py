import json

from flask import Blueprint, Response

from app.message_handler import get_messages, pop_message, reset_messages

routes = Blueprint("routes", __name__)


class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        return json.JSONEncoder.default(self, obj)


@routes.route("/get_messages", methods=["GET"])
def get_messages_route():
    return Response(
        json.dumps(get_messages(), cls=BytesEncoder),
        status=200,
        content_type="application/json",
    )


@routes.route("/pop_message", methods=["GET"])
def pop_message_route():
    try:
        return Response(pop_message(), status=200)
    except IndexError:
        return Response(status=404)


@routes.route("/reset_messages", methods=["GET"])
def reset_messages_route():
    reset_messages()
    return Response(
        status=200,
    )
