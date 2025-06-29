"""
Middleware for the FastAPI application
"""

import time
import logging
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


def add_middleware(app: FastAPI):
    """Add middleware to the FastAPI application"""
    
    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        """Log all HTTP requests"""
        start_time = time.time()
        
        # Log request
        logger.info(f"{request.method} {request.url.path} - {request.client.host if request.client else 'unknown'}")
        
        try:
            response = await call_next(request)
            process_time = time.time() - start_time
            
            # Log response
            logger.info(f"{request.method} {request.url.path} - {response.status_code} - {process_time:.3f}s")
            
            # Add custom headers
            response.headers["X-Process-Time"] = str(process_time)
            response.headers["X-API-Version"] = "0.2.0"
            
            return response
            
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(f"{request.method} {request.url.path} - ERROR: {str(e)} - {process_time:.3f}s")
            
            # Return error response
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal server error",
                    "message": str(e),
                    "path": request.url.path,
                    "method": request.method
                }
            )
    
    @app.middleware("http")
    async def security_headers_middleware(request: Request, call_next):
        """Add security headers"""
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        return response