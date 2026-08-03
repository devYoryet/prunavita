"""Genera URL de autorizacion OAuth y espera callback en localhost:8090."""
from pathlib import Path
from google_auth_oauthlib.flow import Flow

ROOT = Path(__file__).resolve().parents[1]
CLIENT = next(ROOT.glob("client_secret*.json"))
SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]

flow = Flow.from_client_secrets_file(
    str(CLIENT),
    scopes=SCOPES,
    redirect_uri="http://localhost:8090/",
)
auth_url, _ = flow.authorization_url(
    access_type="offline",
    include_granted_scopes="true",
    prompt="consent",
)
print("AUTH_URL=" + auth_url, flush=True)
creds = flow.run_local_server(port=8090, open_browser=False, prompt="consent")
token_path = ROOT / ".google-token.json"
token_path.write_text(creds.to_json(), encoding="utf-8")
print("TOKEN_SAVED=1", flush=True)
