import httplib2
import os
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage

credentials_path = "cled.json"
if os.path.exists(credentials_path):
    store = Storage(credentials_path)
    credentials = store.get()
else:
    f = "client.json"
    scope = "https://www.googleapis.com/auth/youtube.readonly"
    flow = client.flow_from_clientsecrets(f, scope)
    flow.user_agent = "test"
    credentials = tools.run_flow(flow, Storage(credentials_path))
