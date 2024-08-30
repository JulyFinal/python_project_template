from fastapi import FastAPI

import logging
from loguru import logger

# 修改 fastapi 的日志为 loguru 格式


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # 既存のログレコードの属性を使用してLoguruでログを出力
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def setup_logger():
    # uvicornログをInterceptHandlerにリダイレクト
    for _logger in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logging_logger = logging.getLogger(_logger)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False  # ログが２重出力されるのを防止


setup_logger()


app = FastAPI()


@app.get("/")
async def index():
    return "Hello, World!"
