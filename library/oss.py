import base64
import hashlib
import hmac
import json
from datetime import datetime, timedelta
from typing import Any, Dict
from tornado.options import define, options
import orjson


class OSSService():
    """ali-oss"""

    @classmethod
    def _upload_dir(cls) -> str:
        now = datetime.now()
        return 'toyshow/pts/2023/test/edu/{}/{:02d}/'.format(now.year, now.month)

    @classmethod
    def gen_oss_token_info(cls) -> Dict[str, Any]:
        expire_dt = datetime.now() + timedelta(days=180)

        policy_info = {
            'expiration': expire_dt.isoformat() + 'Z',
            'conditions': [['starts-with', '$key', cls._upload_dir()]],
        }
        policy = base64.b64encode(orjson.dumps(policy_info))

        h_sha1 = hmac.new(options.oss_secret.encode(), policy, digestmod=hashlib.sha1)
        signature = base64.b64encode(h_sha1.digest().strip())

        return {
            'accessid': options.oss_key,
            'host': options.oss_url,
            'policy': policy.decode(),
            'signature': signature.decode(),
            'expire': int(expire_dt.timestamp()),
            'dir': cls._upload_dir(),
        }
