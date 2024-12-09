from app.core.logger import logger
from fastapi import Request
import time


async def logger_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    done_at = time.time_ns()
    processing_time = done_at - start_time
    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "time_taker": processing_time
    }
    logger.info(log_dict)
    return response
