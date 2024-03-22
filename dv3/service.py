import os
import socket

from googleapiclient import discovery
from google.oauth2 import service_account
from google.auth import default
from google.auth import impersonated_credentials


def build_service(sa_principal: str, credential_path: str = None, timeout: int = 480) -> discovery.Resource:
    """
    Builds an impersonated service that can interact with the DV360 API.

    This function creates a service client for interacting with the Display & Video 360 (DV360) API,
    using either a provided service account file or default credentials, and then impersonates another service account
    specified by `sa_principal`. It sets a custom network timeout and retries for the created service client.

    Args:
        sa_principal (str): The email identifier of the service account to impersonate.
        credential_path (str, optional): Path to the service account JSON file. Uses application default credentials if not provided.
        timeout (int, optional): Custom network timeout in seconds. Defaults to 480.

    Returns:
        googleapiclient.discovery.Resource: An authenticated Resource object for interacting with the DV360 API.

    Raises:
        FileNotFoundError: If the `credential_path` is provided but the file does not exist.
        GoogleAuthError: If there is an issue authenticating with Google's API.
        Exception: For other unexpected errors during the service creation process.
    """
    target_scopes = ['https://www.googleapis.com/auth/display-video']

    try:
        if credential_path:
            print(f"Using provided credentials: {credential_path}")
            if not os.path.exists(credential_path):
                raise FileNotFoundError(f"The provided credential file was not found: {credential_path}")
            source_credentials = service_account.Credentials.from_service_account_file(
                credential_path,
                scopes=target_scopes
            )
        else:
            print("Using default credentials")
            source_credentials, _ = default(
                scopes=target_scopes
            )

        print(f"Using impersonated credentials: {sa_principal}")
        target_credentials = impersonated_credentials.Credentials(
            source_credentials=source_credentials,
            target_principal=sa_principal,
            target_scopes=target_scopes,
            quota_project_id=os.environ.get("QUOTA_PROJECT_ID"),
            lifetime=500
        )
        #
        if os.environ.get("QUOTA_PROJECT_ID"):
            target_credentials._quota_project_id = os.environ.get("QUOTA_PROJECT_ID")

        socket.setdefaulttimeout(timeout)

        service = discovery.build(
            'displayvideo',
            'v3',
            credentials=target_credentials,
            cache_discovery=False,  # Avoids cache discovery problems
            num_retries=3
        )
        return service
    except Exception as e:
        raise DV360ServiceInitError(f"Failed to build DV360 service. {e}")


class DV360ServiceInitError(Exception):
    pass
