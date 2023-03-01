from pydantic import BaseSettings, SecretStr, RedisDsn, validator
from typing import Optional


class Settings(BaseSettings):
    bot_token: SecretStr
    fsm_mode: str
    redis: Optional[RedisDsn]

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

    class Config:
        env_file = '.env'
        env_file_config = 'utf-8'


config = Settings()
