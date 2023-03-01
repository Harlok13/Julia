from pydantic import BaseSettings, SecretStr, RedisDsn, validator
from typing import Optional


class Settings(BaseSettings):
    bot_token: SecretStr
    bot_fsm_storage: str
    redis_dsn: Optional[RedisDsn]
    app_host: Optional[str] = '0.0.0.0'
    app_port: Optional[int] = 8000
    webhook_domain: Optional[str]
    webhook_path: Optional[str]

    @validator('fsm_mode')
    def fsm_type_check(cls, v):
        if v not in ('redis', 'memory'):
            raise ValueError('Incorrect value of fsm_mode. Must be one of: redis, memory')
        return v

    @validator('redis')
    def skip_validating_redis(cls, v, values):
        if values['fsm_mode'] == 'redis' and v is None:
            raise ValueError('Redis config is missing, though fsm_type is "redis"')
        return v

    @validator('webhook_path')
    def validate_webhook_path(cls, v, value):
        if value['webhook_domain'] and not v:
            raise ValueError('Webhook path is missing')
        return v

    class Config:
        env_file = '.env'
        env_file_config = 'utf-8'


config = Settings()
