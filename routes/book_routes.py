from fastapi import APIRouter ,HTTPException
from logs.loger_config import logger
from database.book_db import ConnectDb ,BookDB

router = APIRouter(prefix="/books")
db = ConnectDb()
book_db = BookDB()


@router.post("/table")
def create_table():
    try:
        create = db.create_book_table()
        logger.info("POST /table created")
        if create:
            return "create successful"
        else:
            raise HTTPException(status_code=404 ,detail="id not found")

    except Exception as e:
        logger.error(e)

@router.post("/")
def create_book(bodi:dict):
    try:
        book = book_db.create_new_book(bodi)
        logger.info("POST /create book")
        return book
    except Exception as e:
        logger.error(e)

@router.get("/")
def get_all_books():
    try:
        books = book_db.get_all_books()
        logger.info("GET /get all books")
        return books
    except Exception as e:
        logger.error(e)
        
@router.get("/{id}")
def get_book_by_id(id:int):
    try:
        book = book_db.get_book_by_id(id)
        logger.info("GET /books/id")
        return book
    except Exception as e:
        logger.error(e)

@router.put("/{id}")
def update_book(id:int ,data:dict):
    try:
        book = book_db.update_book(id,data)
        logger.info("PUT /books/id")
        if book:
            return "book update succefful"
        raise HTTPException(status_code=404 ,detail="id not found")
    except Exception as e:
        logger.error(e)

@router.put("/{id}/return/{member_id}")
def set_available(id:int ,val:bool ,member_id:int):
    try:
        available = book_db.set_available(id ,val ,member_id)
        logger.info("PUT /return book")
        if available:
            return "return successful"
        else:
            raise HTTPException(status_code=404 ,detail="id not found") 
    except Exception as e:
        logger.error(e)

@router.put("/books/{id}/borrow/{member_id}")
def set_available(id:int ,val:bool ,member_id:int):
    try:
        available = book_db.set_available(id ,val ,member_id)
        logger.info("/borrowed book")
        if available:
            return "borrowed successful"
        else:
            raise HTTPException(status_code=404 ,detail="id not found") 
    except Exception as e:
        logger.error(e)

@router.get("/reports/summary/total")
def count_total_books():
    try:
        total_books = book_db.count_total_books()
        logger.info("GET /reports/summary")
        return total_books
    except Exception as e:
        logger.error(e)

@router.get("/reports/summary/borrowed")
def count_borrowed_books():
    try:
        borrowed_books = book_db.count_borrowed_books()
        logger.info("GET /reports/summary")
        return borrowed_books
    except Exception as e:
        logger.error(e)

@router.get("/reports/summary/return")
def count_return_books():
    try:
        return_books = book_db.count_return_books()
        logger.info("GET /reports/summary")
        return return_books
    except Exception as e:
        logger.error(e)

@router.get("/reports/books-by-genre")
def count_by_genre(genre:str):
    try:
        sum_of_genre_books = book_db.count_by_genre(genre)
        logger.info("GET //reports/books-by-genre")
        return {"genre":genre},sum_of_genre_books
    except Exception as e:
        logger.error(e)

@router.get("/reports/active_borrows_by_member/{member_id}")
def count_active_borrows_by_member(member_id:int):
    try:
        sum_of_active_borrows_by_member = book_db.count_active_borrows_by_member(member_id)
        logger.info("GET /active_borrows_by_member")
        return sum_of_active_borrows_by_member
    except Exception as e:
        logger.error(e)





