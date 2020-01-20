from .Karix_services import Karix_interface

def get_channel_provider_from_channel_id(channel_id):
    if channel_id=="1":
        return Karix_interface()
    else:
        raise Exception("Provide valid channel_id")
