

 תיאור:מערכת לניהול סיפרייה:
 המערכת מיועדת לניהול סיפרייה ע"י שרת  api באמצעות  fastapi
 שמתחבר למסד נתונים mysql המערכת תעבוד דרך בקשות http בלבד דרך swagger או postman
 המערכת תגע לעדכן ספרים להוריד ולהוסיף ולבדוק מלאי מול לקוחות 


: mysql עם docker הקוד ליצירת 

docker run --name librarysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=librarydb -p 3306:3306 -v mysql_data:/var/lib/mysql -d mysql:latest

מבנה תיקיות:

library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
| |- loger_config.py
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

מבנה הטבלאות:


### טבלת `books` — שדות

| שדה | הסבר |
| :--- | :--- |
| `id` | מפתח ראשי |
| `title` | כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים |
| `author` | שם המחבר, עמודה לא ריקה, מקסימום 50 תווים |
| `genre` | ערכי `genre` מותרים: Fiction \| Non-Fiction \| Science \| History \| Other.<br>מומש כעמודת ENUM במסד הנתונים, כל ערך אחר מחזיר שגיאה, עמודה לא ריקה |
| `is_available` | האם הספר זמין להשאלה — FALSE מסמן הושאל, עמודה לא ריקה |
| `borrowed_by_member_id` | מזהה החבר שמחזיק את הספר — NULL אם זמין |

### טבלת `members` — שדות

| שדה | הסבר |
| :--- | :--- |
| `id` | מפתח ראשי |
| `name` | שם החבר, עמודה לא ריקה, מקסימום 50 תווים |
| `email` | כתובת מייל — ייחודית, עמודה לא ריקה |
| `is_active` | האם החבר פעיל — FALSE לא יכול להשאיל, עמודה לא ריקה |
| `total_borrows` | מונה סה"כ השאלות — עולה ב-1 בכל השאלה, עמודה לא ריקה |

חוקי המערכת:

1 יצירת ספר המשתמש שולח genre/author/title — המערכת מוסיפה
is_available=True, borrowed_by=NULLערך כל — Fiction / Non-Fiction / Science / 

2 History / Other להיות חייב genre 
אחר מחזיר שגיאה
יש לוודא הן בהוספה )POST )והן בעדכון )PATCH)

3 יצירת חבר המשתמש שולח email/name — המערכת מוסיפה ,True=active_is
total_borrows=0

4 email חייב להיות ייחודי — אם קיים כבר מחזיר שגיאה

5 חבר לא פעיל אם False=active_is — אי אפשר להשאיל ספר

6 ספר לא זמין אי אפשר להשאיל ספר שכבר מושאל )False=available_is)

7 מקסימום
ספרים
חבר לא יכול להחזיק יותר מ3- ספרים בו-זמנית

8 החזרת ספר ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו


          Endpoints:
Books:


Method | Endpoint | תיאור
| :--- | :--- | ---
POST | books/ | יצירת ספר
GET | books/ | כל הספרים  
GET  | /books/{id} | לפי ספר ID
PATCH | /books/{id} | ספר עדכון
PATCH | /books/{id}/borrow/{member_id} | לחבר ספר השאלת
PATCH | /books/{id}/return/{member_id} | מחבר ספר החזרת

Members:


Method | Endpoint | תיאור
| :--- | :--- | ---
POST | members | /יצירת חבר  
GET | /members | כל החברים 
GET | /members/{id} | ID לפי חבר
PATCH | /members/{id} | חבר עדכון
PATCH | /members/{id}/deactivate | חבר השבתת
PATCH | /members/{id}/activate |  חבר הפעל

Reports:

Method | Endpoint | תיאור
| :--- | :--- | ---
GET | /reports/summary | כללי דוח
GET | /reports/books-by-genre | אנר'ז לפי ספרים
GET | /reports/top-member | פעיל הכי החבר

===

## זרימת המערכת:


מנהל
    ספרים
        יצירת ספר 
                Endpoint POST /books
                create_book(data) 
        החזרת כל הספרים
                Endpoint GET  /books
                get_all_books()
        
    חברים
    דוחות

===

## הוראות הרצה:

uvicorn main:app --reloade

