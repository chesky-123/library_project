from fastapi import APIRouter ,HTTPException
from logs.loger_config import logger
from database.member_db import ConnectDb ,Member_db



router = APIRouter(prefix="/members")
db = ConnectDb()
member_db = Member_db()



@router.post("/member_table")
def create_member_table():
    logger.info("POST /create member table")
    try:
        db.create_member_table()
        return "member table created successful"
    except Exception as e:
        logger.error(e)


@router.post("/")
def create_member(data:dict):
    logger.info("POST /members")
    try:
        member = member_db.create_member(data)
        if member:
            return "member create successful"
        else:
            raise HTTPException(status_code=404 ,detail="somthing is vrong")
    except Exception as e:
        logger.error(e)

@router.get("/")
def get_all_members():
    logger.info("GET /members")
    try:
        members = member_db.get_all_members()
        return members
    except Exception as e:
        logger.error(e)

@router.get("/{id}")
def get_member_by_id(id):
    logger.info("GET /(id)")
    try:
        return member_db.get_member_by_id(id)
    except Exception as e:
        logger.error(e)

@router.put("/{id}")
def update_member(id,data:dict):
    logger.info("PUT /(id)")
    try:
        member = member_db.update_member(id ,data)
        if member:
            return "member update successful"
        raise HTTPException(status_code=404 ,detail="sumthing wrong")
    except Exception as e:
        logger.error(e)

@router.put("/{id}/deactivate")
def deactivate_member(id):
    logger.info("PUT /(id)/deactivate")
    try:
        member = member_db.deactivate_member(id)
        if member:
            return "member activated"
        raise HTTPException(status_code=404 ,detail="somthing wrong")
    except Exception as e:
        logger.error(e)

@router.put("/{id}/activate")
def activate_member(id):
    logger.info("PUT /(id)/activate")
    try:
        member = member_db.activate_member(id)
        if member:
            return "member activate"
        raise HTTPException(status_code=404 ,detail="somthing wrong")
    except Exception as e:
        logger.error(e)

@router.put("/{id}/borrow_member")
def increment_borrows(id) :
    logger.info("PUT /(id)/borrow_member")
    try:
        member = member_db.increment_borrows(id)
        if member:
            return "increment borrows successful"
        raise HTTPException(status_code=404 ,detail="somthing wrong")
    except Exception as e:
        logger.error(e)

@router.get("/reports/summary")
def count_active_members():
    logger.info("GET /reports/summary")
    try:
        return member_db.get_all_members()
    except Exception as e:
        logger.error(e)

@router.get("/reports/top-member")
def get_top_member():
    logger.info("GET //reports/top-member")
    try:
        return member_db.get_top_member()
    except Exception as e:
        logger.error(e)





