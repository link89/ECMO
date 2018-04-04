import os
import json
import logging
from urllib.request import urlopen

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PORT = os.environ.get("PORT", 8888)

KEYCLOAK_OPENID_CONFIG_URL = os.environ.get("KEYCLOAK_OPENID_CONFIG_URL")
fp = urlopen(KEYCLOAK_OPENID_CONFIG_URL)
try:
    KEYCLOAK_OPENID_CONFIG = json.load(fp)
finally:
    fp.close()

logger.info("keycloak openid config: %s", KEYCLOAK_OPENID_CONFIG)

KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET")

