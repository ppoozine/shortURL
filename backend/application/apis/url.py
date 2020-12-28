from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, RedirectResponse
from ..models.models import UrlModel
from ..schemas.url_schema import UrlSchema, RequestUrl, ResponsesUrl
from ..schemas.common import SuccessCreate
from typing import List
from ..log.log import logger
from ..database import database
from ..core.core import short_url

router = APIRouter()

@router.post("/shortUrl", response_model=ResponsesUrl, status_code=status.HTTP_201_CREATED)
@logger.catch
async def create_short_url(create: RequestUrl):
    db_exist = await database.execute(UrlModel.select().where(UrlModel.c.old_url == create.old_url))
    if db_exist:
        query = UrlModel.select().where(UrlModel.c.old_url == create.old_url)
        a = await database.fetch_one(query)
        return {"new_url": a["new_url"]}
    else:
        old_url = create.old_url.split("://")[-1]
        new_url = "http://localhost:8000/" + short_url(old_url)
        query = UrlModel.insert().values(
            old_url=create.old_url,
            new_url=new_url
        )
        await database.execute(query)
        return {"new_url": new_url}

@router.get("/{new_url}", status_code=status.HTTP_200_OK)
@logger.catch
async def read_url(new_url: str):
    url = "http://localhost:8000/" + new_url
    query = UrlModel.select().where(UrlModel.c.new_url == url)
    a = await database.fetch_one(query)
    # return {"old_url": a["old_url"]}
    return RedirectResponse(url=a["old_url"])